import numpy
import cv2

# Carrega imagem de exemplo em cores originais
imagem = cv2.imread("imgs/exemplo.jpg")

# Converte a imagem para grayscale
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Mostrar a imagem original e a imagem em escala de cinza
cv2.imshow('original', imagem)
cv2.imshow('grayscale', imagem_cinza)
cv2.waitKey(0)
cv2.destroyAllWindows()