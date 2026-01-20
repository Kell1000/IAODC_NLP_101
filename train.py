# Import required libraries
import numpy as np
import json
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

import nltk
nltk.download('punkt_tab')

# Import custom utilities for text processing and the neural network model
from nltk_utils import bag_of_words, tokenize, stem
from model import NeuralNet

# Load the intents JSON file which contains the training data
with open('intents.json', 'r', encoding='utf-8') as f:
    intents = json.load(f)

# Initialize lists to hold all words, tags, and sentence-tag pairs
all_words = []
tags = []
xy = []

# Loop through each intent in the JSON file
for intent in intents['intents']:
    tag = intent['tag']  # Get the tag for the current intent
    tags.append(tag)  # Add the tag to the list of tags
    for pattern in intent['patterns']:
        w = tokenize(pattern)  # Tokenize each sentence into words
        all_words.extend(w)  # Add the words to the list of all words
        xy.append((w, tag))  # Add the sentence and tag pair to the list

# Define a list of words to ignore during processing
ignore_words = ['?', '.', '!']
# Stem and lower each word, and remove duplicates and sort
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
tags = sorted(set(tags))

# Print some statistics about the data
print(len(xy), "patterns")
print(len(tags), "tags:", tags)
print(len(all_words), "unique stemmed words:", all_words)

# Create training data in the form of bag-of-words vectors and corresponding labels
X_train = []
y_train = []
for (pattern_sentence, tag) in xy:
    bag = bag_of_words(pattern_sentence, all_words)  # Create a bag of words for each sentence
    X_train.append(bag)  # Add the bag of words to the training data
    label = tags.index(tag)  # Get the index of the tag
    y_train.append(label)  # Add the label to the training data

# Convert training data to numpy arrays
X_train = np.array(X_train)
y_train = np.array(y_train)

# Define hyperparameters for the neural network
num_epochs = 2000
batch_size = 8
learning_rate = 0.001
input_size = len(X_train[0])  # Size of input layer
hidden_size = 7  # Size of hidden layer
output_size = len(tags)  # Size of output layer (number of tags)
print(input_size, output_size)

# Define a custom dataset class for loading the training data
class ChatDataset(Dataset):

    def __init__(self):
        self.n_samples = len(X_train)  # Number of samples
        self.x_data = X_train  # Feature data
        self.y_data = y_train  # Label data

    # Support indexing such that dataset[i] can be used to get the i-th sample
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    # Return the size of the dataset
    def __len__(self):
        return self.n_samples

# Create a dataset and a dataloader for batching and shuffling the data
dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset,
                          batch_size=batch_size,
                          shuffle=True,
                          num_workers=0)

# Set the device to GPU if available, otherwise use CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Initialize the neural network model
model = NeuralNet(input_size, hidden_size, output_size).to(device)

# Set the loss function and optimizer
criterion = nn.CrossEntropyLoss()  # Loss function
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)  # Optimizer

# Train the model
epo_list = []
loss_list = []

for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)
        
        # Forward pass: compute predicted outputs by passing inputs to the model
        outputs = model(words)
        
        # Calculate the loss
        loss = criterion(outputs, labels)
        
        # Backward pass: compute gradient of the loss with respect to model parameters
        optimizer.zero_grad()
        loss.backward()
        
        # Perform a single optimization step (parameter update)
        optimizer.step()
        
    # Print the loss every 50 epochs
    if (epoch+1) % 50 == 0:
        print (f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')
        epo_list.append(epoch)
        loss_list.append(loss.item())
print(epo_list)

print(f'final loss: {loss.item():.4f}')

# Save the trained model
data = {
"model_state": model.state_dict(),
"input_size": input_size,
"hidden_size": hidden_size,
"output_size": output_size,
"all_words": all_words,
"tags": tags
}

FILE = "data.pth"
torch.save(data, FILE)

print(f'training complete. file saved to {FILE}')