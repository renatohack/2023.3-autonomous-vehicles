# LÓGICA E CONSIDERAÇÕES AO FINAL DO CÓDIGO

import cv2
import numpy as np
import robot_controller as rc
import sys

# variaveis globais
thickness = 5
black = (0, 0, 0)
blue = (255, 127, 50)
green = (0, 255, 0)
yellow = (0, 255, 255)
red = (0, 0, 255)
orange = (0, 146, 255)


# Definir caminhos
path_img = "7/imgs/robot.jpg"
path_template = "7/imgs/robot_template.jpg"

# Ler imagens
img_original = rc.read_image(path_img)
img_template = rc.read_image(path_template)

# ------------- ENCONTRAR BRAÇO -------------
#Converter imagens para cinza
img_original_cinza = rc.img_to_grayscale(img_original)
img_template_cinza = rc.img_to_grayscale(img_template)
img_original_hsv = rc.img_to_hsv(img_original)

# Encontrar match
resultado, max_loc = rc.match_robot(img_original_cinza, img_template_cinza)

if not resultado.any():
    print("Template da garra não encontrado.")
    sys.exit()

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
if ponto_medio[0] == -1:
    print("Frasco AZUL não encontrado.")
    sys.exit()

top_left = (ponto_medio[0] - 20, ponto_medio[1] - 20)
bottom_right = (ponto_medio[0] + 20, ponto_medio[1] + 20)

rc.draw_rectangle_match(img_original, top_left, bottom_right, blue, thickness)



# ------------- ENCONTRAR FRASCO VERDE -------------
# intervalo de cor verde
lower_bound = np.array([50, 50, 50])
upper_bound = np.array([70, 150, 65])

ponto_medio = rc.get_ponto_medio_contornos(img_original, lower_bound, upper_bound)
if ponto_medio[0] == -1:
    print("Frasco VERDE não encontrado.")
    sys.exit()

top_left = (ponto_medio[0] - 20, ponto_medio[1] - 20)
bottom_right = (ponto_medio[0] + 20, ponto_medio[1] + 20)

rc.draw_rectangle_match(img_original, top_left, bottom_right, green, thickness)



# ------------- ENCONTRAR FRASCO AMARELO -------------
# intervalo de cor amarela
lower_bound = np.array([15, 195, 230])
upper_bound = np.array([19, 199, 234])

ponto_medio = rc.get_ponto_medio_contornos(img_original, lower_bound, upper_bound)
if ponto_medio[0] == -1:
    print("Frasco AMARELO não encontrado.")
    sys.exit()

top_left = (ponto_medio[0] - 20, ponto_medio[1] - 20)
bottom_right = (ponto_medio[0] + 20, ponto_medio[1] + 20)

rc.draw_rectangle_match(img_original, top_left, bottom_right, yellow, thickness)



# ------------- ENCONTRAR FRASCO VERMELHO -------------
# intervalo de cor vermelha
lower_bound = np.array([125, 125, 235])
upper_bound = np.array([135, 135, 245])

ponto_medio = rc.get_ponto_medio_contornos(img_original, lower_bound, upper_bound)
if ponto_medio[0] == -1:
    print("Frasco VERMELHO não encontrado.")
    sys.exit()

top_left = (ponto_medio[0] - 20, ponto_medio[1] - 20)
bottom_right = (ponto_medio[0] + 20, ponto_medio[1] + 20)

rc.draw_rectangle_match(img_original, top_left, bottom_right, red, thickness)



# ------------- ENCONTRAR FRASCO LARANJA -------------
# intervalo de cor laranja
lower_bound = np.array([0, 0, 85])
upper_bound = np.array([1, 1, 89])

ponto_medio = rc.get_ponto_medio_contornos(img_original, lower_bound, upper_bound)
if ponto_medio[0] == -1:
    print("Frasco LARANJA não encontrado.")
    sys.exit()

top_left = (ponto_medio[0] - 20, ponto_medio[1] - 20)
bottom_right = (ponto_medio[0] + 20, ponto_medio[1] + 20)

rc.draw_rectangle_match(img_original, top_left, bottom_right, orange, thickness)



# Mostrar os resultados
cv2.namedWindow('Detec', cv2.WINDOW_NORMAL)
cv2.imshow('Detec', img_original)
cv2.waitKey(0)
cv2.destroyAllWindows()


# LÓGICA 
# 1. Cada frasco é identificado pela cor do seu retângulo definido no início do código.
# 2. Inicialmente a garra está aberta.
# 3. O usuário digita o comando (cor do frasco) e a garra passa a se movimentar.
# 4. A garra percorre o eixo x até que sua posição X' seja a mesma posição X do ponto médio do retângulo em questão (aqui, consideramos que os pontos médios estão mais ou menos à meia largura de cada frasco, então podemos considerar a posição X' para a garra como sendo a própria posição X do ponto médio de cada frasco).
# 5. Ao atingir a posição X, a garra começa a descer, variando sua posição Y'. A garra deve se posicionar levemente acima do ponto médio do retângulo para ser capaz de agarrar o frasco pelo seu gargalo. Para isso, basta aplicar uma translação do tipo Y' = Y - X, onde Y' é a posição y que a garra deve se posicionar, Y é a posição y do ponto médio do retângulo e X é a translação padrão. Para um valor padrão da translação devemos calcular a proporcionalidade entre a altura do líquido e a altura do gargalo. 
# 6. A garra se mantém aberta até desde o momento em que o usuário digita o comando até o momento em que atinge a posição (X', Y') final.
# 7. Ao atingir a posição final, a garra se fecha e se mantém fechada, voltando à sua posição inicial.



# CONSIDERAÇÕES
# 1. Para garantir a posição correta da garra, um sistema do tipo eye-to-hand deverá ser implementado em conjunto com a funcionalidade match template. Dessa forma, como um sistema de malha fechada, o sistema pode realizar correções até que a posição da garra esteja esteja ideal.
# 2. Técnicas de pré-processamento "básicas" foram implementadas para a tentativa de se contornar perfeitamente o frasco de cada cor, porém elas não foram suficientes para conseguir um contorno único que não retornassem falsos positivos de outras cores (ex: contorno azul também contornando o frasco verde). Técnicas utilizadas incluem limiarização, HSV e alterações na luminosidade/brilho da imagem. No fim, utilizei um intervalo de cores que me garantia que a grande maioria dos pontos encontrados fizessem parte APENAS do frasco em questão. Isso me garantiria que o ponto médio dos pontos estaria dentro do frasco. Uma outra técnica poderia ser utilizar um intervalo de cores mais "geral" em conjunto com uma média ponderada para dar mais peso a vizinhos mais próximos (pontos acumulados em um frasco teriam mais peso que pontos espaçados em outros frascos).