import cv2
import numpy as np
import utlis

# --------------------------------------------------------------------------------------------------------------------------------------------------------- VARIABLE
path = "input1.jpg"  # Đường dẫn tới "input.jpg"
widthImg: int = 700  # Chiều dài ảnh 700px
heightImg = 700  # Chiều cao ảnh 700px
questions = 5  # 5 câu hỏi
choices = 5  # 5 lựa chọn
ans = [1, 2, 0, 1, 3]  # Đáp án

# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# PREPROCESSING
img = cv2.imread(path)  # Đọc file ảnh từ đường dẫn path
img = cv2.resize(img, (widthImg, heightImg))  # Thay đổi kích thước ảnh thành width = 700px, height = 700px
imgContours = img.copy()  # Tạo bản sao img lưu vào imgContours
imgFinal = img.copy()  # Tạo bản sao img lưu vào imgFinal
imgBiggestContours = img.copy()  # Tạo bản sao img lưu vào imgBiggestContours
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Chuyển đổi ảnh sang thang độ xám
imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)  # Ảnh xám imgGray cần được làm mờ, kenel Gaussian (5,5), độ lệch chuẩn 1
imgCanny = cv2.Canny(imgBlur, 10, 50)  # Dùng Canny để phát hiện biên cạnh của ảnh được làm mờ bằng bộ lọc Gaussian với kích thước kenel 5x5

# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# FINDING ALL CONTOURS
# Tìm viền: contours: danh sách các đường viền tìm thấy trong hình ảnh imgCanny, hierarchy: thông tin về hệ thống phân cấp của các đường viền
# cv2.RETR_EXTERNAL để chỉ tìm các đường viền ngoài cùng (bên ngoài hình ảnh)
# cv2.CHAIN_APPROX_NONE để biểu diễn các đường viền bằng tất cả các điểm trên đường viền
contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(imgContours, contours, -1, (0, 255), 10)  # Vẽ các đường viền tìm thấy lên hình ảnh imgContours

# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# FIND RECTANGLES
rectCon = utlis.rectContour(contours)  # Chuyển đổi đường viền "contours" thành hình chữ nhật có cùng diện tích
biggestContour = utlis.getCornerPoints(rectCon[0])  # Lấy ra các điểm góc của hình chữ nhật lớn nhất
# print("biggestContour: ", biggestContour)
# print(biggestContour.shape)
gradePoints = utlis.getCornerPoints(rectCon[1])  # Lấy ra các điểm góc của hình chữ nhật thứ hai
# print("gradePoints: ", gradePoints)
# print(gradePoints.shape)

if biggestContour.size != 0 and gradePoints.size != 0:  # Kiểm tra xem hai mảng đường viền biggestContour và gradePoints có kích thước khác không bằng 0
    cv2.drawContours(imgBiggestContours, biggestContour, -1, (0, 255, 0), 20)  # Vẽ các đường viền màu xanh lá, độ dày là 20
    cv2.drawContours(imgBiggestContours, gradePoints, -1, (255, 0, 0), 20)  # Vẽ các đường viền màu xanh dương, độ dày là 20

    biggestContour = utlis.reorder(biggestContour)  # Sắp xếp lại các điểm trên contour lớn nhất được tìm thấy trong ảnh
    # print("biggestContour: ", biggestContour)
    # print(biggestContour.shape)
    gradePoints = utlis.reorder(gradePoints)  # Sắp xếp lại các điểm trên contour lớn thứ hai được tìm thấy trong ảnh
    # print("gradePoints: ", gradePoints)
    # print(gradePoints.shape)

    pt1 = np.float32(biggestContour)  # Chuyển đổi sang kiểu dữ liệu float
    pt2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])  # Xác định một tập hợp 4 điểm để xác định góc nhìn đích
    matrix = cv2.getPerspectiveTransform(pt1, pt2)  # Tính ma trận biến đổi góc nhìn
    # print("matrix: ", matrix)
    imgWrapColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg))  # Biến đổi góc nhìn, hình ảnh kết quả lưu vào imgWrapColored

    pt1G = np.float32(gradePoints)  # Chuyển đổi sang kiểu dữ liệu float
    pt2G = np.float32([[0, 0], [325, 0], [0, 150], [325, 150]])  # Xác định một tập hợp 4 điểm để xác định góc nhìn đích
    matrixG = cv2.getPerspectiveTransform(pt1G, pt2G)  # Tính ma trận biến đổi góc nhìn
    # print("matrixG: ", matrix)
    imgGradeDisplay = cv2.warpPerspective(img, matrixG, (325, 150))  # Biến đổi góc nhìn, hình ảnh kết quả lưu vào imgGradeDisplay

    #cv2.imshow("Grade", imgGradeDisplay)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# APPLY THRESHOLD
imgWrapGray = cv2.cvtColor(imgWrapColored, cv2.COLOR_BGR2GRAY)  # Chuyển ảnh imgWrapColored sang ảnh xám lưu vào ảnh imgWrapGray
imgThresh = cv2.threshold(imgWrapGray, 170, 255, cv2.THRESH_BINARY_INV)[1]  # Chuyển ảnh imgWrapGray thành ảnh nhị phân với ngưỡng giá trị 170 lưu vào ảnh imgThresh
boxes = utlis.splitBoxes(imgThresh)
# cv2.imshow("Test", boxes[0])
# print(cv2.countNonZero(boxes[1]), cv2.countNonZero(boxes[2])) # Đếm số điểm ảnh khác không bằng hàm cv2.countNonZero

# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# GETTING NO ZERO PIXEL VALUES OF EACH BOX
myPixelVal = np.zeros((questions, choices))  # Tạo một mảng 2 chiều kích thước (question, choices)
countC = 0  # Đếm cột
countR = 0  # Đếm hàng
for image in boxes:
    totalPixels = cv2.countNonZero(image)  # Đếm tổng số điểm ảnh khác không lưu trữ vào totalPixel
    myPixelVal[countR][countC] = totalPixels  # Giá trị được lưu vào mảng tại vị trí [countR, countC]
    countC += 1
    if countC == choices:
        countR += 1
        countC = 0
# print("myPixelVal: ", myPixelVal)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# FINDING INDEX VALUES OF THE MARKINGS
myIndex = []
for x in range(0, questions):
    arr = myPixelVal[x]
    # print("arr", arr)
    myIndexVal = np.where(arr == np.amax(arr))
    # print("myIndexVal[0]: ",myIndexVal[0])
    myIndex.append(myIndexVal[0][0])
# print("myIndex: ", myIndex)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# GRADING
grading = []
for x in range(0, questions):
    if ans[x] == myIndex[x]:
        grading.append(1)
    else:
        grading.append(0)
# print("grading: ", grading)
score = (sum(grading) / questions) * 10
# print("score: ", score)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# DISPLAYING ANSWERS
imgResult = imgWrapColored.copy()
imgResult = utlis.showAnswers(imgResult, myIndex, grading, ans, questions, choices)
imRawDrawing = np.zeros_like(imgWrapColored)
imRawDrawing = utlis.showAnswers(imRawDrawing, myIndex, grading, ans, questions, choices)
invMatrix = cv2.getPerspectiveTransform(pt2, pt1)  # Tính ma trận biến đổi góc nhìn
# print("invMatrix: ", invMatrix)
imgInvWarp = cv2.warpPerspective(imRawDrawing, invMatrix, (widthImg, heightImg))

imgRawGrade = np.zeros_like(imgGradeDisplay)
text = str(int(score))  # Chuyển đổi sang dữ liệu int
font = cv2.FONT_HERSHEY_COMPLEX  # Font chữ
fontScale = 3  # Kích thước chữ
thinkness = 3  # Độ dày chữ
# Tính toán tọa độ của văn bản để đặt nó ở giữa ảnh
textSize, _ = cv2.getTextSize(text, font, fontScale, thinkness)
textX = int((imgRawGrade.shape[1] - textSize[0]) / 2)
textY = int((imgRawGrade.shape[0] + textSize[1]) / 2)
cv2.putText(imgRawGrade, text, (textX, textY), font, fontScale, (0, 255, 255), thinkness)
invMatrixG = cv2.getPerspectiveTransform(pt2G, pt1G)  # Tính ma trận biến đổi góc nhìn
# print("invMatrixG: ", invMatrixG)
imgInvGradeDisplay = cv2.warpPerspective(imgRawGrade, invMatrixG, (widthImg, heightImg))

imgFinal = cv2.addWeighted(imgFinal, 1, imgInvWarp, 1, 0)
imgFinal = cv2.addWeighted(imgFinal, 1, imgInvGradeDisplay, 1, 0)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# DATA STORAGE ARRAY
imgBlank = np.zeros_like(img)  # Tạo ra một mảng numpy có kích thước và kiểu dữ liệu giống với hình ảnh img, nhưng tất cả các giá trị trong mảng đều được gán bằng 0.
imageArray = ([img, imgGray, imgBlur, imgCanny],  # Tạo mảng chứa các phần tử
              [imgContours, imgBiggestContours, imgWrapColored, imgThresh],
              [imgResult, imRawDrawing, imgInvWarp, imgFinal])
lables = [["Original", "Gray", "Blur", "Canny"],  # Nhãn
          ["Contours", "Biggest Contours", "Wrap Colored", "Thresh"],
          ["Result", "Raw Drawing", "InvWarp", "Final"]]
imgStacked = utlis.stackImages(imageArray, 0.35, lables)  # Tạo ngăn xếp chồng mảng hình ảnh và tỉ lệ scale 0.35

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# EXPORT IMAGES
# cv2.imshow("Original", imgRawGrade)
cv2.imshow("Final Result", imgFinal)
cv2.imshow("Stacked Images", imgStacked)
cv2.waitKey(0)
