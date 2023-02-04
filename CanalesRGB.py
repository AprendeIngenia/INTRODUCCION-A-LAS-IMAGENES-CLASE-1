# Importamos las librerias
import cv2
import matplotlib.pyplot as plt


# Imagen
# Vamos a crear nuestra matriz principal
img = cv2.imread("LEC.png")
# Corregimos
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Extraemos los canales
#R = img[:,:,0]
#G = img[:,:,1]
#B = img[:,:,2]

print(img)

# Comando
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
imgre = cv2.merge((R,G,B))

# IMAGEN ORIGINAL
ax4 = fig.add_subplot(2,2,4)
ax4.imshow(imgre)
ax4.set_title("IMAGEN ORIGINAL")
#plt.imshow(img)

plt.show()

# Con el teclado pasamos la imagen
cv2.waitKey(0)