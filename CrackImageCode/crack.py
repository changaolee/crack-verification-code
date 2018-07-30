import tesserocr
from PIL import Image


def vertify():
    image = Image.open('code.jpg')

    # 将图片转化为灰度图像
    image = image.convert('L')

    # 将图片进行二值化处理（默认阈值127）
    #image = image.convert('1')

    # 设置阈值为150
    threshold = 150
    table = [0 if i < threshold else 1 for i in range(256)]
    image = image.point(table, '1')

    #image.show()
    result = tesserocr.image_to_text(image)
    print(result)


if __name__ == '__main__':
    vertify()