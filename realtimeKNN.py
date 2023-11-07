# Import Section
import cv2
import numpy as np
import time 
from HandTrackingModule import HandDetector
Detector= HandDetector(maxHands=2)
import pickle

# Default values for 
count=1
loop=0
save1 =0
save2 =0
offset=20
# alphabetCount=0


# Load the Model From Model folder
with open("model/KNN_model_English.pkl", 'rb') as file:  
    load_model = pickle.load(file)
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

    
# def Prediction(TotalArray):
#     prediction=load_model.predict([TotalArray])
#     print(prediction, end=", ")
#     # score= load_model.decision_function([totalArray])
#     score= load_model.predict_proba([totalArray])
#     # print(score)
#     maxValue=np.max(score)
#     print("Max value= ",maxValue,end=",")
#     max=np.argmax(score)
#     print(max)
#     cv2.rectangle(frame, (x - offset, y - offset-50),
#     (x - offset+90, y - offset-50+50), (255, 0, 255), cv2.FILLED)
#     cv2.putText(frame, str(prediction[0]), (x, y -26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
#     cv2.rectangle(frame, (x-offset, y-offset),
#     (x + w+offset, y + h+offset), (255, 0, 255), 4)


eleven_zero=[]

for i in range(0,10):
    eleven_zero.append(0)
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
            x,y,w,h=hand1["bbox"]
            lmList1=hand1['lmList']
            leftFeatures=Features_Extraction(lmList1)

            # print(type(leftFeatures))
            zero_string = '0' * 11
            zero_array = np.array(list(zero_string))


            zero_string = zero_array.tostring()
            zero_string = zero_string.decode('utf-8')
            zero_string = ','.join(zero_array)
            # print(zero_string)

            totalArrayLeft=leftFeatures+','+zero_string
            values = [float(x) for x in totalArrayLeft.split(',')]

            # Create a 2D NumPy array
            zero_array = np.array(values).reshape(1, -1)

            # Convert the 2D NumPy array back to a string
            zero_string = ','.join(map(str, zero_array[0]))
            # print(totalArrayLeft)
            # Prediction(zero_string)
            

            if len(hands)==2:
                hand2=hands[1]
                lmList2=hand2['lmList']
                
                rightFeatures=Features_Extraction(lmList2)
                length2Hand, info2Hand, img2Hand=Detector.findDistance(lmList1[4][:2],lmList2[4][:2],img)
                total=leftFeatures+','+rightFeatures+','+str(round(length2Hand,3))
                totalArray=np.fromstring(total, dtype=float, sep=",")
                prediction=load_model.predict([totalArray])
                print(prediction, end=", ")
                # score= load_model.decision_function([totalArray])
                score= load_model.predict_proba([totalArray])
                # print(score)
                maxValue=np.max(score)
                print("Max value= ",maxValue,end=",")
                max=np.argmax(score)
                print(max)
                cv2.rectangle(frame, (x - offset, y - offset-50),
                (x - offset+90, y - offset-50+50), (255, 0, 255), cv2.FILLED)
                cv2.putText(frame, str(prediction[0]), (x, y -26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
                cv2.rectangle(frame, (x-offset, y-offset),
                (x + w+offset, y + h+offset), (255, 0, 255), 4)         
    cv2.imshow("Webcam", frame)
    
    # Exit when 'q' is pressed
    key=cv2.waitKey(1)
    if key==ord("q"):
        break
    # if cv2.waitKey(1) & 0xFF == ord('q'):
        # break
    # elif 

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()


