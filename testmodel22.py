import cv2
from HandTrackingModule import HandDetector
import math
import numpy as np
Detector= HandDetector()
import joblib
import pickle
# Load the Model back from file
with open("model/SVM_Model.pkl", 'rb') as file:  
# with open("model/KNN_model.pkl", 'rb') as file:  

    load_model = pickle.load(file)
# Alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
capture= cv2.VideoCapture(0)
capture.set(3, 1080)
capture.set(4, 720)
offset = 20
Size = 300
count=1
loop=0
feature11=0
feature12=0
save=0
offset=20
while True:
    isFrame, Frame= capture.read()

    if isFrame:
        hands, img= Detector.findHands(Frame)
        # print(hands)
        if hands:
            hand1=hands[0]
            if hand1["type"]=="Right":
                x,y,w,h=hand1["bbox"]
                # print("Right Image")
                lmList=hand1["lmList"]
                lengthBase, info1=Detector.findDistance(lmList[0][:2],lmList[12][:2])
                # print(lengthBase)

                lengthThumb, infoThumb=Detector.findDistance(lmList[0][:2],lmList[4][:2])
                # print(lengthIndex)
                ratio_BT=round(lengthThumb/lengthBase,3)

                lengthIndex, infoIndex=Detector.findDistance(lmList[0][:2],lmList[8][:2])
                # print(lengthIndex)
                ratio_BI=round(lengthIndex/lengthBase,3)

                lengthRing, infoRing=Detector.findDistance(lmList[0][:2],lmList[16][:2])
                # print(lengthIndex)
                ratio_BR=round(lengthRing/lengthBase,3)

                lengthLittle, infoLittle=Detector.findDistance(lmList[0][:2],lmList[20][:2])
                # print(lengthIndex)
                ratio_BL=round(lengthLittle/lengthBase,3)

                lengthLT, infoLT=Detector.findDistance(lmList[4][:2],lmList[20][:2])
                # print(lengthIndex)
                try:
                    ratio_BLT=round(lengthLT/lengthBase,3)
                except:
                    ratio_BLT=0
                


                length4to20, infol4to20=Detector.findDistance(lmList[4][:2],lmList[20][:2])
                # print(lengthIndex)
                # ratio_4_20=length4to20/lengthBase

                length8to20, info8to20=Detector.findDistance(lmList[8][:2],lmList[20][:2])
                # print(lengthIndex)
                ratio_8_20=round(length8to20/length4to20,3)

                length12to20, info12to20=Detector.findDistance(lmList[12][:2],lmList[20][:2])
                # print(lengthIndex)
                ratio_12_20=round(length12to20/length4to20,3)

                length16to20, info16to20, =Detector.findDistance(lmList[16][:2],lmList[20][:2])
                # print(lengthIndex)
                ratio_16_20=round(length16to20/length4to20,3)

                length16to12, info16to12=Detector.findDistance(lmList[16][:2],lmList[12][:2])
                # print(lengthIndex)
                ratio_16_12=round(length16to12/length4to20,3)
                
                length8to12, info8to12,=Detector.findDistance(lmList[8][:2],lmList[12][:2])
                # print(lengthIndex)
                ratio_8_12=round(length8to12/length4to20,3)


                if Detector.fingersUp(hand1)==[0,1,0,0,0] or Detector.fingersUp(hand1)==[0,1,1,0,0] or Detector.fingersUp(hand1)==[0,1,0,0,1] or Detector.fingersUp(hand1)==[0,1,1,0,1]:
                    x9 = lmList[8][0]
                    y9 = lmList[8][1]
                    angle1= np.arctan(y9/x9)
                    if angle1 >=0.90:
                        feature11=1
                        # print("Feature 1-10",feture11,feture12)
                    else:
                        feature11=0
                        # print("Feature 1-10",feture11,feture12)
                elif Detector.fingersUp(hand1)==[0,0,0,0,1]:
                    x10 = lmList[20][0]
                    y10 = lmList[20][1]
                    angle2= np.arctan(y10/x10)
                    if angle2 >=0.90:
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

                
                total=(ratio+","+ratio1+","+ratio3)
                totalArray=np.fromstring(total, dtype=float, sep=",")
                '''
                np.fromstring('1, 2', dtype=int, sep=',')
                array([1, 2])
                '''


                prediction=load_model.predict([totalArray])
                print(prediction, end=", ")
                # score= load_model.decision_function([totalArray])
                score= load_model.predict_proba([totalArray])
                # print(score)
                maxValue=np.max(score)
                print("Max value= ",maxValue,end=",")
                max=np.argmax(score)
                print(max)
                cv2.rectangle(Frame, (x - offset, y - offset-50),
                (x - offset+90, y - offset-50+50), (255, 0, 255), cv2.FILLED)
                cv2.putText(Frame, str(prediction[0]), (x, y -26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
                cv2.rectangle(Frame, (x-offset, y-offset),
                (x + w+offset, y + h+offset), (255, 0, 255), 4)

        cv2.imshow("Capture",Frame)
        key=cv2.waitKey(1)
        if key==ord("q"):
            break
    else:
        break