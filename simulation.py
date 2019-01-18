import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture('drive.mp4')
while(cap.isOpened()):
        ret, frame = cap.read()
        orb = cv2.ORB_create()

        keypoints, descriptors = orb.detectAndCompute(frame, None)

        img = cv2.drawKeypoints(frame, keypoints, None)

        cv2.imshow('frame', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break




