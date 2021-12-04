import cv2

def random_crop_with_points(image, x, y, w, h):
    """随机裁剪图像，并计算points在裁剪后的图像中的位置.
    Args:
        image: ,: [(x, y), ...]，原图像中的坐标点集合
    Return:
        new_img: 裁剪后的图像
        new_pts: [(x, y), ...]，原图中的点在裁剪后的图中的位置
    """
    '''
    h, w = image.shape[: 2]
    points = np.array(points, np.int32)
    min_x, min_y, max_x, max_y = np.min(points[:, 0]), np.min(points[:, 1]), np.max(points[:, 0]), np.max(points[:, 1])
    

     t, b, lft, r = (random.randint(0, min_y),
                    random.randint(max_y + 1, h) if max_y + 1 < h else max_y + 1,
                    random.randint(0, min_x),
                    random.randint(max_x + 1, w) if max_x + 1 < w else max_x + 1)
'''
    t, b, lft, r =(int(y-160), int(y+160), int(x-160), int(x+160))
    print(t)
    new_img = image[t: b, lft: r, :]
    wn, hn= w/320, h/320
    xn, yn = (x - lft)/320, (y - t)/320


    return new_img, new_pts


img = cv2.imread('D:\pycharm_project\data\VOC2028\JPEGImages\\000002.jpg')
new_img, new_pts = random_crop_with_points(img,[(100,100),(100,100)])
cv2.imshow('1',new_img)
cv2.waitKey(0)
