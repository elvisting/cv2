import numpy as np
import cv2

img = cv2.imread('field.jpg')
height, width, channels = img.shape
roi = img[int(height*0.7):height, int(width*0.1):int(width*0.9)]
cv2.imshow('ROI', roi)

gray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (11,11), 0)
edge = cv2.Canny(blur, 20, 160)
cv2.imshow('BLUR', blur)
cv2.imshow('EDGE', edge)

cnts, hierarchy = cv2.findContours(edge,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

# draw Bounding Rectangle
for c in cnts:
    (x,y,w,h) = cv2.boundingRect(c)
    print(x,y,w,h)
    cv2.rectangle(roi, (x,y), (x+w, y+h), (0,255,0), 1)

# draw Area Rectangle
#for c in cnts:
#    box = cv2.minAreaRect(c)
#    box = np.int0(cv2.boxPoints(box))
#    cv2.drawContours(roi, [box], -1, (0,255,0), 1)

cv2.imshow('contours', roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
