import cv2
import numpy as np

def stackImages(scale,imgArray): 
    """
    Stacks multiple images together in a grid format, ensuring they are the same size.
    Converts grayscale images to BGR if necessary and scales them based on the given factor.
    
    Parameters:
        scale (float): Scaling factor for resizing images (e.g., 0.5 for half size, 1.0 for original size).
        imgArray (list): A list or nested list of images to stack together.
    
    Returns:
        np.array: A single image with all input images stacked together.
    """
    rows = len(imgArray)  # Number of rows in imgArray
    cols = len(imgArray[0])  # Number of columns (assuming it's a 2D list)
    rowsAvailable = isinstance(imgArray[0], list) # Check if imgArray is a nested list
    width = imgArray[0][0].shape[1] # Get reference image width
    height = imgArray[0][0].shape[0] # Get reference image height
    if rowsAvailable:
        # Loop through each image and resize it
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                    # Convert grayscale images to BGR (3-channel) for compatibility
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
                # Create a blank image to use in case of missing images
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows  # List to store horizontally stacked images
        hor_con = [imageBlank]*rows
        
         # Stack images horizontally for each row
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        # Stack all rows vertically to get final output
        ver = np.vstack(hor)
    else: 
         # If imgArray is a single list (1D), stack images horizontally only
        for x in range(0, rows): 
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
               # Convert grayscale to BGR if necessary
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)  # Stack images horizontally
        ver = hor  # No vertical stacking needed
    
    return ver  # Return the final stacked image




img = cv2.imread("Resources/img.jpg")
img2 = cv2.imread("Resources/image2.jpg")
imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
imgGray2 = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

""""
Vertical and horizontal stack issues : 
  -- we cannot resize the image -> if you want to stack more images
    if with different sizes gives you error (can't be joined)

  -- and if you joined many images , it will take up the whole space or it might 
     go out of the frame 

  -- if the images don't have the same number of channels , it will not work    
     
"""
## The Solution -> use stackImages() Function to make all the images the same 
imgHor = np.hstack((img , img))
imgVer = np.vstack((img2 , img2))

imgStack = stackImages(0.5 , ([img , img2 , imgGray, imgGray2] , [img , img , img2 , img2]))
cv2.imshow("Horizontal" , imgHor)

cv2.imshow("Vertical" , imgVer)
cv2.imshow("Image Stack" , imgStack)

cv2.waitKey(0)