"""
사진에 얼굴만 찾아 모자이크처리(opencv)
"""
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcade_eye.xml')

ff = np.fromfile(r)
