import cv2
import os
import numpy as np


R = 5
COLORS = np.random.randint(0, 255, (100, 3))


def draw_points(img, points):
    for i, point in enumerate(points):
        cv2.circle(img, (point[0], point[1]), R, COLORS[i].tolist(), -1)
    return img

def get_videowriter(file_name):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    vw = (file_name, fourcc, 15.0, (360, 640))

def create_dir(dir_name):
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
 
def clear_dir(dir_name):
    os.system('rm -rf %s/*' % dir_name)

def del_dir(dir_name):
    if os.path.isdir(dir_name):
        os.system('rm -rf %s' % dir_name)

if __name__ == '__main__':
    cap = cv2.VideoCapture('videos/example.avi')
    points = [(0, 10), (50, 50), (100, 100)]
    while(True):
        _, frame = cap.read()
        if _ is False:
            break
        cv2.imshow('frame', draw_points(frame, points))
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
