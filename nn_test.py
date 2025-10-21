import torch 

x = torch.rand(3)

print(x, torch.cuda.is_available())