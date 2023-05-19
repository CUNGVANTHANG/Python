import cv2
import numpy as np

img = cv2.imread("Resources/lambo.PNG")
print(img.shape) # (chiều cao, chiều rộng, kênh màu)

imgResize = cv2.resize(img, (1000, 500)) # (chiều rộng, chiều cao)
print(imgResize.shape) # (chiều cao, chiều rộng, kênh màu)

imgCropped = img[0:200, 200:500]
print(imgCropped.shape)

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)