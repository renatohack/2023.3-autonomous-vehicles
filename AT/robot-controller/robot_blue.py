# LÓGICA E CONSIDERAÇÕES AO FINAL DO CÓDIGO

import cv2
import numpy as np
import robot_controller as rc

# variaveis globais
thickness = 2
black = (0, 0, 0)
blue = (255, 127, 50)
green = (0, 255, 0)
yellow = (0, 255, 255)
red = (0, 0, 255)
orange = (0, 146, 255)


# Definir caminhos
path_img = "7/imgs/robot.jpg"

# Ler imagens
img_original = rc.read_image(path_img)
img_original_hsv = rc.img_to_hsv(img_original)



# ------------- ENCONTRAR FRASCO AZUL -------------

# intervalo de cor azul
lower_bound = np.array([80, 50, 0])
upper_bound = np.array([110, 255, 255])

mascara = cv2.inRange(img_original_hsv, lower_bound, upper_bound)
cv2.namedWindow('mask-blue', cv2.WINDOW_NORMAL)
cv2.imshow('mask-blue', mascara)

contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

maiorArea = 0
maior_contorno = None
for contorno in contornos:
    if cv2.contourArea(contorno) > maiorArea:
        maiorArea = cv2.contourArea(contorno)
        maior_contorno = contorno

x, y, w, h = cv2.boundingRect(maior_contorno)
rc.draw_rectangle_match(img_original, (x, y), (x + w, y + h), blue, thickness)



# Mostrar os resultados
cv2.namedWindow('Detec', cv2.WINDOW_NORMAL)
cv2.imshow('Detec', img_original)
cv2.waitKey(0)
cv2.destroyAllWindows()