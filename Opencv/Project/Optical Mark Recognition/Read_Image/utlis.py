import cv2
import numpy as np

def stackImages(imgArray,scale,lables=[]):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
            hor_con[x] = np.concatenate(imgArray[x])
        ver = np.vstack(hor)
        ver_con = np.concatenate(hor)
    else:
        for x in range(0, rows):
            imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        hor_con= np.concatenate(imgArray)
        ver = hor
    if len(lables) != 0:
        eachImgWidth= int(ver.shape[1] / cols)
        eachImgHeight = int(ver.shape[0] / rows)
        #print(eachImgHeight)
        for d in range(0, rows):
            for c in range (0,cols):
                cv2.rectangle(ver,(c*eachImgWidth,eachImgHeight*d),(c*eachImgWidth+len(lables[d][c])*13+27,30+eachImgHeight*d),(255,255,255),cv2.FILLED)
                cv2.putText(ver,lables[d][c],(eachImgWidth*c+10,eachImgHeight*d+20),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,255),2)
    return ver

def rectContour (contours):
    rectCon = []
    for i in contours:
        area = cv2.contourArea(i) #Diện tích của mỗi đường viền
        # print("Area = ", area)
        if area > 50: # Kiểm tra diện tích > 50
            peri = cv2.arcLength(i, True) # Tính chu vi đường viền
            approx = cv2.approxPolyDP(i, 0.02*peri, True) # Đoạn mã xấp xỉ đường viền bằng cách sử dụng hàm "cv2.approxPolyDP", trả về một đa giác đơn giản hóa của hình dạng đường viền
            #print("Corner Points = ", len(approx))
            if len(approx) == 4: # Kiểm tra xem đa giác đơn giản hóa có bao gồm 4 đỉnh bằng cách sử dụng hàm len(approx)
                rectCon.append(i) # Đường viền được thêm vào danh sách "rectCon", có thể đại diện cho một hình chữ nhật
    rectCon = sorted(rectCon, key= cv2.contourArea, reverse=True)
    return rectCon

def getCornerPoints(cont):
    peri = cv2.arcLength(cont, True)  # Tính chu vi đường viền
    approx = cv2.approxPolyDP(cont, 0.02*peri, True) # Đoạn mã xấp xỉ đường viền bằng cách sử dụng hàm "cv2.approxPolyDP", trả về một đa giác đơn giản hóa của hình dạng đường viền
    return approx

def reorder(myPoints): # Sắp xếp lại các đỉnh của một tứ giác dựa trên vị trí của chúng.
    myPoints = myPoints.reshape((4,2))
    myPointsNew = np.zeros((4,1,2),np.int32)
    add = myPoints.sum(1)
    # print("myPoints: ", myPoints)
    # print("add: ", add)
    myPointsNew[0] = myPoints[np.argmin(add)] # [0, 0]
    myPointsNew[3] = myPoints[np.argmax(add)] # [w, h]
    diff = np.diff(myPoints,axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)] # [w, 0]
    myPointsNew[2] = myPoints[np.argmax(diff)] # [0, h]
    # print("diff: ", diff)

    return myPointsNew

def splitBoxes(img):
    rows = np.vsplit(img, 5) # Chia hình ảnh thành 5 hàng
    boxes = []
    for r in rows:
        cols = np.hsplit(r, 5) # Chia hình ảnh thành 5 cột
        for box in cols:
            boxes.append(box) # Thêm ô vuông vào danh sách boxes
            # cv2.imshow("Split", box)
    # cv2.imshow("Split", rows[0])
    return boxes # Trả về danh sách boxes chứa các ô vuông nhỏ

def showAnswers(img, myIndex, grading, ans, questions, choices):
    # Tính kích thước của mỗi phần của bức ảnh dành cho một câu hỏi bằng cách chia chiều rộng và chiều cao của bức ảnh cho số câu hỏi và số lựa chọn
    secW = int(img.shape[1]/questions)
    secH = int(img.shape[0]/choices)

    for x in range(0, questions):
        myAns = myIndex[x] # Tìm chỉ số lựa chọn đã chọn cho câu hỏi đó
        # Tính toán tọa độ của tâm của phần của bức ảnh dành cho câu hỏi đó
        cX = (myAns*secW) + secW//2
        cY = (x*secH) + secH//2

        if grading[x] == 1:
            myColor = (0, 255, 0) # Vẽ vòng tròn màu đỏ nếu đáp án sai
        else:
            myColor = (0, 0, 255) # Vẽ vòng tròn màu đỏ nếu đáp án đúng
            correctAns = ans[x]
            cv2.circle(img, ((correctAns*secW) + secW//2, (x*secH) + secH//2), 50, (0,255,0), cv2.FILLED)

        cv2.circle(img, (cX, cY), 50, myColor, cv2.FILLED) # Vẽ một vòng tròn tại tâm tính toán được ở trên
    return img