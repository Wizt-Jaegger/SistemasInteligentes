import cv2
import numpy as np
imagenBRG = cv2.imread("clase_21_03_25.png") 

print(imagenBRG[100][100][0])
height, width =(imagenBRG.shape[:2])
imagenBRGGris = np.zeros((height,width,1),np.uint8)

print("El alto es: ",height)
print("El ancho es: ",width)
cv2.imshow("primera imagen",imagenBRG)
for i in range(width):
    for j in range(height):
        b=imagenBRG.item(j,i,0)
        g=imagenBRG.item(j,i,1)
        r=imagenBRG.item(j,i,2)
        imagenBRGGris[j][i]=(int)(b+g+r)/3
cv2.imshow("Imagen Gris",imagenBRGGris)
cv2.waitKey(0)
cv2.destroyAllWindows()