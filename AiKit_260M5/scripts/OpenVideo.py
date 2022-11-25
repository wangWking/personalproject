


# cap  = cv2.VideoCapture(1)

# while cv2.waitKey(1)<0:
#     ret, frame = cap.read()
#     if not ret:
#         break
#     cv2.imshow('', frame)
import cv2
import numpy as np

# 读取图片并缩放方便显示
img = cv2.imread('../color.png')
height, width = img.shape[:2]
size = (int(width * 0.5), int(height * 0.5))
# 缩放
img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
gs_img = cv2.GaussianBlur(img, (5, 5), 2) # 高斯模糊
# 转换为灰度图片
gray = cv2.cvtColor(gs_img,cv2.COLOR_BGR2GRAY)

 # a etching operation on a picture to remove edge roughness
erosion = cv2.erode(gray, np.ones((1, 1), np.uint8), iterations=2)

# the image for expansion operation, its role is to deepen the color depth in the picture
dilation = cv2.dilate(erosion, np.ones(
    (1, 1), np.uint8), iterations=2)


# 将灰度图img2gray中灰度值小于175的点置0，灰度值大于175的点置255
_, threshold = cv2.threshold(dilation, 175, 255, cv2.THRESH_BINARY)
# 边缘检测
# 最小阈值100，最大阈值200
edges = cv2.Canny(threshold,100,200,)
# edges = cv2.Canny(threshold)
# 检测物体边框
contours,_ = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow('src', img)
cv2.imshow('gs', gs_img)
cv2.imshow('gray',gray)
cv2.imshow('eros', erosion)
cv2.imshow('dila', dilation)
cv2.imshow('Canny',edges)

if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()
    
# cv2.waitKey(0)
# cv2.waitKey(0)
 
        
     
        
# # 获取鼠标所点击的位置信息
# def getposBgr(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print("Bgr is", img[y, x])
# cv2.imshow('image', img)
# # cv2.setMouseCallback("image", getposBgr)
# cv2.imshow("gray",gray)
# cv2.imshow("edge",edges)
# cv2.waitKey(0)