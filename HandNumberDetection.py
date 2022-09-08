import HandTrackingModule as htm
import mediapipe as mp
import cv2
import time
from google.protobuf.json_format import MessageToDict


pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()
tipIds = [4, 8, 12, 16, 20]
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    leftHand, multiHands = detector.findPosition(img)

    if len(leftHand) != 0:
        fingersLeft = []
        for id in range(1, 5):
            if leftHand[tipIds[id]][2] < leftHand[tipIds[id]-2][2]:
                fingersLeft.append(1)
            else:
                fingersLeft.append(0)
        
        # thumb
        if leftHand[tipIds[0]][1] > leftHand[tipIds[0]-1][1]:
            fingersLeft.append(1)
        else:
            fingersLeft.append(0)
        cv2.circle(img, (leftHand[8][1], leftHand[8][2]),
                   2, (255, 255, 0), 3, cv2.FILLED)
        cv2.putText(img, str(sum(fingersLeft)), (100, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 3, (125, 233, 231), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
