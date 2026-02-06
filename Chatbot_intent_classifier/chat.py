# Import necessary libraries
import random
import json
import torch

# Import custom modules for the neural network model and text processing
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

# Set the device to GPU if available, otherwise use CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load the intents JSON file which contains the training data and responses
with open('intents.json', 'r', encoding='utf-8') as json_data:
    intents = json.load(json_data)

# Load the trained model data
FILE = "data.pth"
data = torch.load(FILE)

# Extract the model parameters and other data from the loaded file
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

# Initialize the neural network model with the extracted parameters
model = NeuralNet(input_size, hidden_size, output_size).to(device)
# Load the trained model state
model.load_state_dict(model_state)
# Set the model to evaluation mode
model.eval()

# Define the bot's name
bot_name = "Sam"

def get_response(msg):
    """
    Generate a response from the chatbot based on the user's input message.
    
    Parameters:
    msg (str): The input message from the user.
    
    Returns:
    str: The chatbot's response.
    """
    # Tokenize the input message
    sentence = tokenize(msg)
    # Convert the tokenized sentence to a bag of words
    X = bag_of_words(sentence, all_words)
    # Reshape the input to match the model's expected input shape
    X = X.reshape(1, X.shape[0])
    # Convert the numpy array to a PyTorch tensor and move it to the appropriate device
    X = torch.from_numpy(X).to(device)

    # Perform a forward pass through the model to get the output
    output = model(X)
    # Get the predicted tag index with the highest score
    _, predicted = torch.max(output, dim=1)

    # Get the corresponding tag from the tags list
    tag = tags[predicted.item()]

    # Calculate the softmax probabilities for the output
    probs = torch.softmax(output, dim=1)
    # Get the probability of the predicted tag
    prob = probs[0][predicted.item()]
    # If the probability is greater than 0.75, return a random response from the corresponding intent
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    
    # If the probability is less than 0.75, return a fallback response
    return "I do not understand...any more clarification"

if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        # Get the user's input
        sentence = input("You: ")
        # If the user types 'quit', exit the chat
        if sentence == "quit":
            break

        # Generate a response from the chatbot
        resp = get_response(sentence)
        # Print the chatbot's response
        print(resp)