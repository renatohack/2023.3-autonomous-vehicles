import cv2
import numpy as np

# Carregar o classificador Haar Cascade para detecção de faces
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicializar a câmera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detectar faces na imagem
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Divide-se o display em 4 linhas horizontais e verticais (4x4). O retângulo de referência será definido pelas 4 células centrais (1,2; 1,3; 2,2; 2,3)
        frame_height, frame_width, _ = frame.shape
        a, b = frame_width // 4, frame_height // 4
        cv2.rectangle(frame, (a, b), (3 * a, 3 * b), (0, 255, 0), 2 )

        # Calcular o centro da face
        # x e y são as coords do ponto top_left e i, j as coords do ponto bottom_right do rosto
        i, j = x + w, y + h

        # coordenadas de referencia para as setas
        center_x = x + w // 2
        center_y = y + h // 2

        arrow_size = 50
        arrow_color = (0, 255, 0)  # Cor da seta (verde)

        # se coord x do bottom_right estiver à direita da 3a linha vertical
        if i > 3 * a:
            arrow = np.zeros((arrow_size, arrow_size, 3), dtype=np.uint8)
            cv2.arrowedLine(arrow, (arrow_size-1, arrow_size//2), (0, arrow_size//2), arrow_color, 3)
            frame[center_y-arrow_size//2:center_y+arrow_size//2, 0:arrow_size] = arrow

        # se coord x do top_left estiver à esquerda da 1a linha vertical
        if x < a:
            arrow = np.zeros((arrow_size, arrow_size, 3), dtype=np.uint8)
            cv2.arrowedLine(arrow, (0, arrow_size//2), (arrow_size-1, arrow_size//2), arrow_color, 3)
            frame[center_y-arrow_size//2:center_y+arrow_size//2, frame_width-arrow_size:frame_width] = arrow

        # se coor y do top_left estiver acima da 1a linha horizontal
        if y < b:
            arrow = np.zeros((arrow_size, arrow_size, 3), dtype=np.uint8)
            cv2.arrowedLine(arrow, (arrow_size//2, 0), (arrow_size//2, arrow_size-1), arrow_color, 3)
            frame[frame_height-arrow_size:frame_height, center_x-arrow_size//2:center_x+arrow_size//2] = arrow

        # se coord y do bottom_right estiver abaixo da 3a linha horizontal
        if j > 3 * b:
            arrow = np.zeros((arrow_size, arrow_size, 3), dtype=np.uint8)
            cv2.arrowedLine(arrow, (arrow_size//2, arrow_size-1), (arrow_size//2, 0), arrow_color, 3)
            frame[0:arrow_size, center_x-arrow_size//2:center_x+arrow_size//2] = arrow


    cv2.imshow('Detec face', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
