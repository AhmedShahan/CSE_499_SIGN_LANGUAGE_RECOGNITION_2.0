
import os
import time
import cv2
# import torc
# h
import fnmatch

from cvzone.PoseModule import PoseDetector

file1 = open('/media/shahan/Projects/CSE499B/CSE_499_SIGN_LANGUAGE_RECOGNITION_2.0/classWiseList.txt','a')



def count_mp4_files(directory):
    # List all files in the directory
    files = os.listdir(directory)

    # Count the number of .mp4 files
    mp4_files_count = sum(1 for file in files if file.endswith(".mp4"))

    return mp4_files_count



video='able'


videoFolder=f'/media/shahan/Projects/CSE499B/archive/videos/POC_10_Class/{video}/'
detector = PoseDetector(staticMode=False,
                        modelComplexity=1,
                        smoothLandmarks=True,
                        enableSegmentation=False,
                        smoothSegmentation=True,
                        detectionCon=0.5,
                        trackCon=0.5)
cv2.namedWindow("Webcam", cv2.WINDOW_GUI_NORMAL)  # Use WINDOW_NORMAL for resizable window
cv2.resizeWindow("Webcam", 800, 600)  # Adjust the size as needed


for i in range(count_mp4_files(videoFolder)):
    classFrames=[]
    cap = cv2.VideoCapture(videoFolder+str(i)+".mp4")
    print(cap)
    while True:
        VideoFrames=[]
        ret, frame = cap.read()
        if not ret:
            break
        else:
            img = detector.findPose(frame)
            image_hight, image_width, _ = img.shape
            lmList, bboxInfo = detector.findPosition(frame, draw=True, bboxWithHands=True)
            # print("Original",lmList)
            dx, dy, dz = image_width, image_hight, 1
            translated_points = [[x * dx, y * dy, z * dz] for x, y, z in lmList]
            # print("Normalized Form:",translated_points)
            
            # onlyHandLandmarks= translated_points[13:23]
            onlyHandLandmarks= lmList[13:23]
            # print(onlyHandLandmarks)
            VideoFrames.append(onlyHandLandmarks)

            # for id,coordinate in enumerate(onlyHandLandmarks):
            #     print(id,coordinate)
            # # print("\n")
            # #Finding the positiong of landmarks
            #     cx,cy=(int(coordinate[0]),int(coordinate[1]))
            #     print(cx,cy)
            #     # if id==5:
            #     cv2.circle(frame,(cx,cy),10,color=(0,0,0),thickness=cv2.FILLED)
                # cv2.putText(frame,str(id),(cx,cy),fontFace=2,fontScale=1,color=(0,0,255),thickness=1)

            # print("Only Hand 13-22",len(onlyHandLandmarks))
            if lmList==[]:
                print("null")
                # time.sleep(5)
                continue
            # time.sleep(10)
            cv2.imshow("Webcam", frame)
            # Exit when 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        classFrames.append(VideoFrames)

# print(classFrames)
string=video+"= ["+str(classFrames)+"],"
file1.write(string)
cap.release()
cv2.destroyAllWindows()