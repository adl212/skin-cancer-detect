import torch
from PIL import Image
from torchvision import transforms
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
test_transforms = transforms.Compose([transforms.Resize(224),transforms.ToTensor()])
model = torch.load('./aerialmodel.pth')
model.eval()
def predict_image():
    image = Image.open('image.png') 
    image_tensor = test_transforms(image).float()
    image_tensor = image_tensor.unsqueeze_(0)
    input = image_tensor
    input = input.to(device)
    output = model(input)
    index = output.data.cpu().numpy().argmax()
    return index
