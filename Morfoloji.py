import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('j.png',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
plt.subplot(331),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
#1. Erozyon tekniğiyle morfoloji
plt.subplot(332),plt.imshow(erosion),plt.title('Erozyon')
plt.xticks([]), plt.yticks([])
#2. Dilastasyon tekniğiyle morfoloji
dilation = cv2.dilate(img,kernel,iterations = 1)
plt.subplot(333),plt.imshow(dilation),plt.title('Dilatasyon')
plt.xticks([]), plt.yticks([])
#3. Acilis tekniğiyle morfoloji
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
plt.subplot(334),plt.imshow(opening),plt.title('Açılış')
plt.xticks([]), plt.yticks([])
#4. Kapanis tekniğiyle morfoloji
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
plt.subplot(335),plt.imshow(closing),plt.title('Kapanış')
plt.xticks([]), plt.yticks([])
#5. Morfolojik Gradyan tekniğiyle morfoloji
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.subplot(336),plt.imshow(gradient),plt.title('Morfoloji Gradyan')
plt.xticks([]), plt.yticks([])
#6. Tophat tekniğiyle morfoloji
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
plt.subplot(337),plt.imshow(tophat),plt.title('Üst Şapka')
plt.xticks([]), plt.yticks([])
#7. Blackhat tekniğiyle morfoloji
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
plt.subplot(338),plt.imshow(blackhat),plt.title('Kara Şapka')
plt.xticks([]), plt.yticks([])
#8. Hitmiss tekniğiyle morfoloji
HITMISS = cv2.morphologyEx(img, cv2.MORPH_HITMISS, kernel)
plt.subplot(339),plt.imshow(HITMISS),plt.title('Kare')
plt.xticks([]), plt.yticks([])
plt.show()
DILATE = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel)
plt.subplot(131),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
#9. DILATE tekniğiyle morfoloji
plt.subplot(132),plt.imshow(DILATE),plt.title('Genişletilmiş')
plt.xticks([]), plt.yticks([])
#10. CROSS tekniğiyle morfoloji
cv2.MORPH_CROSS
CROSS = cv2.morphologyEx(img, cv2.MORPH_CROSS, kernel)
plt.subplot(133),plt.imshow(CROSS),plt.title('Çaprazlama')
plt.xticks([]), plt.yticks([])

plt.show()