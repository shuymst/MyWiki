import torch
from torchvision import datasets, transforms

def get_data_loaders(batch_size=64):
    transform = transforms.ToTensor()
    train_loader = torch.utils.data.DataLoader(
        datasets.MNIST('.', train=True, download=True, transform=transform),
        batch_size=batch_size, shuffle=True
    )
    test_loader = torch.utils.data.DataLoader(
        datasets.MNIST('.', train=False, transform=transform),
        batch_size=batch_size, shuffle=False
    )
    return train_loader, test_loader