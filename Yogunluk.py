import cv2
import numpy as np

img = cv2.imread('tatlisu.jpg')
gamma = float(input("İstediğiniz yoğunluk değerini giriniz:"))
gamma_corrected = np.array(255 * (img / 255) ** gamma, dtype='uint8')
cv2.imshow("Yogunluk",gamma_corrected)
    # Save edited images.
    #cv2.imwrite('gamma_transformed' + str(gamma) + '.jpg', gamma_corrected)
cv2.imshow("Orjinal",img)

cv2.waitKey(0)
cv2.destroyAllWindows()