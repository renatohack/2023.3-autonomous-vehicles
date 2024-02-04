import cv2

# Carrega uma imagem em escala de cinza
imagem = cv2.imread("imgs/exemplo.jpg")
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Aplica o operador Sobel nas direções X e Y
sobel_x = cv2.Sobel(imagem_cinza, cv2.CV_64F, 1, 0, ksize=11)
sobel_y = cv2.Sobel(imagem_cinza, cv2.CV_64F, 0, 1, ksize=11)

# Mostrar a imagem original e a imagem com bordas
cv2.imshow('Sobel X', sobel_x)
cv2.imshow('Sobel Y', sobel_y)
cv2.imshow('imagem Original', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
