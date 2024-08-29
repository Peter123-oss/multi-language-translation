import torch
class Lenet5(torch.nn.Module):
    # 构造方法
    def __init__(self):
        self.layer1 = torch.nn.Conv2d(in_channels=1, out_channels=6, kernel_size=(5, 5), padding=0)
        # 池化 relu
        self.layer2 = torch.nn.Conv2d(in_channels=6, out_channels=16, kernel_size=(5, 5), padding=0)
        # 池化 relu
        self.layer3 = torch.nn.Conv2d(in_channels=16, out_channels=120, kernel_size=(5, 5), padding=0)
        self.layer4 = torch.nn.Linear(120, 84)
        self.layer5 = torch.nn.Linear(84, 10)

    def forward(self, input):
        # input N*32*32*1
        # ------------1--------------
        output1 = self.layer1(input)
        output1 = torch.nn.functional.relu(output1)
        output1 = torch.nn.functional.max_pool2d(output1, kernel_size=(2, 2))
        # ------------2--------------
        output2 = self.layer2(output1)
        output2 = torch.nn.functional.relu(output2)
        output2 = torch.nn.functional.max_pool2d(output2, kernel_size=(2, 2))
        # ------------3--------------
        output3 = self.layer3(output2)
        output3 = torch.nn.functional.relu(output3)
        output3 = torch.nn.functional.max_pool2d(output3, kernel_size=(2, 2))
        # ------------4--------------
        output4 = self.layer4(output3)
        output4 = torch.nn.functional.relu(output4)
        # ------------5--------------
        output5 = self.layer5(output4)
        return output5


l = Lenet5()
y = l(x)