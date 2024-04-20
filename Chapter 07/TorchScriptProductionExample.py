
# TorchScript in production
import torch.jit

# Load the TorchScript model
module = torch.jit.load("model.pt")
