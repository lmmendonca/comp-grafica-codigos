from PIL import Image
from numpy import array

img = Image.open("../images/imagem-teste.jpg")

def grayScale(img):
    a = array(img)
    for i in range(len(a)):
        for j in range(len(a[i])):
            t = sum(a[i][j]) // 3
            a[i][j] = [t, t, t]
    return Image.fromarray(a)




x = grayScale(img)

x.show()

