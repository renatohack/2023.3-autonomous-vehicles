import cv2
import numpy as np
from keras.models import load_model
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Desativar notação científica para maior clareza
np.set_printoptions(suppress=True)

# Carregar o modelo - treinado no teachable machine (não sei se vai servir com o senhor, professor, mas tentei treinar colocando a mão na frente do rosto)
model = load_model("5/keras_model.h5", compile=False)

# Carregar as classes (Mais Volume - joinha pra cima - e Menos Volume - joinha pra baixo)
class_names = open("5/labels.txt", "r").readlines()

# Obter o dispositivo de reprodução de áudio padrão
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Definir o incremento de volume (0.01 = 1% de aumento)
incremento_volume = 0.01

# Definir o volume mínimo e máximo permitido
volume_minimo = 0.0
volume_maximo = 1.0

# Definir o volume inicial
volume_inicial = 0.5

# Definir o volume atual
volume_atual = volume_inicial

# Camera default
camera = cv2.VideoCapture(0)

while True:
    # Capturar a imagem da câmera
    ret, image = camera.read()

    # Verificar captura de video ocorreu com sucesso
    if not ret:
        print("Falha ao capturar imagem da câmera.")
        break

    # Redimensionar a imagem para (224-altura, 224-largura) pixels para facilitar o processamento (a minha, no caso é uma 720p)
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Converter a imagem em uma matriz numpy e remodelá-la para o formato de entrada do modelo
    image_array = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalizar a matriz de imagem - nesse caso, normalizado para intervalos entre -1 e 1
    normalized_image_array = (image_array / 127.5) - 1

    # Fazer a previsão do modelo
    prediction = model.predict(normalized_image_array)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Adicionar texto de previsão de classe à imagem
    text = f"Classe: {class_name[2:]} ({confidence_score:.2%})"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.4  # Ajustar a escala da fonte para um texto menor
    cor_fonte = (0, 255, 0)  # Cor preta para o texto
    espessura_linha = 2  # Espessura do texto
    tamanho_texto = cv2.getTextSize(text, font, font_scale, espessura_linha)[0]
    posicao_texto_x = 10
    posicao_texto_y = 30 + tamanho_texto[1]  # Ajustar coordenada y para considerar o tamanho do texto
    cv2.putText(image, text, (posicao_texto_x, posicao_texto_y), font, font_scale, cor_fonte, espessura_linha)

    # Exibir o frame na janela
    cv2.imshow("Imagem da Webcam", image)

    # Ajustar o volume de áudio com base na previsão da classe
    if "Menos volume" in class_name:
        volume_atual = max(volume_minimo, volume_atual - incremento_volume)
    elif "Mais volume" in class_name:
        volume_atual = min(volume_maximo, volume_atual + incremento_volume)

    # Definir o novo volume
    volume.SetMasterVolumeLevelScalar(volume_atual, None)

    # Aguardar entrada do teclado.
    tecla_pressionada = cv2.waitKey(1)

    # 27 é o código ASCII para a tecla Esc no teclado.
    if tecla_pressionada == 27:
        break

# Restaurar o volume padrão ao sair do loop
volume.SetMasterVolumeLevelScalar(volume_inicial, None)

camera.release()
cv2.destroyAllWindows()
