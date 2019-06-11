from PIL import Image
from PIL import Image,ImageChops 
def addWaterMarking (pic , mark,out):
    # 预处理
    img = Image.open(pic).convert("RGB")
    width, height = img.size   # 读取大小

    img_mark = Image.open(mark).convert("RGB")
    img_mark = img_mark.resize((width, height)) #缩放水印到文件大小

    # 这几步也可以扔到后面做
    img = img.point(lambda i: (int(i>>2))<<2)
    img_mark = img_mark.point(lambda i: round(i/85))


    # 合成
    img_pixels = list(img.getdata())
    mark_pixels = list(img_mark.getdata())
    # print img_pixels[:10]

    newpixels = [0 for i in range(len(img_pixels))] #先固定列表大小减少动态内存分配

    for index in range(len(img_pixels)):
        #取出来的格式是truple 要先
        list_temp = []
        for i in range(3):
            list_temp.append(img_pixels[index][i] + mark_pixels[index][i])
        newpixels[index] = tuple(list_temp)
    # print newpixels[:10]

    imn = Image.new("RGB", (width, height))
    imn.putdata(data = newpixels)
    # imn.show()
    # 把加水印后的图像用png格式保存 这里不能用压缩格式吖
    imn.save(out)
    return

def equal (im1, im2): 
    return ImageChops.difference(im1, im2).getbbox() is None

def testWaterMarking (pic):
    # 预处理
    img = Image.open(pic).convert("RGB")
    width, height = img.size   # 读取大小

    # img_mark = Image.open(mark).convert("RGB")
    # img_mark = img_mark.resize((width, height)) #缩放水印到文件大小

    img_pixels = list(img.getdata())
    # print img_pixels[:10]
    # 提取出来的水印
    img_get = img.point(lambda i: (int(i&3))*85)
    img_get.show()
    # 正常应该得到的水印
    # img_mark = img_mark.point(lambda i: round(i/85)*85)
    # print(equal(img_get,img_mark))

    # return equal(img_get,img_mark)
