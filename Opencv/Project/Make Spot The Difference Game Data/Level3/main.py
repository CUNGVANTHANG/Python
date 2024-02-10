from skimage.metrics import structural_similarity
import cv2
import numpy as np
import random
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

# Đọc file Image_input
root = Tk()
root.withdraw()
file_path = askopenfilename(filetypes=[("Image_input", ".jpg;.jpeg;*.png")])

# Kiểm tra
if file_path:
    # Đọc ảnh từ đường dẫn được chọn
    img_origin = cv2.imread(file_path)
    img = img_origin.copy()

    # Chuyển đổi sang ảnh xám
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Bộ lọc canny để phát hiện cạnh
    edges = cv2.Canny(img, 50, 130)

    # Chuyển đổi ảnh sang ảnh nhị phân
    thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]

    # Áp dụng hàm tìm contour để tìm các đối tượng trong ảnh
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Lưu các contour có diện tích lớn hơn 100 vào danh sách objects
    objects = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100 and area < 700:
            objects.append(contour)

    # Nếu không tìm thấy đối tượng nào có diện tích lớn hơn 100, thoát khỏi chương trình
    if not objects:
        exit()

    # Lặp lại 3 lần để chọn và thay đổi màu cho 3 đối tượng
    for i in range(3):
        # Chọn ngẫu nhiên một đối tượng từ danh sách objects
        selected_contour = random.choice(objects)

        # Tìm vị trí ngẫu nhiên trong ảnh mà không giao với bất kỳ cạnh nào
        rows, cols = img.shape[:2]
        mask = np.zeros((rows, cols), dtype=np.uint8)
        cv2.drawContours(mask, [selected_contour], -1, 255, -1)
        rand_x, rand_y = None, None
        while rand_x is None or mask[rand_x, rand_y] == 255:
            rand_x = np.random.randint(0, rows)
            rand_y = np.random.randint(0, cols)

        # Copy đối tượng được chọn đến vị trí ngẫu nhiên tìm được
        mask = np.zeros((rows, cols), dtype=np.uint8)
        cv2.drawContours(mask, [selected_contour], -1, 255, -1)
        x, y, w, h = cv2.boundingRect(selected_contour)
        roi = img[y:y + h, x:x + w]
        mask_roi = mask[y:y + h, x:x + w]
        masked_img = cv2.bitwise_and(roi, roi, mask=mask_roi)
        new_x = rand_x - w // 2
        new_y = rand_y - h // 2
        for i in range(new_x, new_x + masked_img.shape[0]):
            for j in range(new_y, new_y + masked_img.shape[1]):
                if i >= 0 and i < rows and j >= 0 and j < cols and mask_roi[i - new_x, j - new_y] != 0:
                    img[i, j] = masked_img[i - new_x, j - new_y]

    # Xuất hình ảnh
    # Lấy tên file và đường dẫn đến thư mục chứa file
    file_name = os.path.basename(file_path)
    file_dir = os.path.dirname(file_path)

    # Tạo tên file output: "image_imput_output_level2.png"
    file_name_out = file_name.split(".")[0] + "_output_level2.png"

    # Tạo đường dẫn để lưa file
    file_path_out = os.path.join(file_dir, file_name_out)

    # Lưu ảnh đầu ra
    cv2.imwrite(file_path_out, img)

    # Đọc ảnh before và ảnh after
    before = cv2.imread(file_path)
    after = cv2.imread(file_name_out)

    # Chuyển đổi hình ảnh sang thang độ xám
    before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
    after_gray = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)

    # Tính toán SSIM giữa hai hình ảnh
    (score, diff) = structural_similarity(before_gray, after_gray, full=True)
    print("Image similarity", score)

    # Hình ảnh khác biệt chứa sự khác biệt hình ảnh thực tế giữa hai hình ảnh
    # và được biểu diễn dưới dạng kiểu dữ liệu dấu phẩy động trong phạm vi [0,1]
    # vì vậy ta phải chuyển đổi mảng thành số nguyên không dấu 8 bit trong phạm vi
    # [0,255] trước khi ta có thể sử dụng nó với OpenCV
    diff = (diff * 255).astype("uint8")

    # Ngưỡng hình ảnh khác biệt, tiếp theo là tìm đường viền để
    # có được các vùng của hai hình ảnh đầu vào khác nhau
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]

    # Vẽ hình chữ nhật bao quanh vùng khác biệt
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

