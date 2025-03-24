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
gris = cv2.cvtColor(imagenBRG, cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagen gris", gris)
edges = cv2.Canny(imagenBRG, 0, 255)
cv2.imshow("Imagen con bordes", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
