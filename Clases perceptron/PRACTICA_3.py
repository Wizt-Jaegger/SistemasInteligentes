import cv2
import numpy as np

imagenBRG = cv2.imread("clase_21_03_25.png")

if imagenBRG is None:
    print("La imagen no se pudo cargar. Verifica la ruta.")
    exit()

height, width = imagenBRG.shape[:2]
imagenBRGGris = np.zeros((height, width, 3), np.uint8)  

print("El alto es:", height)
print("El ancho es:", width)
cv2.imshow("Primera imagen", imagenBRG)
cv2.imshow("Imagen con bordes", edges)


for i in range(width):
    for j in range(height):
        b = imagenBRG.item(j, i, 0)
        g = imagenBRG.item(j, i, 1)
        r = imagenBRG.item(j, i, 2)

        
        gris = int(0.114 * b + 0.587 * g + 0.299 * r)
        imagenBRGGris[j, i] = [gris, gris, gris]

        
        tr = 0.393 * r + 0.769 * g + 0.189 * b
        tg = 0.349 * r + 0.686 * g + 0.168 * b
        tb = 0.272 * r + 0.534 * g + 0.131 * b

        imagenBRGGris[j, i, 2] = min(255, int(tr)) 
        imagenBRGGris[j, i, 1] = min(255, int(tg))  
        imagenBRGGris[j, i, 0] = min(255, int(tb))  

cv2.imshow("Imagen Gris y Sepia", imagenBRGGris)
cv2.waitKey(0)
cv2.destroyAllWindows()
