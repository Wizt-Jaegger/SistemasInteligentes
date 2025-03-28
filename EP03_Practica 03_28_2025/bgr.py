import cv2


imagen = cv2.imread('imagen.jpg')
tamanoDeseado = (1100, 700)
imagen = cv2.resize(imagen, tamanoDeseado)

cv2.imshow('imagen original', imagen)

hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
bgra = cv2.cvtColor(imagen, cv2.COLOR_BGR2BGRA)  
ycrcb = cv2.cvtColor(imagen, cv2.COLOR_BGR2YCrCb)
yuv_yvyu = cv2.cvtColor(imagen, cv2.COLOR_BGR2YUV)  

cv2.imshow('imagen en hsv', hsv)
cv2.imshow('imagen en bgra', bgra)
cv2.imshow('imagen en yuv_yvyu', yuv_yvyu)
cv2.imshow('imagen en ycrcb', ycrcb)

cv2.waitKey(0)
cv2.destroyAllWindows()
