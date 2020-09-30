import cv2

import codeFinal.FileOperations
import codeFinal.MaxArea
import codeFinal.OrderPoints
import codeFinal.Sobel
import codeFinal.Warp
import codeFinal.Hsv
import codeFinal.Canny

ratio = 10

def main(dir_path, filename, ext, filter, crop):
    print(f"dir_path = {dir_path}, filename={filename}, ext={ext}, filter={filter}, crop={crop}")
    img, mask = scan(dir_path, filename, ext, filter, crop)
    filename, maskname = codeFinal.FileOperations.save(dir_path, filename, ext, filter, img, crop, mask)
    return filename, maskname

def scan(dir_path, filename, ext, filter, crop):
    img = codeFinal.FileOperations.load_image(dir_path, filename, ext)
    img, mask = apply_filter(img, filter, crop)
    return img, mask


def apply_filter(img, filter, crop):
    original = img
    img = cv2.resize(img, (int(img.shape[1] / ratio), int(img.shape[0] / ratio)), interpolation=cv2.INTER_AREA)
    if filter == "sobel":
        img = codeFinal.Sobel.apply_sobel(img)
    elif filter == "hsv":
        img = codeFinal.Hsv.apply_hsv(img)
    elif filter == "canny":
        img = codeFinal.Canny.apply_canny(img)
    img, box = codeFinal.MaxArea.contour_max_area(img)
    mask = img.copy()
    mask = cv2.resize(mask, (int(mask.shape[1] * ratio), int(mask.shape[0] * ratio)), interpolation=cv2.INTER_AREA)
    mask = cv2.drawContours(mask, [box.reshape(4, 2) * ratio], 0, (0, 255, 0), 10)
    if crop:
        box = codeFinal.OrderPoints.order_points(box)
        img = codeFinal.Warp.apply_warp(original, box.reshape(4, 2) * ratio)
    else:
        img = cv2.drawContours(original, [box.reshape(4, 2) * ratio], 0, (0, 255, 0), 10)
    return img, mask