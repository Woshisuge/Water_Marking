import cv2
import os
import numpy.core._methods
import numpy.lib.format
from PIL import Image
import time
import numpy as np
import functools
import sys
# 图像水印加密算法
# 扩频的鲁棒性LSB水印
# 扩频次数
enlarge_size = 5


def embedding_info(picname, savename, text):
    text += '#%#' #作为结束标记
    try:
        im = np.array(Image.open(picname))
    except:
        print("无法获得该图像，请检查文件名")
        time.sleep(3)
        sys.exit()
        
    rows, columns, colors = im.shape
    embed = []
    for c in text:
        bin_sign = (bin(ord(c))[2:]).zfill(16)
        for i in range(16):
            embed.append(int(bin_sign[i]))
    
    count = 0
    for row in range(rows):
        for col in range(columns):
            for color in range(colors):
                if count < len(embed):
                    im[row][col][color] = im[row][col][color] //2 * 2 + embed[count]
                    count += 1

    Image.fromarray(im).save(savename)

def extract_info(picname):
    try:
        im = np.array(Image.open(picname))
    except:
        print("无法获得该图像，请检查文件名")
        time.sleep(2)
        sys.exit()

    rows, columns, colors = im.shape
    text = ""
    extract = np.array([], dtype = int)

    count = 0
    for row in range(rows):
        for col in range(columns):
            for color in range(colors):
                extract = np.append(extract, im[row][col][color] % 2)
                count += 1
                if count % 16 == 0:
                    bcode = functools.reduce(lambda x, y: str(x) + str(y), extract)
                    cur_char = chr(int(bcode, 2))
                    text += cur_char
                    if cur_char == '#' and text[-3:] == '#%#':
                        return text[:-3]
                    extract = np.array([], dtype=int)