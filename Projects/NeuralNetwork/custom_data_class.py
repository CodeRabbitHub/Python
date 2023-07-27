import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
from torchvision.datasets import MNIST
from torch.utils.data import Dataset, DataLoader


# Step 1: Create a custom dataset class
class CustomMNISTDataset(Dataset):
    """
    A custom dataset class to handle MNIST data with optional transformations.

    Parameters:
        mnist_dataset (torch.utils.data.Dataset): The original MNIST dataset.
        transform (callable, optional): A function or callable object that takes an image
            tensor as input and performs transformations on it. Default is None.
    """

    def __init__(self, mnist_dataset, transform=None):
        """
        Initialize the CustomMNISTDataset.

        Args:
            mnist_dataset (torch.utils.data.Dataset): The original MNIST dataset.
            transform (callable, optional): A function or callable object that takes an image
                tensor as input and performs transformations on it. Default is None.
        """
        self.data = mnist_dataset
        self.transform = transform

    def __len__(self):
        """
        Get the number of samples in the dataset.

        Returns:
            int: The total number of samples in the dataset.
        """
        return len(self.data)

    def __getitem__(self, idx):
        """
        Get a single sample from the dataset at the given index.

        Args:
            idx (int): Index of the sample to retrieve.

        Returns:
            tuple: A tuple containing the transformed image tensor and its corresponding label.
        """
        image, label = self.data[idx]
        if self.transform:
            image = self.transform(image)
        return image, label


# Step 2: Load and preprocess the MNIST data
transform = transforms.Compose(
    [transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))]
)
train_dataset = MNIST(root="./data", train=True, download=True)
test_dataset = MNIST(root="./data", train=False, download=True)

train_dataset = CustomMNISTDataset(train_dataset, transform=transform)
test_dataset = CustomMNISTDataset(test_dataset, transform=transform)

batch_size = 32
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)


# Step 3: Define the neural network (same as before)
class NeuralNetwork(nn.Module):
    """
    A simple feedforward neural network model for MNIST digit classification.

    This class inherits from torch.nn.Module and defines the architecture of the neural network.

    The neural network consists of two fully connected (dense) layers with ReLU activation.

    The input layer has 28*28 (784) neurons, and the hidden layer has 128 neurons.
    The output layer has 10 neurons corresponding to the 10 possible classes (digits 0 to 9).

    Note:
        The input images must be flattened to a 1D tensor of size 28*28 before passing through the network.

    """

    def __init__(self):
        """
        Initialize the NeuralNetwork model.

        This constructor sets up the neural network architecture by defining the layers.

        Layers:
            - Fully connected layer (fc1) with 784 input neurons and 128 output neurons.
            - Fully connected layer (fc2) with 128 input neurons and 10 output neurons.

        """
        super(NeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        """
        Perform forward pass through the neural network.

        Args:
            x (torch.Tensor): Input tensor of size (batch_size, 28*28).

        Returns:
            torch.Tensor: Output tensor of size (batch_size, 10) representing class scores.
        """
        x = x.view(-1, 28 * 28)  # Flatten the input image to a 1D tensor
        x = torch.relu(
            self.fc1(x)
        )  # Apply ReLU activation to the first fully connected layer
        x = self.fc2(
            x
        )  # Output from the second fully connected layer (scores for each class)
        return x


# Step 4: Train the neural network
model = NeuralNetwork()
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)
epochs = 10


def train_model(model, train_loader, criterion, optimizer, epochs):
    """
    Train the neural network model using the specified training data and hyperparameters.

    Args:
        model (NeuralNetwork): The neural network model to be trained.
        train_loader (torch.utils.data.DataLoader): DataLoader containing the training data.
        criterion (torch.nn.Module): Loss criterion used to compute the loss.
        optimizer (torch.optim.Optimizer): Optimization algorithm used to update the model's parameters.
        epochs (int): The number of training epochs (iterations over the entire training dataset).

    Returns:
        list: A list containing the average loss at the end of each epoch.

    """
    epoch_losses = []  # List to store the average loss for each epoch

    for epoch in range(epochs):
        total_loss = 0.0

        for images, labels in train_loader:
            optimizer.zero_grad()  # Clear gradients of all optimized variables
            outputs = model(images)  # Forward pass: compute predicted outputs
            loss = criterion(outputs, labels)  # Compute the loss
            loss.backward()  # Backpropagation: compute gradients of the loss w.r.t. model parameters
            optimizer.step()  # Update model parameters using the gradients
            total_loss += loss.item()  # Accumulate the loss for this batch

        epoch_loss = total_loss / len(train_loader)  # Average loss for the epoch
        epoch_losses.append(epoch_loss)

        print(f"Epoch {epoch + 1}/{epochs}, Loss: {epoch_loss}")

    return epoch_losses


# Step 5: Test the trained model
def test_model(model, test_loader):
    """
    Evaluate the trained neural network model on the test dataset.

    Args:
        model (NeuralNetwork): The trained neural network model to be evaluated.
        test_loader (torch.utils.data.DataLoader): DataLoader containing the test data.

    Returns:
        float: The accuracy of the model on the test dataset.

    """
    correct = 0
    total = 0

    # Disable gradient computation during testing
    with torch.no_grad():
        for images, labels in test_loader:
            outputs = model(images)  # Forward pass: compute predicted outputs
            _, predicted = torch.max(
                outputs.data, 1
            )  # Get the predicted class with highest score
            total += labels.size(
                0
            )  # Accumulate the number of samples in the test dataset
            correct += (
                (predicted == labels).sum().item()
            )  # Count the number of correct predictions

    accuracy = 100 * correct / total  # Compute the accuracy as a percentage
    print(f"Test Accuracy: {accuracy:.2f}%")
    return accuracy
