import cv2 
import numpy as np 


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def getContours(img) : 
  contours , hierarchy = cv2.findContours(img , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE) 
  for cnt in contours : 
    area = cv2.contourArea(cnt) 
    print(area) 
    cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
    #  True : Means the contour is closed (if False, it assumes an open shape).
    """"
    Why we need perimeter : 
      -- The perimeter helps in approximation of shapes.
      -- Used in the next step to simplify contour points.
       """
    perimeter = cv2.arcLength(cnt , True)
    """ 
     -- Approximates the shape by reducing the number of contour points.
     -- epsilon :
        - 0.01 >> Keeps most details (high accuracy) <For example, a star shape will keep all its sharp edges.>
        - 0.02 >> Balanced simplification <Example: A rectangle with rough edges may become a smooth rectangle.> 
        - 0.05 >> Very simplified shape (loses small details)<Example: A star shape might turn into a pentagon!>
    """
     # This Function >>  - Converts a detailed contour into a simplified polygon.   
     #                   - Helps classify shapes based on the number of corners.
    approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)  
    print(len(approx))# Print number of Corners of object 
    objCor = len(approx) 

    #A bounding box >> is a rectangular box that surrounds a detected shape. 
    # It is commonly used in object detection to define the position and size of an object in an image.
    x, y, w, h = cv2.boundingRect(approx) 
    # (x , y) >> Top_Left Corner of bounding box 
    # (w , h) >> Width , height of bounding box
    
    if objCor == 3 : 
      ObjType = "Triangle" 
    elif objCor == 4 : 
      aspRatio = w / float(h)
      if aspRatio >= 0.98 and aspRatio <= 1.03 : 
        ObjType = "Square" 
      else : 
        ObjType = "Rectangle"
    else : 
      ObjType = "Circle"

    # Drawing a Bounding box
    cv2.rectangle(imgContour , (x , y) , (x + w , y + h) ,( 0 , 255 , 0) , 3)

    # put text (type of object)
    cv2.putText(imgContour, ObjType, 
            (x + (w // 2) - 10, y + (h // 2) - 10), 
            cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2)

path = "Resources/shapes.png" 
img = cv2.imread(path)
imgContour = img.copy() ; 

imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray , (7 , 7) , 1)
imgCanny = cv2.Canny(imgBlur , 50 , 50) 

getContours(imgCanny)

imgBlank = np.zeros_like(img)
imgStack = stackImages(0.8,([img,imgGray,imgBlur],
                            [imgCanny,imgContour,imgBlank]))

cv2.imshow("Stack", imgStack)

cv2.waitKey(0)