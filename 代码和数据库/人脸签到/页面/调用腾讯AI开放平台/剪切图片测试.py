from PIL import Image

path = 'C:/Users/m1309/Desktop/测试图集/class_1.jpg'
img = Image.open(path)
print(img.size)
cropped = img.crop((0, 0, 100, 100))  # (left, upper, right, lower)
cropped.save('C:/Users/m1309/Desktop/测试图集/crop_1.jpg')