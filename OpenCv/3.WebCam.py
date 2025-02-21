import cv2


#use webCam -> laptop camera 
cap = cv2.VideoCapture(0) # 0 -> default webcam, >1 -> enter your camera id 

cap.set(3 , 640)
cap.set(4 , 480)
cap.set(10 , 100)


while True : 
    success , frame = cap.read()  # success -> Boolean value represent if it is frame or not 
                                  # frame -> the frame itself
    cv2.imshow("Video" , frame)
    if cv2.waitKey(1) & 0xFF == ord('q') :  # Finish the video
        break  