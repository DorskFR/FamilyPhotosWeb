import numpy as np

def order_points(box):
    rect = np.zeros((4, 2), dtype="float32")
    # A B
    # D C
    # Add x,y values for each point
    # A will have the smallest x,y sum
    # C will have the largest x,y sum
    s = box.sum(axis=1)
    rect[0] = box[np.argmin(s)]
    rect[2] = box[np.argmax(s)]

    # calculate x,y diff for each point
    # B will have the smallest difference
    # D will have the largest difference
    diff = np.diff(box, axis=1)
    rect[1] = box[np.argmin(diff)]
    rect[3] = box[np.argmax(diff)]

    return rect
