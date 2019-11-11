import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('rotate.png')
# görüntü yüksekliği, genişliği
(h, w) = img.shape[:2]
#1. Rotation Tekniğiyle
# Resmin merkezini hesaplar
center = (w / 2, h / 2)
angle90 = 90
angle180 = 180
angle270 = 270
scale = 1.0
# 90 derece
M = cv2.getRotationMatrix2D(center, angle90, scale)
rotated90 = cv2.warpAffine(img, M, (h, w))

# 180 derece
M = cv2.getRotationMatrix2D(center, angle180, scale)
rotated180 = cv2.warpAffine(img, M, (w, h))

# 270 derece
M = cv2.getRotationMatrix2D(center, angle270, scale)
rotated270 = cv2.warpAffine(img, M, (h, w))

cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Image rotated by 90 degrees', rotated90)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Image rotated by 180 degrees', rotated180)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Image rotated by 270 degrees', rotated270)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 2 Translation tekniğiyle
img = cv2.imread('ronaldo.jpg',0)
rows,cols = img.shape
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 3 Affline Translation tekniğiyle
img1 = cv2.imread('ronaldo.jpg')
rows,cols,ch = img1.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv2.getAffineTransform(pts1,pts2)
dst = cv2.warpAffine(img,M,(cols,rows))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
# 4 Affline Translation tekniğiyle
img2 = cv2.imread('sudoku.png')
rows,cols,ch = img2.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img2,M,(300,300))
plt.subplot(121),plt.imshow(img2),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
# 5 Cropping Translation tekniğiyle
image = cv2.imread("tatlisu1.jpg")
cv2.imshow("original", image)
cv2.waitKey(0)
cropped = image[70:170, 440:540]
cv2.imshow("cropped", cropped)
cv2.waitKey(0)