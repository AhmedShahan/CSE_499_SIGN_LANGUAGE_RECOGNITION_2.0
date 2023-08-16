import cv2
from HandTrackingModule import HandDetector
import math
import numpy as np
# import prerocessing as NBMODEL
Detector= HandDetector()
import joblib

capture= cv2.VideoCapture(0, cv2.CAP_DSHOW)
capture.set(3, 1080)
capture.set(4, 720)
offset = 20
imgSize = 300
file = open('demoDatasetCollect.csv', 'a')

feature11=0
feature12=0
save=0
while True:
    isFrame, Frame= capture.read()

    if isFrame:
        hands, img= Detector.findHands(Frame)
        # print(hands)
        if hands:
            hand1=hands[0]
            if hand1["type"]=="Right":
                # print("Right Image")
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


                if Detector.fingersUp(hand1)==[0,1,0,0,0] or Detector.fingersUp(hand1)==[0,1,1,0,0] or Detector.fingersUp(hand1)==[0,1,0,0,1] or Detector.fingersUp(hand1)==[0,1,1,0,1]:
                    x9 = lmList[8][0]
                    y9 = lmList[8][1]
                    angle1= np.arctan(y9/x9)
                    if angle1 >=0.80:
                        feature11=1
                        # print("Feature 1-10",feture11,feture12)
                    else:
                        feature11=0
                        # print("Feature 1-10",feture11,feture12)
                elif Detector.fingersUp(hand1)==[0,0,0,0,1]:
                    x10 = lmList[20][0]
                    y10 = lmList[20][1]
                    angle2= np.arctan(y10/x10)
                    if angle2 >=0.80:
                        feature12=1
                        # print("Feature 1-10",feature11,feature11)
                    else:
                        feature12=0
                        # print("Feature 1-10",feature11,feature11)
                else:
                    feature11=0
                    feature12=0
                    # print("Feature 1-10")

                    # print("Feature 12")

                # ratio=[ratio_BT,ratio_BI,ratio_BR,ratio_BL]
                ratio=str(ratio_BT)+','+ str(ratio_BI)+','+str(ratio_BR)+','+str(ratio_BL)+','+str(ratio_BLT)
                ratio1=str(ratio_8_20)+','+str(ratio_12_20)+','+str(ratio_16_20)+','+str(ratio_16_12)+','+str(ratio_8_12)
                ratio3= str(feature11)+','+str(feature12)
                # print("Feature 1-5: ",ratio)
                # print("Feature 6-10: ",ratio1)
                # print("Feature 11,12: ",ratio3)/
                
                total=(ratio+","+ratio1+","+ratio3)
                if count==101:
                    file.write("\n")
                    cv2.putText(Frame, "Thank You!!",(400,100),fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=7, color=(255,0,255), thickness=5)
                    save=0
                    count=0
                else: 
                    if save==1:
                        print(count)
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
        cv2.imshow("Capture",Frame)

        key=cv2.waitKey(1)
        if key==ord("q"):
            break
        elif key== ord("s"):
            save=1
    else:
        break