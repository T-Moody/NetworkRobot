import cv2
import numpy as np
import utils

def getLaneCurve(img):
    imgThres = utils.thresholding(img)

    cv2.imshow('Thres', imgThres)
    return None

if __name__ == '__main__':
    cap = cv2.VideoCapture('vid6.mp4')
    while True:
        success, img = cap.read()
        img = cv2.resize(img, (480, 240))

        getLaneCurve(img)
        cv2.imshow('Vid', img)
        cv2.waitKey(1)
