# Import necessary libraries from PyTorch
import torch
import torch.nn as nn

# Define a neural network class by inheriting from nn.Module
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        """
        Initialize the neural network layers.
        
        Parameters:
        input_size (int): The number of input features.
        hidden_size (int): The number of neurons in the hidden layers.
        num_classes (int): The number of output classes.
        """
        super(NeuralNet, self).__init__()
        # Define the first linear layer (input to hidden)
        self.l1 = nn.Linear(input_size, hidden_size) 
        # Define the second linear layer (hidden to hidden)
        self.l2 = nn.Linear(hidden_size, hidden_size) 
        # Define the third linear layer (hidden to output)
        self.l3 = nn.Linear(hidden_size, num_classes)
        # Define the ReLU activation function
        self.relu = nn.ReLU()
    
    def forward(self, x):
        """
        Perform a forward pass through the network.
        
        Parameters:
        x (torch.Tensor): Input tensor.
        
        Returns:
        torch.Tensor: Output of the neural network.
        """
        # Pass the input through the first layer and apply ReLU activation
        out = self.l1(x)
        out = self.relu(out)
        # Pass the result through the second layer and apply ReLU activation
        out = self.l2(out)
        out = self.relu(out)
        # Pass the result through the third layer (output layer)
        out = self.l3(out)
        # No activation function or softmax is applied to the output
        return out