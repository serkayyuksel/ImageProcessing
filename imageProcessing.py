import cv2
import numpy as np
from matplotlib import pyplot as plt
#goruntu okuma ( Gri tonlamalı resim yükleme)
img = cv2.imread('tatlisu.jpg',0)
#'s' tuşuna basarak görüntü kaydetme
k = cv2.waitKey(0) & 0XFF
if k == 27:  # wait for ESC key to exit
    cv2.destroyAllWindows()

elif k == ord('s'):  # wait for 's' key to save and exit
    cv2.imwrite('messigray.png', img)
    cv2.destroyAllWindows()

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

cv2.imwrite('Laplacian.png',laplacian)
cv2.imwrite('sobelx.png',sobelx)
cv2.imwrite('sobely.png',sobely)

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
#1. Filtrelenme Laplacian tekniğiyle
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
#2. Filtrelenme Sobel X tekniğiyle
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
#3. Filtrelenme Sobel Y tekniğiyle
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()
#4. Filtrelenme Blur tekniğiyle
img1 = cv2.imread('tatlisu1.jpg',0)
blur = cv2.blur(img1,(5,5))
median = cv2.medianBlur(img1,5)
blur2 = cv2.bilateralFilter(img1,9,75,75)
#5. Filtreleme Low Pass Filter Tekniğiyle
plt.subplot(141),plt.imshow(img1),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(142),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
#6. Filtrelenme medianBlur Tekniğiyle
plt.subplot(143),plt.imshow(median),plt.title('medianBlur')
plt.xticks([]), plt.yticks([])
#7. Filtrelenme Bilateral Filtering tekniğiyle
plt.subplot(144),plt.imshow(blur2),plt.title('Bilateral Filtering')
plt.xticks([]), plt.yticks([])

plt.show()

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
#8. Filtrelenme
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])

#9. Filtrelenme meanFilter Tekniğiyle
image3 = cv2.imread('me.JPG') # reads the image
image3 = cv2.cvtColor(image3, cv2.COLOR_BGR2HSV) # convert to HSV
figure_size = 9 # the dimension of the x and y axis of the kernal.
new_image = cv2.blur(image3,(figure_size, figure_size))
plt.figure(figsize=(11,6))
plt.subplot(121), plt.imshow(cv2.cvtColor(image3, cv2.COLOR_HSV2RGB)),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_HSV2RGB)),plt.title('Mean filter')
plt.xticks([]), plt.yticks([])
plt.show()
#10. Filtrelenme Gaussian Filter tekniğiyle
image4 = cv2.imread('quaresma.JPG')
new_image_gauss = cv2.GaussianBlur(image4, (figure_size, figure_size),0)
plt.figure(figsize=(11,6))
plt.subplot(121), plt.imshow(image4, cmap='gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(new_image_gauss, cmap='gray'),plt.title('Gaussian Filter')
plt.xticks([]), plt.yticks([])
plt.show()


img = cv2.imread('pout.jpg',0)

rows,cols = img.shape
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))


plt.show()