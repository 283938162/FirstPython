from PIL import Image
import sys

from io import BytesIO

'''
Python 里面最常用的图像操作库是Image library（PIL）

Image类的属性
format  mode   size

'''
#
# img_path = 'tx.jpg'
# # 读取一张图片
# im = Image.open(img_path)
#
# # 源文件的文件格式。如果是由PIL创建的图像，则其文件格式为None。
# # 注：test.jpg是JPEG图像，所以其文件格式为JPEG。
#
# print(im.format)
#
# # 图像得模式 这个字符串表明图像所使用像素格式。
# # 该属性典型的取值为“1”，“L”，“RGB”或“CMYK”。
# print(im.mode)
#
# # 图像的尺寸，按照像素数计算。它的返回值为宽度和高度的二元组（width, height）。
# print(im.size)

# 显示一张照片
# im.show()

# im.save('')


#   Image.new(mode, size, color) ⇒ image
# Size是给定的宽/高二元组，这是按照像素数来计算的。 不是坐标点
# im = Image.new('RGBA', (128, 128),'red')
#
# im.show()

# crop

# box = (0, 200, 339, 592)
#
# im_crop = im.crop(box)

# print(box,im_crop.mode,im_crop.size)

# im_crop.show()

'''
sys.args 参与运行的文件数

剪切 粘贴

（1） 将剪切的内容粘贴到一个新的空白版

（2） 将剪切的内容添加到原来的图层之上

这可以使用的方法有两种，第一种是以及被注释掉的方法，即生成一个新的Image，
调用Image.new方法。然后将该image粘贴到需要修改的图片上。

另外一种为了保持图片的前后背景色一致，从图片的最前头拷贝一部分图片（使用crop函数)，
然后在粘贴到需要修改的图片上，来完成最下端文字的覆盖。


crop函数带的参数为(起始点的横坐标，起始点的纵坐标，宽度，高度）

paste函数的参数为(需要修改的图片，粘贴的起始点的横坐标，粘贴的起始点的纵坐标）


paste

box = (0,0)
含义1：将一张图粘贴到另一张图像上。变量box或者是一个给定左上角的2元组，
或者是定义了左，上，右和下像素坐标的4元组，或者为空（与（0，0）一样）。
如果给定4元组，被粘贴的图像的尺寸必须与区域尺寸一样。


'''


def crop_paste():
    # print(sys.argv)
    # if len(sys.argv) == 2:
    #     print('%s <image file>' % __file__)
    #     sys.exit()
    # else:
    #     filename = sys.argv[0]
    #     print(filename)

    filename = 'wzs.jpg'
    img = Image.open(filename)

    width = img.size[0]
    height = img.size[1]

    print('原图宽=%s，高=%s' % (width, height))

    # 剪取距顶部200px等宽的图片
    img_crop = img.crop((0, 0, width, 200))

    # 保存剪裁后的图片
    # img_crop.save('1.png')
    # 显示剪裁后的图片
    # img_crop.show()

    # 新建空白版的宽高
    img_new = Image.new('RGBA', (width, width))

    img_new.paste(img_crop, (0,0))

    img_new_fb = BytesIO()

    img_new.save(img_new_fb,'png')

    print(img_new)
    print(img_new_fb.getvalue())

    # img_new.show()
    # img1 = Image.new('RGBA',(width,10))
    # img.paste(img1, (0, height - 90))
    # img.save(filename)
    #
    # img = Image.open(filename)
    # img.show()


if __name__ == '__main__':
    crop_paste()
