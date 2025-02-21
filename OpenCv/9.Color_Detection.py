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


def empty(a):
    pass


path = 'Resources/lambo.png'
# Create a window named "TrackBars" to display the trackbars
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)  # Resize the window to a suitable size for the trackbars

# Create trackbars to adjust the HSV range dynamically
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)  # Trackbar to control minimum Hue value (0 to 179)
cv2.createTrackbar("Hue Max","TrackBars",19,179,empty)  # Trackbar to control maximum Hue value (0 to 179)
cv2.createTrackbar("Sat Min","TrackBars",110,255,empty)  # Trackbar to control minimum Saturation value (0 to 255)
cv2.createTrackbar("Sat Max","TrackBars",240,255,empty)  # Trackbar to control maximum Saturation value (0 to 255)
cv2.createTrackbar("Val Min","TrackBars",153,255,empty)  # Trackbar to control minimum Value (brightness) (0 to 255)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)  # Trackbar to control maximum Value (brightness) (0 to 255)

# Start an infinite loop to keep the trackbars and image processing running
while True:
    # Read the image from the specified path
    img = cv2.imread(path)
    # Convert the image from BGR to HSV color space
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    # Get the current values of the trackbars for Hue, Saturation, and Value
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")  # Minimum Hue value
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")  # Maximum Hue value
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")  # Minimum Saturation value
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")  # Maximum Saturation value
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")  # Minimum Value (brightness) value
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")  # Maximum Value (brightness) value

    # Print the current values of the trackbars to the console for debugging
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    # Create the lower and upper bounds for the HSV range based on trackbar values
    lower = np.array([h_min, s_min, v_min])  # Lower bound of HSV range
    upper = np.array([h_max, s_max, v_max])  # Upper bound of HSV range

    # Create a mask that isolates the pixels within the specified HSV range
    mask = cv2.inRange(imgHSV, lower, upper)

    # Apply the mask to the original image using a bitwise AND operation to extract the color
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    # Optionally, display the images (commented out for now)
    # cv2.imshow("Original", img)  # Show the original image
    # cv2.imshow("HSV", imgHSV)  # Show the image in HSV color space
    # cv2.imshow("Mask", mask)  # Show the mask created from the HSV range
    # cv2.imshow("Result", imgResult)  # Show the result after applying the mask

    # Stack the images (original, HSV, mask, and result) into one window for better visualization
    imgStack = stackImages(0.6, ([img, imgHSV], [mask, imgResult]))
    cv2.imshow("Stacked Images", imgStack)  # Display the stacked images

    # Wait for 1 millisecond before continuing to the next frame (useful for real-time updates)
    cv2.waitKey(1)
