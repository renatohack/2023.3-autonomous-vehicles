import cv2
import numpy as np
import matplotlib.pyplot as plt
import util

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

        frame_height, frame_width, _ = frame.shape
        a, b = frame_width // 4, frame_height // 4
        cv2.rectangle(frame, (a, b), (3 * a, 3 * b), (0, 255, 0), 2 )

        # Calcular o centro da face
        i, j = x + w, y + h

        center_x = x + w // 2
        center_y = y + h // 2

        arrow_size = 50
        arrow_color = (0, 255, 0)  # Cor da seta (verde)

        if (i - x > 2 * a) or (j - y > 2 * b):
            util.show_msg("AFASTE-SE DA TELA", frame)

        if i > 3 * a:
            util.show_arrow('left', frame, center_y, center_x, frame_width, frame_height)

        if x < a:
            util.show_arrow('right', frame, center_y, center_x, frame_width, frame_height)

        if y < b:
            util.show_arrow('bottom', frame, center_y, center_x, frame_width, frame_height)

        if j > 3 * b:
            util.show_arrow('up', frame, center_y, center_x, frame_width, frame_height)

    cv2.imshow('Centralizar rosto', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
