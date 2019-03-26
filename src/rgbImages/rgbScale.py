from PIL import Image
from numpy import array
import matplotlib.pyplot as plt

img = Image.open("../images/imagem-teste.jpg")


def rgbScale(img):
    a = array(img)
    r, g, b = a.copy(), a.copy(), a.copy()
    for i in range(len(a)):
        for j in range(len(a[i])):
            r[i][j] = [a[i][j][0], 0, 0]
            g[i][j] = [0, a[i][j][1], 0]
            b[i][j] = [0, 0, a[i][j][2]]

    return (Image.fromarray(r), Image.fromarray(g), Image.fromarray(b))


a, b, c = rgbScale(img)

a.show()
b.show()
c.show()
