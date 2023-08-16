import cv2
from HandTrackingModule import HandDetector
import math
Detector= HandDetector()
# Alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# capture= cv2.VideoCapture(0)
# capture.set(3, 1080)
# capture.set(4, 720)
capture = cv2.VideoCapture(0)

# Create a named window
cv2.namedWindow("Webcam", cv2.WINDOW_NORMAL)  # Use WINDOW_NORMAL for resizable window

# Set the initial window size
cv2.resizeWindow("Webcam", 800, 600)  # Adjust the size as needed
offset = 20
imgSize = 300
file = open('Sani.csv', 'a')
count=1
loop=0

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



                # ratio=[ratio_BT,ratio_BI,ratio_BR,ratio_BL]
                ratio=str(ratio_BT)+','+ str(ratio_BI)+','+str(ratio_BR)+','+str(ratio_BL)+','+str(ratio_BLT)
                ratio1=str(ratio_8_20)+','+str(ratio_12_20)+','+str(ratio_16_20)+','+str(ratio_16_12)+','+str(ratio_8_12)
                
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
        if key==ord("s"):
            print(count,ratio1)
            count+=1
            total= ratio+ ","+ ratio1
            # total= round(ratio,3)+ ","+ round(ratio1,3)
            file.write(total)
            file.write("\n")
            # with open("text.txt", 'w') as f:
            #     for s in ratio:
            #         f.write(str(s) + '\n')
            # cv2.imwrite(f"{folder}/Image_"{time.time()}.png", imgWhite)
            # cv2.imwrite(f"{folder}/Image_{time.time()}.png",imgWhite)
            # print(counter)
        elif key==ord("q"):
            break
    else:
        break