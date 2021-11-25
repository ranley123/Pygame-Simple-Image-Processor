# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author(s):
# Date:
# Description:

from cmpt120imageProjHelper import *
import numpy as np

def applyRedFilter(img):
    image_array = np.array(img)
    rows, cols, colors = image_array.shape
    print(image_array.shape)
    for i in range(0, rows):
        for j in range(0, cols):
            for k in range(1,2):
                img[i][j][k] = 0
    return img

def applyGreenFilter(img):
    image_array = np.array(img)
    rows, cols, colors = image_array.shape
    print(image_array.shape)
    for i in range(0, rows):
        for j in range(0, cols):
            for k in [0,2]:
                img[i][j][k] = 0

    return img

def applyBlueFilter(img):
    image_array = np.array(img)
    rows, cols, colors = image_array.shape
    print(image_array.shape)
    for i in range(0, rows):
        for j in range(0, cols):
            for k in range(0, 2):
                img[i][j][k] = 0
    return img

def applySepiaFilter(img):
    image_array = np.array(img)
    rows, cols, _ = image_array.shape
    for i in range(0, rows):
        for j in range(0, cols):
            image_array[i][j][0] = min(img[i][j][0] * 0.393 + \
                img[i][j][1] * 0.769 + img[i][j][2] * 0.189, 255)
            image_array[i][j][1] = min(img[i][j][0] * 0.349 + \
                img[i][j][1] * 0.686 + img[i][j][2] * 0.168, 225)
            image_array[i][j][2] = min(img[i][j][0] * 0.272 + \
                img[i][j][1] * 0.534 + img[i][j][2] * 0.131, 255)
    return list(image_array)

def applyWarmFilter(img):
    image_array = np.array(img)
    rows, cols, _ = image_array.shape
    for i in range(0, rows):
        for j in range(0, cols):
            # R value
            r = img[i][j][0]
            if r < 64:
                img[i][j][0] = int(r / 64 * 80)
            elif 64 <= r < 128:
                img[i][j][0] = int((r - 64) / (128 - 64) * 80 + 80)
            else:
                img[i][j][0] = int((r - 128) / (255-128) * (255-160) + 160)
            
            # B value
            b = img[i][j][2]
            if b < 64:
                img[i][j][2] = int(b / 64 * 50)
            elif 64 <= b < 128:
                img[i][j][2] = int((b - 64)/(128-64) * (100-50) + 50)
            else:
                img[i][j][2] = int((b -128)/(255-128) * (255-100) + 100)
    return img 

def applyColdFilter(img):
    image_array = np.array(img)
    rows, cols, _ = image_array.shape
    for i in range(0, rows):
        for j in range(0, cols):
            # B value
            b = img[i][j][2]
            if b < 64:
                img[i][j][2] = int(b / 64 * 80)
            elif 64 <= b < 128:
                img[i][j][2] = int((b - 64) / (128 - 64) * 80 + 80)
            else:
                img[i][j][2] = int((b - 128) / (255-128) * (255-160) + 160)
            
            # R value
            r = img[i][j][0]
            if r < 64:
                img[i][j][0] = int(r / 64 * 50)
            elif 64 <= r < 128:
                img[i][j][0] = int((r - 64)/(128-64) * (100-50) + 50)
            else:
                img[i][j][0] = int((r -128)/(255-128) * (255-100) + 100)
    return img