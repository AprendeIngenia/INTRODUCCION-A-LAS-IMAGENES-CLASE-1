# Importamos las librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Image


# Imagen
# Vamos a crear nuestra matriz principal
img = cv2.imread("LEC.png")
# Corregimos
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(img)

# Extraemos los canales
R,G,B = cv2.split(img)


# Mostramos nuestros canales
fig = plt.figure()
# CANAL ROJO
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(R, cmap="gray")
ax1.set_title("CANAL ROJO")
# CANAL VERDE
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(G, cmap="gray")
ax2.set_title("CANAL VERDE")
# CANAL AZUL
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(B, cmap="gray")
ax3.set_title("CANAL AZUL")

# RECONSTRUCCION
imgre = cv2.merge((R,G+100,B))

# IMAGEN ORIGINAL
ax4 = fig.add_subplot(2,2,4)
ax4.imshow(imgre)
ax4.set_title("IMAGEN ORIGINAL")

# Guardamos la imagen
cv2.imwrite("NUEVAIMAGEN.PNG", imgre)

plt.show()

# Con el teclado pasamos la imagen
cv2.waitKey(0)