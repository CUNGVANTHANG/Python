import cv2

# Đọc/hiện thị ảnh từ đường dẫn
# img = cv2.imread("Resources/lena.png")
# cv2.imshow("Output", img)
# cv2.waitKey(0)

# -------------------------------------------------------
# Đọc/hiện thị video từ đường dẫn
# cap = cv2.VideoCapture("Resources/test_video.mp4")
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# -------------------------------------------------------
# Đọc/hiện thị webcam máy tính
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_BRIGHTNESS, 100)
while True:
    success, img = cap.read()
    cv2.imshow("Webcam", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break