# @Time : 2021/12/4 9:20
import os
import cv2
import random
import numpy as np

path1 = "C:\\Users\C\Documents\GitHub\LLproject\dataset\Image\\"
path2 = "C:\\Users\C\Documents\GitHub\LLproject\dataset\Label\\"
f_image = os.listdir(path1)
f_lable = os.listdir(path2)
aa = []
n = 0

def random_crop_with_points(img, save_point_small, w, h,
                            save_point_bigx, save_point_bigy, save_point_w_big, save_point_h_big,
                            save_class):
    top, bottom, lft, r = 0, 0, 0, 0
    #h, w = img.shape[: 2]
    points = np.array(save_point_small, np.int32)
    min_x, min_y, max_x, max_y = np.min(points[:, 0]), \
                                 np.min(points[:, 1]), \
                                 np.max(points[:, 0]), \
                                 np.max(points[:, 1])
    print(min_x, min_y, max_x, max_y)

    if min_x == max_x :#or max_x < 112 or max_y < 112:
        return img#1
    #x_center, y_center = (min_x + max_x)/2,(min_y + max_y)/2
    x_limit = max_x - min_x
    y_limit = max_y - min_y
    min_x, max_x, min_y, max_y = min_x - 32, \
                                 max_x + 20, \
                                 min_y - 10, \
                                 max_y + 10
    if y_limit < 224 :
        top, bottom = int((224 - y_limit)/2), int((224 - y_limit)/2)
    if x_limit < 224 :
        lft, r =  int((224 - x_limit)/2), int((224 - x_limit)/2)
    #wn, hn, xn, yn
    new_img = img[min_x: max_x, min_y: max_y, :]
    cv2.imshow('1', new_img)
    cv2.waitKey(0)
    print(lft, r,top, bottom)
    new_img = cv2.copyMakeBorder(new_img, lft, r,top, bottom,  borderType=cv2.BORDER_REPLICATE)
    s2p = new_img.shape
    sz2 = s2p[0]  # height(rows) of image
    sz2 = s2p[1]  # width(colums) of image
    file_save_txt = open('C:\\Users\C\Documents\GitHub\LLproject\dataset\Label\\' + str(100000 + n).zfill(6) + '.txt',                    'w')
    for number_save in range(len(w)):
        savex_before, savey_before = (float(save_point_small[number_save][0]) - min_x + lft),\
                                     (float(save_point_small[number_save][1]) - min_y + top)
        save_x, save_y, save_w, save_h = round(savex_before/s2p[1],2), \
                                         round(savey_before/s2p[0],2),\
                                         w[number_save] / s2p[1], \
                                         h[number_save] / s2p[0]

        file_save_txt.write(str(int(save_class[n]))+" "+
                            str(save_x,)+" "+
                            str(save_y,)+" "+
                            str(float(save_w))+" "+
                            str(float(save_h))+'\n')
    return new_img

def chuli(image,n):
    save_point_bigx = []
    save_point_bigy = []
    save_point_h = []
    save_point_w = []
    save_point_h_big = []
    save_point_w_big = []
    save_class = []
    save_point_small = np.array([[0, 0]])
    save_point_small = np.array(save_point_small, np.int32)
    i = 1
    img = cv2.imread("C:\\Users\C\Documents\GitHub\LLproject\dataset\Image\\"+image)
    sp = img.shape
    sz1 = sp[0]#height(rows) of image
    sz2 = sp[1]#width(colums) of image
    #if sz1 < 350 or sz2 < 350:
        #return 1
    with open("C:\\Users\C\Documents\GitHub\LLproject\dataset\Label\\"+f_lable[n], "r") as f:

        for line in f.readlines():
            data = line.split('\n\t')
            for sss in data:
                sub_str = sss.split(' ')
                numbers_float = map(float, sub_str)
                numbers_float = list(numbers_float)
                x = sp[0] * numbers_float[2]
                y = sp[1] * numbers_float[1]
                w = sp[0] * numbers_float[3]
                h = sp[1] * numbers_float[3]
                #save_class_before = numbers_float[0]
                s = w*h
                limit_x = sp[0] - 10
                limit_y = sp[1] - 20
                if i == 1 and s < 1024 and x > 10 and y > 32 and x < limit_x and y < limit_y:
                    save_point_small = ([[x,y]])
                    save_point_w = [w]
                    save_point_h = [h]
                    save_class = [numbers_float[0]]
                    i = 0
                elif s < 1024 and x > 32 and y > 10 and x < limit_x and y < limit_y:
                    xy = ([[x,y]])
                    save_point_small = np.append(save_point_small, xy, axis=0)
                    save_point_w.append(w)
                    save_point_h.append(h)
                    save_class.append(numbers_float[0])
                    print(save_point_small)
                else:
                    save_point_bigx.append(x)
                    save_point_bigy.append(y)
                    save_point_w_big.append(w)
                    save_point_h_big.append(h)
                    save_class.append(numbers_float[0])
            #print(xy)
            #x_limit, y_limit = sp[0] - 112, sp[1] - 112
            #if s < 1024:#and x > 112 and y > 112 and x < x_limit and y < y_limit:
    #print(save_point_bigx,save_point_bigy)
        new_img = random_crop_with_points(img, save_point_small, save_point_w, save_point_h,
                                          save_point_bigx, save_point_bigy, save_point_w_big, save_point_h_big,
                                          save_class)

        #cv2.imwrite( "C:\\Users\C\Documents\GitHub\LLproject\dataset\Image\\" + str(100000+n).zfill(6) + '.jpg', new_img)
        cv2.imshow('1', new_img)
        cv2.waitKey(0)

def main():
    global n
    for number_image in f_image:
        name = f_image[n]
        print(name)
        chuli(name,n)
        n += 1

if __name__ == "__main__":
    main()