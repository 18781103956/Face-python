from PIL import Image


def resize_img(path, path_goal):
    img = Image.open(path)

    x, y = img.size
    n = 300 / x
    x = int(x * n)
    y = int(y * n)

    img_resize = img.resize((x, y))
    img_resize.save(path_goal)


if __name__ == '__main__':
    path = 'C:/Users/m1309/Desktop/测试图集/zzz.png'
    path_goal = 'C:/Users/m1309/Desktop/测试图集/recrop_1.png'

    resize_img(path, path_goal)






