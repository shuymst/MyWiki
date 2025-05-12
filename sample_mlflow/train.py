import mlflow
import torch
from torch import nn, optim
from tqdm import tqdm
from model import MLP
from data_loader import get_data_loaders

def evaluate(model, test_loader):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for X, y in test_loader:
            outputs = model(X)
            _, predicted = torch.max(outputs.data, 1)
            total += y.size(0)
            correct += (predicted == y).sum().item()
    accuracy = correct / total
    return accuracy

def train(epochs=5, lr=1e-3, batch_size=64):
    mlflow.set_experiment("Sample_MNIST")
    with mlflow.start_run():
        mlflow.log_param("epochs", epochs)
        mlflow.log_param("lr", lr)
        mlflow.log_param("batch_size", batch_size)

        model = MLP()
        train_loader, test_loader = get_data_loaders(batch_size)
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(model.parameters(), lr=lr)

        for epoch in range(epochs):
            avg_loss = 0.0
            for X, y in tqdm(train_loader):
                optimizer.zero_grad()
                pred = model(X)
                loss = criterion(pred, y)
                loss.backward()
                optimizer.step()
                avg_loss += loss.item()
            avg_loss /= len(train_loader)
            mlflow.log_metric("train_loss", avg_loss, step=epoch)
            print(f"Epoch {epoch+1}, Loss: {avg_loss:.4f}")
        
        test_accuracy = evaluate(model, test_loader)
        mlflow.log_metric("test_accuracy", test_accuracy)
        print(f"Test Accuracy: {test_accuracy:4f}")

        # モデルの保存
        # mlflow.pytorch.log_model(model, "model")

if __name__ == "__main__":
    train()
