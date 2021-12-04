import cv2
import random
# 你看！
aa = []
img = cv2.imread('D:\pycharm_project\data\VOC2028\JPEGImages\\000378.jpg')
sp = img.shape
sz1 = sp[0]#height(rows) of image
sz2 = sp[1]#width(colums) of image

def random_crop_with_points(image, x, y, w, h):

    #t1, b1, lft1, r1 = (int(y-h/2), int(y+h/2), int(x-w/2), int(x+w/2))
    t, b, lft, r = (int(y-112), int(y+112), int(x-112), int(x+112))
    print(t)
    new_img = image[t: b, lft: r, :]

    wn, hn= w/224, h/224
    xn, yn = (x - lft)/224, (y - t)/224
    return new_img, wn, hn, xn, yn


with open("D:/pycharm_project/data/VOC2028/000/000378.txt", "r") as f:
    for line in f.readlines():
        data = line.split('\n\t')
        for str in data:
            sub_str = str.split(' ')
            numbers_float = map(float, sub_str)
            numbers_float = list(numbers_float)
            x = sp[0] * numbers_float[2]
            y = sp[1] * numbers_float[1]
            print(x,y)
            w = sp[0] * numbers_float[3]
            h = sp[1] * numbers_float[3]
            s = w*h
            x_limit, y_limit = sp[0] - 112, sp[1] - 112
        if s < 1024 and x > 112 and y > 112 and x < x_limit and y < y_limit:
            new_img, wn, hn, xn, yn = random_crop_with_points(img, y, x, w, h)
            for i in range(224):  # 遍历图像x,y
                for j in range(0, 224):
                    for k in range(0, 3):  # 遍历每个通道
                        if not (92 < j < 132 and 82 < i < 220):  # 白色的区域r通道有数值，r为红色，可以通过更改阈值更改下面颜色的赋值
                            new_img.itemset((i, j, k), 0)#random.randint(0,255)

            s2p = new_img.shape
            print(s2p)
            cv2.imshow('1', new_img)
            cv2.waitKey(0)
            break
            '''            
            save_point[i] = x
            save_point[i+1] = y
            i = i + 2
            '''


            #print(x,y)

'''
            print(list(numbers_float))
        if sub_str:
            aa.append(numbers_float)
print(list(aa))
'''
