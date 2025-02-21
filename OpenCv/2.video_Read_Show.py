import cv2


#Read Video
cap = cv2.VideoCapture('Resources/vid.mp4') 

#loop over video frames to be appeared

while True : 
    success , frame = cap.read()  # success -> Boolean value represent if it is frame or not 
                                  # frame -> the frame itself
    cv2.imshow("Video" , frame)
    if cv2.waitKey(1) & 0xFF == ord('q') :  # Finish the video
        break  