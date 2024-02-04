import cv2
import numpy as np

# Carrega imagem de exemplo em cores originais
imagem = cv2.imread("imgs/exemplo.jpg")

# Converte a imagem para  HSV
hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Mostrar a imagem original e a imagem em hsv
cv2.imshow('original', imagem)
cv2.imshow('hsv', hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()