from PIL import Image


def crop_img(path, x1, y1, x2, y2, path_goal):
    img = Image.open(path)
    img_crop = img.crop((x1, y1, x2, y2))
    img_crop.save(path_goal)


if __name__ == '__main__':

    path = 'C:/Users/m1309/Desktop/测试图集/class_1.jpg'

    path_goal = 'C:/Users/m1309/Desktop/测试图集/crop_1.jpg'

    crop_img(path_goal, 0, 0, 100, 100, path_goal)
