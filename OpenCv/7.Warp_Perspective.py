import cv2
import numpy as np  

# Load the image
img = cv2.imread("Resources/img2.jpg")

# Define the width and height of the output image
width, height = 200, 300  

# Define the four points from the original image that will be transformed
# These points should be selected based on the area you want to warp
pts1 = np.float32([[62, 63], [727, 273], [13, 682], [716, 856]])  

# Define the corresponding points in the output image (rectangle)
# These points map the selected area to a new perspective
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# Compute the transformation matrix for perspective warping
matrix = cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)

# Apply the perspective transformation to get the desired output
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

# Display the original image
cv2.imshow("Image", img)

# Display the transformed output image
cv2.imshow("Output", imgOutput)

# Wait indefinitely for a key press before closing the windows
cv2.waitKey(0)
cv2.destroyAllWindows()  # Close all windows after key press
