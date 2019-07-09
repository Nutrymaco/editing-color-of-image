from PIL import Image
from PicFunc import *
import numpy as np
import math


def convertDegreesToRadian(degrees):
    return degrees*math.pi/180


def getRotatedImage(path_to_image, x_rotate=0, y_rotate=0, z_rotate=0):

    original = parseImage(path_to_image)
    width, height = original.size
    pixels_list = getListofPixels(original)

    if x_rotate:  # red
        x_rotate_matrix = getXRotatingMatrix(x_rotate)
        pixels_list = getChangedPixels(pixels_list, x_rotate_matrix)

    if y_rotate:  # green
        y_rotate_matrix = getYRotationMatrix(y_rotate)
        pixels_list = getChangedPixels(pixels_list, y_rotate_matrix)

    if z_rotate:  # blue
        z_rotate_matrix = getZRotationMatrix(z_rotate)
        pixels_list = getChangedPixels(pixels_list, z_rotate_matrix)

    return getImageFromPixelsList(pixels_list, width, height)



def getXRotatingMatrix(degrees):
    radian = convertDegreesToRadian(degrees)
    rotate_matrix = np.array(
        [
            [1, 0, 0],
            [0, np.cos(radian), -np.sin(radian)],
            [0, np.sin(radian), np.cos(radian)]
        ]
    )

    return rotate_matrix


def getYRotationMatrix(degrees):
    radian = convertDegreesToRadian(degrees)
    rotate_matrix = np.array(
        [
            [np.cos(radian), 0, np.sin(radian)],
            [0, 1, 0],
            [-np.sin(radian), 0, np.cos(radian)]
        ]
    )

    return rotate_matrix


def getZRotationMatrix(degrees):
    radian = convertDegreesToRadian(degrees)
    rotate_matrix = np.array(
        [
            [np.cos(radian), -np.sin(radian), 0],
            [np.sin(radian), np.cos(radian),0],
            [0, 0, 1]
        ]
    )

    return rotate_matrix


