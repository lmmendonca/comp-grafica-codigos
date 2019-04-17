from PIL import Image
from matplotlib import pyplot as plt
from numpy import array


def rgbScale(img):
    a = array(img)
    r, g, b = a.copy(), a.copy(), a.copy()
    for i in range(len(a)):
        for j in range(len(a[i])):
            r[i][j] = [a[i][j][0], 0, 0]
            g[i][j] = [0, a[i][j][1], 0]
            b[i][j] = [0, 0, a[i][j][2]]

    return (Image.fromarray(r), Image.fromarray(g), Image.fromarray(b))


# Tarefa 1

def subplotImagens(path):
    img = Image.open(path)
    a, b, c = rgbScale(img)

    plt.subplot(231)
    plt.imshow(img)
    plt.subplot(232)
    plt.imshow(a)
    plt.subplot(234)
    plt.imshow(b)
    plt.subplot(235)
    plt.imshow(c)


# Tarefa 2

def grayScale(img):
    a = array(img)
    for i in range(len(a)):
        for j in range(len(a[i])):
            t = sum(a[i][j]) // 3
            a[i][j] = [t, t, t]
    return Image.fromarray(a)


def pretoBranco(img):
    a = array(img)
    for i in range(len(a)):
        for j in range(len(a[i])):
            t = sum(a[i][j]) // 3
            if t > 127:
                a[i][j] = [255, 255, 255]
            else:
                a[i][j] = [0, 0, 0]
    return Image.fromarray(a)


def pretoBrancoPelaMediaMatriz(img):
    a = array(img)
    media = a.mean()
    for i in range(len(a)):
        for j in range(len(a[i])):
            t = sum(a[i][j]) // 3
            if media > t:
                a[i][j] = [255, 255, 255]
            else:
                a[i][j] = [0, 0, 0]
    return Image.fromarray(a)


def subplotGrayScale(path):
    img = Image.open(path)

    a = grayScale(img)
    b = pretoBranco(a)
    c = pretoBrancoPelaMediaMatriz(a)

    plt.subplot(231)
    plt.imshow(a)
    plt.subplot(232)
    plt.imshow(b)
    plt.subplot(233)
    plt.imshow(c)


subplotGrayScale("../images/imagem-teste.jpg")
