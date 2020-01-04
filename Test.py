import numpy as np
import cv2
import matplotlib.pyplot as plt
m=3
def get_M_Minv():

    n=1
    x =400
    y =480
    src = np.float32([[(444,520),(546,520),(423,609),(585,604)]])
    dst = np.float32([[((25/n+x),25/n+y),(125/n+x,0+y),(25/n+x,150/n+y),(125/n+x,150/n+y)]])
    #dst= np.float32([[(444,520),(546,520),(423,609),(585,604)]])
    M = cv2.getPerspectiveTransform(src,dst)
    Minv = cv2.getPerspectiveTransform(dst,src)

    return M,Minv
image=cv2.imread("D:\code\python\\fisheye\hou\\4.png")
#plt.imshow(image)
#plt.show()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, corners = cv2.findChessboardCorners(gray,(5,6), cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_NORMALIZE_IMAGE)
#print(corners)
M, Minv = get_M_Minv()
src_image1=cv2.imread("D:\code\python\\fisheye\hou\\4.png")
dst_image1=cv2.imread("unfisheyeImage.png")
trans_image1 = cv2.warpPerspective(dst_image1,M,dst_image1.shape[1::-1],flags=cv2.INTER_LINEAR )
src_image2=cv2.imread("hou1.png")
dst_image2=cv2.imread("hou.png")
trans_image2 = cv2.warpPerspective(dst_image2,M,dst_image2.shape[1::-1],flags=cv2.INTER_LINEAR )
cv2.imshow("1",trans_image1)
cv2.imshow("2",trans_image2)
cv2.waitKey(0)
