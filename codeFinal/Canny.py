import cv2
import numpy as np

def apply_canny(img):
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(img, 50, 100)
    return edges