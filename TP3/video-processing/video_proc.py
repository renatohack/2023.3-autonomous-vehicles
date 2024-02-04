import cv2

# Define caminhos de entrada e saida
input_video_file = "imgs/video_exemplo.mp4"
output_video_file = "imgs/video_exemplo_output.mp4"

# Abre o arquivo de vídeo de entrada
cap = cv2.VideoCapture(input_video_file)

# Verifica se o arquivo foi aberto com sucesso
if not cap.isOpened():
    print("Erro ao abrir o arquivo de vídeo.")
    exit()

# Obtem largura, altura e framerate
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_rate = int(cap.get(5))

# Define o codec e cria um objeto VideoWriter para o arquivo de saída
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_video_file, fourcc, frame_rate, (frame_width, frame_height), isColor=False)

while True:
    ret, frame = cap.read()

    # Se não houver mais leitura, sair
    if not ret:
        break

    # Converte para escala de cinza
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Grava o quadro pré-processado no vídeo de saída
    out.write(gray_frame)

    # Mostra o quadro pré-processado em uma janela
    cv2.imshow('Video Processado', gray_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera os objetos VideoCapture e VideoWriter
cap.release()
out.release()

# Fecha todas as janelas abertas
cv2.destroyAllWindows()

print("Vídeo processado e exportado com sucesso!")
