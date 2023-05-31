from skimage.metrics import structural_similarity
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
from PIL import Image
import os

# Đọc file Image_input
root = Tk()
root.withdraw()
file_path = askopenfilename(filetypes=[("Image_input", ".jpg;.jpeg;*.png")])

# Kiểm tra
if file_path:
    # Đọc ảnh từ đường dẫn
    img_origin = cv2.imread(file_path)
    img = img_origin.copy()

    #Tạo 3 hình chữ nhật random từng vị trí
    num_rectangles = 3
    for i in range(num_rectangles):
        # chọn vị trí vẽ hình chữ nhật
        height, width = img.shape[:2]
        w = np.random.randint(16, width // 8)
        h = np.random.randint(16, height // 8)
        x = np.random.randint(w // 8, width - w // 8)
        y = np.random.randint(h // 8, height - h // 8)
        # Chọn màu hình chữ nhật bằng cách lấy màu trung bình quanh vị trí
        roi = img[y - h // 2:y + h // 2, x - w // 2:x + w // 2]
        avg_color = np.mean(roi, axis=(0, 1))
        # Cộng thêm màu đề tránh trường hợp vẽ trùng với màu nền
        background_color = [0, 0, 0]  # Giả sử màu nền là đen
        threshold = 30  # Khoảng ngưỡng để xác định sự khác biệt giữa màu trung bình và màu nền
        if np.sum(np.abs(avg_color - background_color)) > threshold:
            color = avg_color + [20, 20, 20]
        else:
            color = [255, 255, 255]  # Nếu màu trung bình không khác biệt đủ, sử dụng màu trắng thay thế
        # Vẽ hình chữ nhật
        cv2.rectangle(img, (x - w//8, y - h//8), (x + w//8, y + h//8), color, -1)
        x = np.clip(x, w // 8, width - w // 8)
        y = np.clip(y, h // 8, height - h // 8)

    # Xuất hình ảnh
    # Lấy tên file và đường dẫn đến thư mục chứa file
    file_name = os.path.basename(file_path)
    file_dir = os.path.dirname(file_path)

    # Tạo tên file output: "image_imput_output_level1.png"
    file_name_out = file_name.split(".")[0] + "_output_level1.png"

    # Tạo đường dẫn để lưa file
    file_path_out = os.path.join(file_dir, file_name_out)

    # Lưu ảnh đầu ra
    cv2.imwrite(file_path_out, img)

    #Đọc ảnh before và ảnh after
    before = cv2.imread(file_path)
    after = cv2.imread(file_name_out)

    #Chuyển đổi hình ảnh sang thang độ xám
    before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
    after_gray = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)

    #Tính toán SSIM giữa hai hình ảnh
    (score, diff) = structural_similarity(before_gray, after_gray, full=True)
    print("Image similarity", score)

    #Hình ảnh khác biệt chứa sự khác biệt hình ảnh thực tế giữa hai hình ảnh
    #và được biểu diễn dưới dạng kiểu dữ liệu dấu phẩy động trong phạm vi [0,1]
    #vì vậy ta phải chuyển đổi mảng thành số nguyên không dấu 8 bit trong phạm vi
    #[0,255] trước khi ta có thể sử dụng nó với OpenCV
    diff = (diff * 255).astype("uint8")

    #Ngưỡng hình ảnh khác biệt, tiếp theo là tìm đường viền để
    #có được các vùng của hai hình ảnh đầu vào khác nhau
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]

    #Vẽ hình chữ nhật bao quanh vùng khác biệt
    for c in contours:
        area = cv2.contourArea(c)
        if area > 40:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(before, (x, y), (x + w, y + h), (36, 255, 12), 2)
            cv2.rectangle(after, (x, y), (x + w, y + h), (36, 255, 12), 2)

    # Hiển thị hình ảnh
    result1 = np.hstack((img_origin, img))
    cv2.imshow("Task1", result1)
    result2 = np.hstack((before, after))
    cv2.imshow("Task2", result2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

