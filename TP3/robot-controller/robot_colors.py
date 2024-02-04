import cv2
import numpy as np
import robot_controller as rc

# variaveis globais
thickness = 5
black = (0, 0, 0)
blue = (255, 127, 50)
green = (0, 255, 0)
yellow = (0, 255, 255)
red = (0, 0, 255)
orange = (0, 146, 255)


# Definir caminhos
path_img = "imgs/robot.jpg"
path_template = "imgs/robot_template.jpg"

# Ler imagens
img_original = rc.read_image(path_img)
img_template = rc.read_image(path_template)

# ------------- ENCONTRAR BRAÇO -------------
#Converter imagens para cinza e hsv
img_original_cinza = rc.img_to_grayscale(img_original)
img_template_cinza = rc.img_to_grayscale(img_template)

# Encontrar match da garra
resultado, max_loc = rc.match_robot(img_original_cinza, img_template_cinza)

# Desenhar retangulo na imagem em volta do match
point_top_left = max_loc # ponto superior esquerdo

altura_template = img_template_cinza.shape[0]
largura_template = img_template_cinza.shape[1]
bottom_right_x = point_top_left[0] + largura_template
bottom_right_y = point_top_left[1] + altura_template
point_bottom_right = (bottom_right_x, bottom_right_y) # ponto inferior direito

rc.draw_rectangle_match(img_original, point_top_left, point_bottom_right, black, thickness)



# ------------- ENCONTRAR FRASCO AZUL -------------

# intervalo de cor azul
lower_bound = np.array([40, 35, 20])
upper_bound = np.array([60, 40, 25])

ponto_medio = rc.get_ponto_medio_contornos(img_original, lower_bound, upper_bound)
top_left = (ponto_medio[0] - 20, ponto_medio[1] - 20)
bottom_right = (ponto_medio[0] + 20, ponto_medio[1] + 20)

rc.draw_rectangle_match(img_original, top_left, bottom_right, blue, thickness)



# ------------- ENCONTRAR FRASCO VERDE -------------
# intervalo de cor verde
lower_bound = np.array([50, 50, 50])
upper_bound = np.array([70, 150, 65])

ponto_medio = rc.get_ponto_medio_contornos(img_original, lower_bound, upper_bound)
top_left = (ponto_medio[0] - 20, ponto_medio[1] - 20)
bottom_right = (ponto_medio[0] + 20, ponto_medio[1] + 20)

rc.draw_rectangle_match(img_original, top_left, bottom_right, green, thickness)



# ------------- ENCONTRAR FRASCO AMARELO -------------
# intervalo de cor amarela
lower_bound = np.array([15, 195, 230])
upper_bound = np.array([19, 199, 234])

ponto_medio = rc.get_ponto_medio_contornos(img_original, lower_bound, upper_bound)
top_left = (ponto_medio[0] - 20, ponto_medio[1] - 20)
bottom_right = (ponto_medio[0] + 20, ponto_medio[1] + 20)

rc.draw_rectangle_match(img_original, top_left, bottom_right, yellow, thickness)



# ------------- ENCONTRAR FRASCO VERMELHO -------------
# intervalo de cor vermelha
lower_bound = np.array([125, 125, 235])
upper_bound = np.array([135, 135, 245])

ponto_medio = rc.get_ponto_medio_contornos(img_original, lower_bound, upper_bound)
top_left = (ponto_medio[0] - 20, ponto_medio[1] - 20)
bottom_right = (ponto_medio[0] + 20, ponto_medio[1] + 20)

rc.draw_rectangle_match(img_original, top_left, bottom_right, red, thickness)



# ------------- ENCONTRAR FRASCO LARANJA -------------
# intervalo de cor laranja
lower_bound = np.array([0, 0, 85])
upper_bound = np.array([1, 1, 89])

ponto_medio = rc.get_ponto_medio_contornos(img_original, lower_bound, upper_bound)
top_left = (ponto_medio[0] - 20, ponto_medio[1] - 20)
bottom_right = (ponto_medio[0] + 20, ponto_medio[1] + 20)

rc.draw_rectangle_match(img_original, top_left, bottom_right, orange, thickness)



# Mostrar os resultados
cv2.namedWindow('Detec', cv2.WINDOW_NORMAL)
cv2.imshow('Detec', img_original)
cv2.waitKey(0)
cv2.destroyAllWindows()