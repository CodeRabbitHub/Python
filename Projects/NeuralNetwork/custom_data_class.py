import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
from torchvision.datasets import MNIST
from torch.utils.data import Dataset, DataLoader


# Step 1: Create a custom dataset class
class CustomMNISTDataset(Dataset):
    def __init__(self, mnist_dataset, transform=None):
        self.data = mnist_dataset
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
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
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
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
