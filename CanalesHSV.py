# Importamos las librerias
import cv2
import matplotlib.pyplot as plt

# Imagen
# Vamos a crear nuestra matriz principal
img = cv2.imread("LEC.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Corregimos
imghsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

# Extraemos los canales
H,S,V = cv2.split(imghsv)

# Mostramos nuestros canales
fig = plt.figure()
# CANAL ROJO
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(H, cmap="gray")
ax1.set_title("CANAL H")
# CANAL VERDE
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(S, cmap="gray")
ax2.set_title("CANAL S")
# CANAL AZUL
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(V, cmap="gray")
ax3.set_title("CANAL V")

# RECONSTRUCCION
imgre = cv2.merge((H,S,V))

# IMAGEN ORIGINAL
ax4 = fig.add_subplot(2,2,4)
ax4.imshow(img)
ax4.set_title("IMAGEN ORIGINAL")

plt.show()

# Con el teclado pasamos la imagen
cv2.waitKey(0)