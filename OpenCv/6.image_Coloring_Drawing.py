import cv2 
import numpy as np 

# img = np.zeros((512 , 512)) # zeroes -> BLACK image 
img = np.zeros((512 , 512 , 3) , np.uint8) #has 3 channels 


#color Whole image with blue
# img[:] = 255 , 0 , 0 
#color part of image 
img[100 : 200 , 300 : 400] = 255 , 0 , 0

cv2.imshow("Blue Image",img) 
print(img)



# Line Drawing

#line(image , start Point , End Point , color , Thickness)
cv2.line(img , (0 , 0) , (img.shape[1] , img.shape[0]) , (0 , 255 , 0) , 3) 

cv2.imshow("Line",img) 


# Rectangle Drawing

#rectangle(image , start point of diagonal , end point of diagonal , color , Thickness)
cv2.rectangle(img , (0 , 0) , (250 , 350) , (0 , 0 , 255) , cv2.FILLED)
cv2.imshow("Rectangle",img) 

#Circle Drawing 
# circle(image , center , r , color , thickness)
cv2.circle(img , (400 , 50) , 30 , (255 , 140 , 66) , 5)
cv2.imshow("Circle",img) 

#write a text 
#putText(image , text , start ,Font , scale , color , Thickness)
cv2.putText(img , "Fatma Ibrahim" , (300 , 200) , cv2.FONT_HERSHEY_DUPLEX , 1 , 3)
cv2.imshow("Text",img) 
cv2.waitKey(0)