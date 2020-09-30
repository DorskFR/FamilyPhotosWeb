import cv2
import sys
import os
import glob


def load_image(dir_path, filename, ext):
    img = dir_path + filename + '.' + ext
    img = cv2.imread(img)
    if img is None:
        print("Image could not be loaded")
        sys.exit(1)
    return img


def save(dir_path, filename, ext, filter, img, crop, mask):

    maskname = filename + "-" + filter + "mask." + ext
    path = dir_path + maskname
    cv2.imwrite(path, mask)

    if crop:
        filename = filename + "-crop." + ext
        path = dir_path + filename
        cv2.imwrite(path, img)
    else:
        filename = filename + "-" + filter + "." + ext
        path = dir_path + filename
        cv2.imwrite(path, img)

    print(f"{maskname} and {filename} saved")
    return filename, maskname

