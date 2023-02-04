# Importamos las librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt


# Lectura de imagenes
# Lectura en Gray
imggray = cv2.imread("LEC.png", 0)  # 1 CANAL 1 MATRIZ

# Lectura a color
imgRGB = cv2.imread("LEC.png",1)  # 3 CANALES 3 MATRICES

# Lectura
img = cv2.imread("LEC.png")   # 3 CANALES 3 MATRICES

# Extraer atributos principales
tama = imggray.shape
tipo = imggray.dtype
print("Tamaño Gray | Tipo de Dato |", tama, tipo)

# Extraer atributos principales
tamargb = imgRGB.shape
tiporgb = imgRGB.dtype
print("Tamaño RGB | Tipo de Dato |", tamargb, tiporgb)

# Mostramos las imagenes
cv2.imshow("GRAY", imggray)
cv2.imshow("RGB", imgRGB)
cv2.imshow("IMG", img)

# Correccion COLOR
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Mostramos nuestra imagen
plt.imshow(img)
plt.show()


# Con el teclado pasamos la imagen
cv2.waitKey(0)