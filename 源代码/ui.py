#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter.filedialog import askopenfilename
from tkinter import *  # 导入 Tkinter 库
import image  # 处理图片
import music  # 处理音频
import jpg
import tkinter as tk
import os
import matplotlib.pyplot as plt
from PIL import Image
#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
file_path=''
jpg_path=''
def choice_bmp():
    root = tk.Tk()    # 创建一个Tkinter.Tk()实例
    root.withdraw()       # 将Tkinter.Tk()实例隐藏
    default_dir = r"文件路径"
    global file_path
    file_path = tk.filedialog.askopenfilename(title=u'选择文件', 
        initialdir=(os.path.expanduser(default_dir)))
    file_text.set(file_path)
    print(file_path)
    if file_path[-3:]!='wav':

        image = Image.open(file_path)
        plt.figure(1)
        plt.imshow(image,'gray')
        plt.title('图片显示')
        plt.axis('off')
        plt.show()

def choice_():
    root = tk.Tk()    # 创建一个Tkinter.Tk()实例
    root.withdraw()       # 将Tkinter.Tk()实例隐藏
    default_dir = r"文件路径"
    global jpg_path
    jpg_path = tk.filedialog.askopenfilename(title=u'选择文件', 
        initialdir=(os.path.expanduser(default_dir)))
    if file_path[-3:]!='wav':
        image = Image.open(jpg_path)
        plt.figure(2)
        plt.imshow(image,'gray')
        plt.title('水印')
        plt.axis('off')
        plt.show()

def start():
    # 处理图片
    if first_first_bool.get() == True and first_second_bool.get() == False :
        if second_first_bool.get() == True and second_second_bool.get() == False and second_third_bool.get()==False and second_four_bool.get()==False:
            # 图片水印加密
            image_file=file_path
            image_file = file_text.get()  # 获得文件地址
            message = water_text.get()  # 获得水印
            output = "D:/test/out_str.png"  # 输出文件
            alpha = 5  # 加密系数
            image.embedding_info(image_file,output,message)
            # image.SpreadSpectrumEmbed(image_file, output, message, alpha)
        elif second_first_bool.get() == False and second_second_bool.get() == True and second_third_bool.get()==False and second_four_bool.get()==False:
            
            makefile=file_path
            makefile = file_text.get()
            bigger_x = 2
            bigger_y = 4.
            more_number = 1
            string = image.extract_info(makefile)
            # string = image.decode_get_watermark(makefile, more_number, bigger_y, bigger_x)
            encode_text.set(string)
        elif second_first_bool.get() == False and second_second_bool.get() == False and second_third_bool.get()==True and second_four_bool.get()==False:

            output = "D:/test/out_pic.png"
            jpg.addWaterMarking(file_path,jpg_path,output)
        elif second_first_bool.get() == False and second_second_bool.get() == False and second_third_bool.get()==False and second_four_bool.get()==True:

            output = file_path  # 输出文件
            output = file_text.get()
            jpg.testWaterMarking(output)
        else:
            print("不能同时加、解密")
    # 处理音频
    elif first_first_bool.get() == False and first_second_bool.get() == True:
        if second_first_bool.get() == True and second_second_bool.get() == False and second_third_bool.get()==False and second_four_bool.get()==False:
            message = file_path
            message = water_text.get()  # 获得水印
            cover_audio = file_text.get()  # 获得文件地址
            output = "D:/test/ok.wav"  # 输出文件
            music.lsb_watermark(cover_audio, message, output)
        elif second_first_bool.get() == False and second_second_bool.get() == True and second_third_bool.get()==False and second_four_bool.get()==False:
            message = file_path
            message = file_text.get()
            string = music.recover_lsb_watermark(message)
            encode_text.set(string)
        else:
            print("参数设置错误")
    else:
        print("参数设置错误")


if __name__ == '__main__':
    root = Tk()  # 创建窗口对象的背景色
    root.title("python水印整合")  # 窗口标题
    root.geometry("500x500")  # 窗口大小
    # 第一块选择区
    text1 = Label(root, text="Please check")  # 标题
    text1.pack()

    first_first_bool = BooleanVar()
    first_first = Checkbutton(root, text="图片", variable=first_first_bool)
    first_first.pack()

    first_second_bool = BooleanVar()
    first_second = Checkbutton(root, text="音频", variable=first_second_bool)
    first_second.pack()

    # 第二块选择区
    text2 = Label(root, text="Please check")  # 标题
    text2.pack()

    second_first_bool = BooleanVar()
    second_first = Checkbutton(root, text="嵌入字母", variable=second_first_bool)
    second_first.pack()

    second_second_bool = BooleanVar()
    second_second = Checkbutton(root, text="提取字母", variable=second_second_bool)
    second_second.pack()

    second_third_bool = BooleanVar()
    second_third = Checkbutton(root, text="嵌入图片", variable=second_third_bool)
    second_third.pack()

    second_four_bool = BooleanVar()
    second_four = Checkbutton(root, text="提取图片", variable=second_four_bool)
    second_four.pack()


    choice_button = Button(root, 
        text='选择文件',      # 显示在按钮上的文字
        width=15, height=2, 
        command=choice_bmp  )
    choice_button.pack()    # 按钮位置

    choice_jpg = Button(root, 
        text='选择水印文件',      # 显示在按钮上的文字
        width=15, height=2, 
        command=choice_  )
    choice_jpg.pack()    # 按钮位置

    # 输入文件名字
    l1 = Label(root, text="输入文件")
    l1.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
    file_text = StringVar()
    file = Entry(root, textvariable=file_text)
    file.pack()
    # 输入水印
    l2 = Label(root, text="输入水印")
    l2.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
    water_text = StringVar()
    water = Entry(root, textvariable=water_text)
    water.pack()
    # 解密得到的水印
    l3 = Label(root, text="得到的水印")
    l3.pack()
    encode_text = StringVar()
    encode = Entry(root, textvariable=encode_text)
    encode.pack()
    # 确认按钮
    l3 = Label(root, text="是否确认")
    l3.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
    right = Button(root, text="确认", width=19, relief=GROOVE, bg="blue", command=start)  # 按下时触发事件
    right.pack()

    # 循环
    root.mainloop()

