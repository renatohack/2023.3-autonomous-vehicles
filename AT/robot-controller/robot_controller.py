import cv2
import numpy as np

def read_image(path_img):
    return cv2.imread(path_img)


def img_to_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def img_to_hsv(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


def match_robot(img, template):
    resultado =  cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(resultado)
    
    return resultado, max_loc


def draw_rectangle_match(img, point_top_left, point_bottom_right, color, thickness):
    cv2.rectangle(img, point_top_left, point_bottom_right, color, thickness)

def get_ponto_medio_contornos(img, lower_bound, upper_bound):
    mascara = cv2.inRange(img, lower_bound, upper_bound)
    contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contornos) == 0:
        return (-1, -1)

    x = 0
    y = 0
    for contorno in contornos:
        x += contorno[0][0][0]
        y += contorno[0][0][1]
    x = int(x / len(contornos))
    y = int(y / len(contornos))
    
    return (x, y)

def img_to_lim(img, thresh, maxval):
    _, imagem_limiarizada = cv2.threshold(img, thresh, maxval, cv2.THRESH_BINARY)
    return imagem_limiarizada

def img_to_rgb(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)