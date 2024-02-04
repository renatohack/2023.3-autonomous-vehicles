import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Definir o intervalo da cor vermelha
lower_bound = np.array([0, 50, 50])
upper_bound = np.array([10, 255, 255])

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Converter a imagem para o espaço de cores HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Criar uma máscara para a cor desejada
    mascara = cv2.inRange(hsv, lower_bound, upper_bound)
    
    # Encontrar contornos na máscara
    contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Desenhar os contornos na imagem original
    cv2.drawContours(frame, contornos, -1, (0, 255, 0), 2)
    
    cv2.imshow('Detectar Cores', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break