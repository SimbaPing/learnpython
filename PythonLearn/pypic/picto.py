# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.....author: Ping
....contact: uppjs@qq.com
.......file: picto.py
.......time: 2018/08/17 14:10:33
Created with Visual Studio Code.
description:
"""

import numpy as np
from PIL import Image


def img_to_char(image_path, height):
    """
    将图片转化为字符
    image_path是图片的路径
    height是字符串图片的高度
    """

    # 读取图片
    img = Image.open(image_file)
    img_width, img_height = img.size
    # 假设字符的宽度是高度的3倍
    width = 3 * height * img_width // img_height
    img = img.resize((width, height), Image.ANTIALIAS)
    # 读取图片的灰度值矩阵
    data = np.array(img.convert('L'))
    # 设定字符,字符数要是256的因子，这里取32
    chars = "#RMNHQODBWGPZ*@$C&98?32I1>!:-;. "
    N = len(chars)
    # 计算每个字符的区间,//取整
    n = 256 // N
    # result是字符结果
    result = ''
    for i in range(height):
        for j in range(width):
            result += chars[data[i][j] // n]
        result += '\n'
    with open('img.txt', mode='w') as f:
        f.write(result)


if __name__ == '__main__':
    image_file = '10.jpg'
    height = 100
    img_to_char(image_file, height)