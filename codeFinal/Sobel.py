import cv2
import numpy as np

def edge_detect(channel):
    sobel_x = cv2.Sobel(channel, cv2.CV_16S, 1, 0)
    sobel_y = cv2.Sobel(channel, cv2.CV_16S, 0, 1)
    sobel = np.hypot(sobel_x, sobel_y)

    sobel[sobel > 255] = 255
    sobel[sobel < 150] = 0
    return sobel

def apply_sobel(img):
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    edge_img = np.max(np.array([
        edge_detect(blurred[:, :, 0]),
        edge_detect(blurred[:, :, 1]),
        edge_detect(blurred[:, :, 2])]), axis=0)

    mean = np.mean(edge_img)
    edge_img[edge_img <= mean] = 0
    edge_img = edge_img.astype(np.uint8)

    return edge_img

