import cv2
import numpy as np
from utils import draw_points

lk_params = dict(winSize=(15,15),maxLevel=2,criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)) 


def mark_opticalflow(previous_points, previous_gray, current_gray):
     p1, st, err = cv2.calcOpticalFlowPyrLK(previous_gray, current_gray, previous_points, None, **lk_params)
     good_new = p1[st==1]
     good_old = p0[st==1]

     return good_new



if __name__ == '__main__':
    cap = cv2.VideoCapture('videos/example.avi')
    ret, frame = cap.read()
    previous_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    p0 = np.array([[[89.2954, 387.04]], [[117.159, 392.263]], [[75.3686, 317.383]], [[89.302, 380.012]], [[115.393, 381.788]]], dtype=np.float32)
    while(True):
        ret, frame = cap.read()
        if ret is False:
            break
        current_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        new_p = mark_opticalflow(p0, previous_gray, current_gray)
        p0 = new_p.reshape(-1, 1, 2)
        previous_gray = current_gray.copy()
        cv2.imshow('frame', draw_points(frame, new_p))
        cv2.waitKey(30)


