import cv2 

img = cv2.imread("Resources/img.jpg")

print(img.shape) # return height , width , number of channels : BGR -> 3 ... 

#image Resize

imgResize = cv2.resize(img , (200 , 200)) # resize function(width , height)

#image cropping

imgCropped = img[0 : 200 , 200 : 400]  # cut from 0 to 200 in x-axis and from 200 to 400 in y-axis

cv2.imshow("Image" , img) 
cv2.imshow("Image Resize" , imgResize) 
cv2.imshow("Image Cropped" , imgCropped) 
cv2.waitKey(0) # wait indefinitely

