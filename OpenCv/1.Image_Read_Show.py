import cv2
#Read Image
img = cv2.imread('Resources/img.jpg' , 1)
#Show Image
cv2.imshow("Beautiful cat" , img)
# 0 -> infinite delay (time that photo is open)
cv2.waitKey(0)



