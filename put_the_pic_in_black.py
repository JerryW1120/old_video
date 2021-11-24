import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

def img_resize_to_target_black(image):

    target = np.zeros((1080,1920),dtype=np.uint8)

    bgr_img = cv2.cvtColor(target, cv2.COLOR_GRAY2BGR)

    h = image.shape[0]

    w = image.shape[1]

    for i in range(h):

        for j in range(w):

            bgr_img[i + 130, j + 419, 0] = image[i, j, 0]

            bgr_img[i + 130, j + 419, 1] = image[i, j, 1]

            bgr_img[i + 130, j + 419, 2] = image[i, j, 2]

    return bgr_img

def main_fuc(input_dir, output_dir):
    files =  os.listdir('input_dir')
    files.sort()
    for file in files:

        image = cv2.imread('input_dir' + '\\' + file)

        img_new_black = img_resize_to_target_black(image)

        #cv2.imshow("img_new_black", img_new_black)

        #cv2.waitKey()
        cv2.imwrite('output_dir' + '\\' + file, img_new_black)