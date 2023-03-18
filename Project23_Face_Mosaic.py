"""
사진에 얼굴만 찾아 모자이크처리(opencv)
"""
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

ff = np.fromfile(r'/Users/chung_sungwoong/Desktop/Practice/Practice_Python/Project23_Sample_Image.jpg',np.uint8)
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
img = cv2.resize(img,dsize=(0,0), fx=1.0,fy = 1.0, interpolation=cv2.INTER_LINEAR)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.2,5)
for (x,y,w,h) in faces:
    face_img = img[y:y+h,x:x+w]
    face_img = cv2.resize(face_img,dsize = (0,0), fx = 0.05, fy=0.05)       # fx, fy 비율에 따라 모자이크 크기 변경 가능
    face_img = cv2.resize(face_img,(w,h), interpolation=cv2.INTER_AREA)
    img[y:y+h, x:x+w] = face_img
    
"""
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h,x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detecMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
"""

cv2.imshow('face find', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 앞모습은 모자이크, 옆모습은 모자이크 적용 안됨