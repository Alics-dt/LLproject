# @Time : 2021/12/4 9:20

import cv2
import random
import numpy as np

aa = []
img = cv2.imread('C:\\Users\C\Documents\GitHub\LLproject\dataset\Image\\000308.jpg')
sp = img.shape
sz1 = sp[0]#height(rows) of image
sz2 = sp[1]#width(colums) of image

save_point_bigx = []
save_point_bigy = []
save_point_small = np.array([[0, 0]])
save_point_small = np.array(save_point_small, np.int32)

def random_crop_with_points(img, save_point_small):

    #h, w = img.shape[: 2]
    points = np.array(save_point_small, np.int32)
    min_x, min_y, max_x, max_y = np.min(points[:, 0]), np.min(points[:, 1]), np.max(points[:, 0]), np.max(points[:, 1])
    print(min_x, min_y, max_x, max_y)
    #x_center, y_center = (min_x + max_x)/2,(min_y + max_y)/2
    #if
    new_img = img[min_y: max_y, min_x: max_x, :]
    #wn, hn, xn, yn
    return new_img

with open("C:\\Users\C\Documents\GitHub\LLproject\dataset\Label\\000308.txt", "r") as f:
    for line in f.readlines():
        data = line.split('\n\t')
        for str in data:
            sub_str = str.split(' ')
            numbers_float = map(float, sub_str)
            numbers_float = list(numbers_float)
            x = sp[0] * numbers_float[2]
            y = sp[1] * numbers_float[1]
            xy = ([[x,y]])
            print(xy)
            w = sp[0] * numbers_float[3]
            h = sp[1] * numbers_float[3]
            s = w*h
            #x_limit, y_limit = sp[0] - 112, sp[1] - 112
            if s < 1024:#and x > 112 and y > 112 and x < x_limit and y < y_limit:
                save_point_small = np.append(save_point_small, xy, axis=0)
                print(save_point_small)
            else:
                save_point_bigx.append(x)
                save_point_bigy.append(y)

    new_img = random_crop_with_points(img, save_point_small)
    s2p = new_img.shape
    print(s2p)
    cv2.imshow('1', new_img)
    cv2.waitKey(0)
