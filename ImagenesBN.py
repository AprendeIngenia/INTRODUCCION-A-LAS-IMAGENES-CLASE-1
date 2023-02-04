# Importamos las librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Imagen Negra
# Vamos a crear nuestra imagen negra
img = np.zeros((10,10,1), np.uint8)

# Cambiamos algunos pixeles
img[0,1] = 30.8
img[2,3] = 50
img[4,5] = 200
img[6,7] = 140

# Mostramos los valores numericos
print(img)

# Mostramos nuestra imagen
plt.imshow(img, cmap='gray')
plt.show()

