import cv2
import numpy as np
import imutils


azulBajo = np.array([80, 50, 20], np.uint8)
azulAlto = np.array([150, 255, 255], np.uint8)


image = cv2.imread("rubioRuido.jpg")
image = imutils.resize(image, width=640)
image = cv2.blur(image, (4, 4))
#image = cv2.GaussianBlur(image, (5, 5), 0)
#image = cv2.medianBlur(image, 5)


imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imageGray = cv2.cvtColor(imageGray, cv2.COLOR_GRAY2BGR)
imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


maskAzul = cv2.inRange(imageHSV, azulBajo, azulAlto)
maskAzul = cv2.medianBlur(maskAzul, 7)
blueDetected = cv2.bitwise_and(image, image, mask=maskAzul)


invMask = cv2.bitwise_not(maskAzul)
bgGray = cv2.bitwise_and(imageGray, imageGray, mask=invMask)


finalImage = cv2.add(bgGray, blueDetected)


cv2.imshow('image', blueDetected)
cv2.imshow('imageGray', imageGray)
cv2.imshow('Invertida', invMask)
cv2.imshow('bgGray', bgGray)
cv2.imshow('finalImage', finalImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
