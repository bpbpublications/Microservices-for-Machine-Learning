
# You need to install pysyft: pip install syft[udacity]
import syft as sy
import torch
import numpy as np

# Create a hook to PyTorch
hook = sy.TorchHook(torch)

def private_average(data, epsilon):
    """Compute a differentially private average using Laplace mechanism."""
    tensor_data = torch.tensor(data)
    average = tensor_data.float().mean()
    
    beta = 1.0 / epsilon
    noise = torch.tensor(np.random.laplace(0, beta, 1))
    
    return average + noise

# INPUT
ratings = [5, 4.5, 3.5, 5, 4]
epsilon = 0.1

# PROCESS
private_avg = private_average(ratings, epsilon)

# OUTPUT
print(private_avg)
