import cv2
import numpy as np 

# Upload the Model 
faceCascade = cv2.CascadeClassifier("Resources/haarcascades/haarcascade_frontalface_default.xml")
img = cv2.imread("Resources/lena.png")
#Convert To GrayScale
imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
#find faces in the image.
#detectMultiScale(imgGray , Scale Factor , Minimum Neighbors : 
#  controls how many overlapping detections are needed before the classifier confirms a region as a face.

""""
  -- Scale Factor : - This parameter controls how much the image size is reduced at each scale during the multi-scale detection process.
                    - The function works by scanning the image multiple times at different scales (sizes) to detect faces of varying sizes.

  -- If scaleFactor = 1.1 → Each image size is reduced by 10% at each step.
  -- If scaleFactor = 1.2 → Each image size is reduced by 20% at each step.

  -- Lower values (1.05 - 1.1) → Detects more faces, but slower (more computation).
  -- Higher values (1.2 - 1.5) → Faster, but might miss some smaller faces.
"""

""""
  -- minNeighbors – Controls False Positives
  -- The classifier detects multiple face-like regions, 
     and minNeighbors ensures a face is confirmed only if detected several times in overlapping regions.

   -- How It Works:
     If minNeighbors = 3 → The region must be detected at least 3 times to be considered a face.
     If minNeighbors = 5 → The region must be detected at least 5 times (more strict, reducing false positives).

   -- Choosing the Right Value:
     Lower values (1-2) → More detections but higher false positives (detects random objects as faces).
     Higher values (5-6) → Fewer false positives, but might miss some faces.

"""
faces = faceCascade.detectMultiScale(imgGray , 1.1 , 4)

for (x , y , w , h) in faces : 
    #Draws a rectangle around the face
    cv2.rectangle(img , (x , y) , (x + w , y + h) , (255 , 0 , 0) , 2)

cv2.imshow("Result", img)
cv2.waitKey(0)