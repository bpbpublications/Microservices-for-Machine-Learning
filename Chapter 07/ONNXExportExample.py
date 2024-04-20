
# Exporting a PyTorch model to ONNX format
import torch
import torch.onnx

torch.onnx.export(model, dummy_input, "model.onnx")
