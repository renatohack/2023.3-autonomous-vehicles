import cv2


# Carrega imagem de exemplo em cores originais
imagem = cv2.imread("imgs/exemplo.jpg")

# Converte a imagem para grayscale
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Aplica a limiarização
_, imagem_limiarizada = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)

# Mostrar a imagem original e a imagem limiarizada
cv2.imshow('original', imagem)
cv2.imshow('limiarizada', imagem_limiarizada)
cv2.waitKey(0)
cv2.destroyAllWindows()