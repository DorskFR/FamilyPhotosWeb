import cv2
import numpy as np

def contour_max_area(img):
    if len(img.shape) > 2:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5, 5), "uint8")
    img = cv2.dilate(img, kernel, iterations=1)

    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        # find the biggest contour by the area
        c = max(contours, key = cv2.contourArea)
        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
    else:
        box = np.zeros((4, 2), dtype=int)

    return img, box

