import cv2
import numpy as np

def apply_hsv(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask_params = {
        'min_blue': 40,
        'min_green': 0,
        'min_red': 0,
        'max_blue': 120,
        'max_green': 255,
        'max_red': 255
    }

    lower_mask = np.array([mask_params['min_blue'], mask_params['min_green'], mask_params['min_red']])
    upper_mask = np.array([mask_params['max_blue'], mask_params['max_green'], mask_params['max_red']])
    mask = cv2.inRange(hsv, lower_mask, upper_mask)

    return mask

