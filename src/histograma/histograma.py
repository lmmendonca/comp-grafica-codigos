import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import cv2



#img = Image.open("../images/imagem-teste.jpg")


def geraHistograma(img):
    _ = plt.hist(np.ravel(img), 256, [0, 256], color='red')
    _ = plt.xlabel('INTENCIDADE DA COR')
    _ = plt.ylabel('NUMERO DE REPETIÇOES')
    plt.show()

img = cv2.imread("../images/imagem-teste.jpg")

color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.show()