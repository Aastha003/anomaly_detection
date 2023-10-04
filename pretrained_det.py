
import torch
import torch.nn as nn
import torch.optim as optim

PATH = '/Users/caast/Downloads/model_unet_vgg_16_best.pt'

class model(nn.Module): 
        def __init__(self):
            super(model, self).__init__()
            self.a = torch.nn.Parameter(torch.rand(1, requires_grad=True))
            self.b = torch.nn.Parameter(torch.rand(1, requires_grad=True))
            self.c = torch.nn.Parameter(torch.rand(1, requires_grad=True))
            #print(self.a, self.b, self.c)

        def load(self):
          try:
            checkpoint = torch.load(PATH)  
            print('\nloading pre-trained model...')
            self.load_state_dict(checkpoint['model'])
            self.optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
            print(self.a, self.b, self.c)
            self.train()
          except: #file doesn't exist yet
            pass

        @property
        def b_opt(self):
            return torch.tanh(self.b)*2

        def train(self):
            print('training...')
            for epoch in range(3):
                print(self.a, self.b, self.c)
            for r in range(5):
                optimizer.zero_grad()
                loss = torch.square(5 * (r > 2) * (3) - model_net.a * torch.sigmoid((r - model_net.b)) * (model_net.c))
                loss.backward(retain_graph=True) #accumulate gradients
                print(loss)

            #checkpoint save
            torch.save({
                'model': model_net.state_dict(),
                'a': model_net.a,
                'b': model_net.b,
                'c': model_net.c,
                'optimizer_state_dict': optimizer.state_dict(),
                }, PATH)

            
            optimizer.step() 
          


model_net = model()
optimizer = optim.Adam(model_net.parameters(), lr = 0.1)
model_net.optimizer = optimizer

model_net.load()
model_net.train()

# Print model's state_dict
print("Model's state_dict:")
for param_tensor in model_net.state_dict():
    print(param_tensor, "\t", model_net.state_dict()[param_tensor].size())

# Print optimizer's state_dict
print("Optimizer's state_dict:")
for var_name in optimizer.state_dict():
    print(var_name, "\t", optimizer.state_dict()[var_name])

print(model_net.a)
print(model_net.b)
print(model_net.c)
