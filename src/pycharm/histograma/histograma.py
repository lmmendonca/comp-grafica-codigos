import cv2
import matplotlib.pyplot as plt
import numpy as np


# img = Image.open("../images/imagem-teste.jpg")


def geraHistograma(img):
    _ = plt.hist(np.ravel(img), 256, [0, 256], color='red')
    _ = plt.xlabel('INTENCIDADE DA COR')
    _ = plt.ylabel('NUMERO DE REPETIÇOES')
    plt.show()


def geraHistogramaSeparado(path):
    img = cv2.imread(path)
    print(img)
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.show()


geraHistogramaSeparado("../images/imagem-teste.jpg")
