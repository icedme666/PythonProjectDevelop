from PIL import Image


# 图像格式转换
def convert():
    # 打开文件获取Image对象
    image = Image.open("test_img.gif")
    # 模式转换为RGB
    image_rgb = image.convert("RGB")
    # 图像保存到文件
    image_rgb.save("python_convert.jpg", "jpeg")


# 改变图像尺寸：直接修改对象自身的图像大小，但比例不变
def thumbnail():
    image = Image.open("test_img.jpg")
    # 计算图像长款的一半
    half_size = (image.size[0]/2, image.size[1]/2)
    # 图像大小降为一半
    image.thumbnail(half_size, Image.ANTIALIAS)
    image.save("python_thumbnail.jpg")


# 改变图像尺寸：修改图片长宽比例
def resize():
    image = Image.open("test_img.jpg")
    # 计算图像长款的一半
    double_size = (image.size[0], image.size[1]*2)
    # 图像大小降为一半
    image_resized = image.resize(double_size, Image.ANTIALIAS)  # ANTIALIAS为滤镜中一种
    image_resized.save("python_resize.jpg")


# 剪裁图片
def crop():
    image = Image.open("test_img.jpg")
    # 根据短边长度求中央正方形的坐标
    if image.size[0] < image.size[1]:  # 当横边较短时
        crop_rect = (0, (image.size[1] - image.size[0])/2, image.size[0], (image.size[1] - image.size[0])/2+image.size[0])
    else:  # 竖边较短时
        crop_rect = ((image.size[0] - image.size[1])/2, 0, (image.size[0] - image.size[1])/2+image.size[1], image.size[1])
    # 剪裁
    image_croped = image.crop(crop_rect)  # crop参数包含长方形剪裁区域的左上角坐标和右下角左边，返回值为存有剪裁图像后图像的image类对象
    # 图像保存至文件
    image_croped.save("python_crop.jpg")


# 滤镜
def pil_filter():
    image = Image.open("test_img.jpg")
    buffer = []
    # 循环逐一获取图像的像素
    for pixel in image.getdata():  # getdata返回一个迭代器，用于逐一访问每一组像素值
        # 将像素反色并存入缓冲区
        buffer.append((255-pixel[0], 255-pixel[1], 255-pixel[2]))  # 反色
    # 用缓冲区内的像素覆盖原有数据
    image.putdata(buffer)
    image.save("python_filter.jpg")


def pil_pixel():
    image = Image.open("test_img.jpg")
    # 右上角的位置
    point = (image.size[0]-1, 0)
    # 获取像素值
    pixel = image.getpixel(point)
    # 改为反色的像素值
    image.putpixel(point, (255-pixel[0], 255-pixel[1], 255-pixel[2]))
    image.save("python_pixel.jpg")


convert()
thumbnail()
resize()
crop()
pil_filter()
pil_pixel()
