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
        # find the biggest contour (c) by the area
        c = max(contours, key = cv2.contourArea)
        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        print(box)
        print(type(box))
        #img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        #cv2.drawContours(img, [box], 0, (0, 255, 255), 3)

        # draw the biggest rectangle not vertical
        # for cnt in contours:
        #     rect = cv2.minAreaRect(cnt)
        #     box = cv2.boxPoints(rect)
        #     box = np.int0(box)
        #     cv2.drawContours(img, [box], 0, (0, 255, 255), 25)
    else:
        box = np.zeros((4, 2), dtype=int)

    return img, box

