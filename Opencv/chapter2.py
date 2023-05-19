import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Ảnh xám
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0) # Làm mờ
imgCanny = cv2.Canny(img, 150, 200) # Tách cạnh
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1) # Giãn nở
imgEroded = cv2.erode(imgDialation, kernel, iterations=1) # Xói mòn

cv2.imshow("Gray image", imgGray)
cv2.imshow("Blur image", imgBlur)
cv2.imshow("Canny image", imgCanny)
cv2.imshow("Dialation image", imgDialation)
cv2.imshow("Eroded image", imgEroded)

cv2.waitKey(0)