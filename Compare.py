import numpy as np
import cv2

def isImgEqual(lhs, rhs): #lhs, rhs are strings of img location
    img1 = cv2.imread(lhs)
    img2 = cv2.imread(rhs)
    if np.array_equal(img1, img2):
        return True
    #print(img1)
    #print(img2)
    return False