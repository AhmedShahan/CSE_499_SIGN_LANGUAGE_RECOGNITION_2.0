# Import Section
import cv2
import numpy as np
import time 
from HandTrackingModule import HandDetector
Detector= HandDetector(maxHands=2)

# Alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# Default values for 
count=1
loop=0
save1 =0
save2 =0
# alphabetCount=0
file = open('Dataset/shahan.csv','a')


# Open the webcam
cap = cv2.VideoCapture(0)

# Create a named window
cv2.namedWindow("Webcam", cv2.WINDOW_KEEPRATIO)  # Use WINDOW_NORMAL for resizable window

# Set the initial window size
cv2.resizeWindow("Webcam", 1080, 720)  # Adjust the size as needed

def Features_Extraction(lmList):
    lmList=hand1["lmList"]
    lengthBase, info1, img1=Detector.findDistance(lmList[0][:2],lmList[12][:2],img)
    # print(lengthBase)

    lengthThumb, infoThumb, imgThumb=Detector.findDistance(lmList[0][:2],lmList[4][:2],img)
    # print(lengthIndex)
    ratio_BT=round(lengthThumb/lengthBase,3)

    lengthIndex, infoIndex, imgIndex=Detector.findDistance(lmList[0][:2],lmList[8][:2],img)
    # print(lengthIndex)
    ratio_BI=round(lengthIndex/lengthBase,3)

    lengthRing, infoRing, imgRing=Detector.findDistance(lmList[0][:2],lmList[16][:2],img)
    # print(lengthIndex)
    ratio_BR=round(lengthRing/lengthBase,3)

    lengthLittle, infoLittle, imgLittle=Detector.findDistance(lmList[0][:2],lmList[20][:2],img)
    # print(lengthIndex)
    ratio_BL=round(lengthLittle/lengthBase,3)

    lengthLT, infoLT, imgLT=Detector.findDistance(lmList[4][:2],lmList[20][:2],img)
    # print(lengthIndex)
    try:
        ratio_BLT=round(lengthLT/lengthBase,3)
    except:
        ratio_BLT=0
    


    length4to20, infol4to20, imgl4to20=Detector.findDistance(lmList[4][:2],lmList[20][:2],img)
    # print(lengthIndex)
    # ratio_4_20=length4to20/lengthBase

    length8to20, info8to20, img8to20=Detector.findDistance(lmList[8][:2],lmList[20][:2],img)
    # print(lengthIndex)
    ratio_8_20=round(length8to20/length4to20,3)

    length12to20, info12to20, img12to20=Detector.findDistance(lmList[12][:2],lmList[20][:2],img)
    # print(lengthIndex)
    ratio_12_20=round(length12to20/length4to20,3)

    length16to20, info16to20, img16to20=Detector.findDistance(lmList[16][:2],lmList[20][:2],img)
    # print(lengthIndex)
    ratio_16_20=round(length16to20/length4to20,3)

    length16to12, info16to12, img16to12=Detector.findDistance(lmList[16][:2],lmList[12][:2],img)
    # print(lengthIndex)
    ratio_16_12=round(length16to12/length4to20,3)
    
    length8to12, info8to12, img8to12=Detector.findDistance(lmList[8][:2],lmList[12][:2],img)
    # print(lengthIndex)
    ratio_8_12=round(length8to12/length4to20,3)
    ratio=str(ratio_BT)+','+ str(ratio_BI)+','+str(ratio_BR)+','+str(ratio_BL)+','+str(ratio_BLT)
    ratio1=str(ratio_8_20)+','+str(ratio_12_20)+','+str(ratio_16_20)+','+str(ratio_16_12)+','+str(ratio_8_12)
    total=(ratio+","+ratio1)
    return total

    
    

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    else:
        hands, img= Detector.findHands(frame)
        # print(hands)
        if hands:
            # print(hands)
            hand1=hands[0]
            lmList1=hand1['lmList']
            leftFeatures=Features_Extraction(lmList1)
            # print(hand1['type'], end=',')
            
            if len(hands)==2:
                hand2=hands[1]
                lmList2=hand2['lmList']
                
                rightFeatures=Features_Extraction(lmList2)
                length2Hand, info2Hand, img2Hand=Detector.findDistance(lmList1[4][:2],lmList2[4][:2],img)
                # print(hand2['type'])
            
            # if Detector.fingersUp(hand1)==[0,1,0,0,0] or Detector.fingersUp(hand1)==[0,1,1,0,0] or Detector.fingersUp(hand1)==[0,1,0,0,1] or Detector.fingersUp(hand1)==[0,1,1,0,1]:
            #     x9 = lmList[8][0]
            #     y9 = lmList[8][1]
            #     angle1= np.arctan(y9/x9)
            #     if angle1 >=0.80:
            #         feature11=1
            #         # print("Feature 1-10",feture11,feture12)
            #     else:
            #         feature11=0
            #         # print("Feature 1-10",feture11,feture12)
            # elif Detector.fingersUp(hand1)==[0,0,0,0,1]:
            #     x10 = lmList[20][0]
            #     y10 = lmList[20][1]
            #     angle2= np.arctan(y10/x10)
            #     if angle2 >=0.80:
            #         feature12=1
            #         # print("Feature 1-10",feature11,feature11)
            #     else:
            #         feature12=0
            #         # print("Feature 1-10",feature11,feature11)
            # else:
            #     feature11=0
            #     feature12=0
            #     # print("Feature 1-10")

            #     # print("Feature 12")

            # ratio=[ratio_BT,ratio_BI,ratio_BR,ratio_BL]
            
            # ratio3= str(feature11)+','+str(feature12)
            # print("Feature 1-5: ",ratio)
            # print("Feature 6-10: ",ratio1)
            # print("Feature 11,12: ",ratio3)/
            
            # total=(ratio+","+ratio1+","+ratio3)
                total=leftFeatures+','+rightFeatures+','+str(round(length2Hand,3))
            
            if count==21:
                file.write("\n")
                # cv2.putText(frame, "Thank You!!",(400,100),fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=7, color=(255,0,255), thickness=5)
                # time.sleep()
                save1=0
                count=0
            else: 
                if save1==1:
                    print(count)
                    # time.sleep(2)
                    cv2.putText(frame, f"Data Stored Number:{str(count)}",(20,100),fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3, color=(255,0,255), thickness=5)
                    
                    # angle= str(done1)+ str(done2)
                    file.write(total)
                    file.write("\n")
                    count+=1
            # totalinarray=np.fromstring(total, dtype=int, sep=',')
            
            # print(result)
            # print(count,ratio1)

            # if  0xFF==ord("s"):

            # file.close()
            # lengthThumb, infoThumb, imgThumb=Detector.findDistance(lmList[0][:2],lmList[4][:2],img)
            # print(lengthThumb)

            # print(lmList[8],lmList[4])
            
            # print(length1)
            # print(lmList[8][2])
            # print(lmList[8])
            # print(lmList[4])
            # d = math.hypot(lmList[8][0] - lmList[4][0],lmList[8][1] - lmList[4][1],lmList[8][2] - lmList[4][2])
            # print("my founded",d)
            # print("From founded",length1)
            # print(lmList)
            # for id, coordinate in enumerate(lmList):
                # print(id, coordinate[:2],end=" ")
            # print("\n")
    cv2.imshow("Webcam", frame)
    
    # Exit when 'q' is pressed
    key=cv2.waitKey(1)
    if key==ord("s"):
        # print(count,ratio1)
        # count+=1
        # total= ratio+ ","+ ratio1
        # # total= round(ratio,3)+ ","+ round(ratio1,3)
        # file.write(total)
        # file.write("\n")
        save1 =1
    elif key==ord("q"):
        break
    # if cv2.waitKey(1) & 0xFF == ord('q'):
        # break
    # elif 

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()
