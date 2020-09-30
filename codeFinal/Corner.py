import numpy as np
import cv2

def detect_corners(img):

    # first obtain each channel individually
    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]
    # and obtain the grayscale channel
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # and obtain the binary channel
    binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)

    matrix_tl = []
    matrix_tr = []
    matrix_bl = []
    matrix_nr = []

    # then for each corner we are going to apply a matrix search.
    # basically we scan the image using a matrix that has the shape we are looking for
    # if we find a pattern corresponding to our matrix we get the pixel position where we detect the best the pattern

    # we then return the position of the four corners

    return img

