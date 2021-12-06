import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
import cv2 as cv

if __name__ == '__main__':
    img_path = 'data/taco/images/batch_2_000090.JPG'
    img = np.array(cv.imread(img_path))
    H, W, C = img.shape
    label_path = 'data/taco/labels/batch_2_000090.txt'
    boxes = np.loadtxt(label_path, dtype=np.float).reshape(-1, 5)
    # xywh to xxyy
    # yolo格式数据集，转换成坐标形式并展示
    boxes[:, 1] = (boxes[:, 1] - boxes[:, 3] / 2) * W
    boxes[:, 2] = (boxes[:, 2] - boxes[:, 4] / 2) * H
    boxes[:, 3] *= W
    boxes[:, 4] *= H
    fig = plt.figure()
    ax = fig.subplots(1)
    for box in boxes:
        bbox = patches.Rectangle((box[1], box[2]), box[3], box[4], linewidth=2,
                                 edgecolor='r', facecolor="none")
        label = int(box[0])
        # Add the bbox to the plot
        ax.add_patch(bbox)
        # Add label
        plt.text(
            box[1],
            box[2],
            s=label,
            color="white",
            verticalalignment="top",
            bbox={"color": 'g', "pad": 0},
        )
        ax.imshow(img)
    plt.show()