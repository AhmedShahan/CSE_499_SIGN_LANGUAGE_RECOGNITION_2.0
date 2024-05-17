
import os
import time
import cv2
# import torch
from cvzone.PoseModule import PoseDetector

cont=0

cap = cv2.VideoCapture(0)

file1 = file1 = open('/media/shahan/Projects/CSE499B/CSE_499_SIGN_LANGUAGE_RECOGNITION_2.0/temp.txt','a')

detector = PoseDetector(staticMode=False,
                        modelComplexity=1,
                        smoothLandmarks=True,
                        enableSegmentation=False,
                        smoothSegmentation=True,
                        detectionCon=0.5,
                        trackCon=0.5)
cv2.namedWindow("Webcam", cv2.WINDOW_GUI_NORMAL)  # Use WINDOW_NORMAL for resizable window
cv2.resizeWindow("Webcam", 800, 600)  # Adjust the size as needed

# Set the initial window size
i=0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    else:
        img = detector.findPose(frame)
        image_hight, image_width, _ = img.shape
        lmList, bboxInfo = detector.findPosition(frame, draw=True, bboxWithHands=True)
        print("Original",lmList)
        dx, dy, dz = image_width, image_hight, 1
        translated_points = [[x * dx, y * dy, z * dz] for x, y, z in lmList]

        print("Normalized Form:",translated_points)
        landmarkList=[]
        if lmList==[]:
            print("null")
            # time.sleep(5)
            continue
        # time.sleep(10)
        cv2.imshow("Webcam", frame)
        # Exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()