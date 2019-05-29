'''
Name: Thales de Oliveira Goncalves
USP Number: 11383541
Course Code: SCC5830
Year/Semester: 2019/1
Final Project - Detecting Malaria Desease in Cell Images
'''

import os
import numpy as np
import imageio
import matplotlib.pyplot as plt
import time
from ccc import clc, clear
clc(); exec(clear())

# Generate Metrics on the Testing Subset
T = 0.0725490196078431 # = 18.5/255 (no report está 0.073)
classes = ['0 - Uninfected' , '1 - Parasitized']
path = 'G:/Thales/Documents/Acadêmico/Doutorado/Processamento de Imagem/Trabalho Final/cell_images'

score = []
label = []
for i in range(len(classes)):
    N = len(os.listdir(path + '/' + classes[i]))-1
    N0 = int(0.9*N)
    label += [int(classes[i][0])]*(N-N0)
    for num in range(N0,N):
        if num%500 == 0: clc(); print('Classe ' + classes[i] + ': ' + str(round((num-N0)/(N-N0)*100,2)) + '%'); time.sleep(0.1)
        img_path = path + '/' + classes[i] + '/' + str(num) + '.png'
        img = np.array(imageio.imread(img_path))/255
        pos = np.where(np.sum(img,2)!=0)
        for j in range(3):
            camada = img[:,:,j]
            camada[pos] = camada[pos]-np.median(camada[pos])
        img[img>0] = 0
        img = abs(img)
        pos = np.where(np.sqrt(np.sum(img**2,2))<T)
        for j in range(3):
            camada = img[:,:,j]
            camada[pos] = 0
        score.append(np.sum(np.sqrt(np.sum(img**2,2))))

clc()
T = 36.70535787931294 # (no report está 36.71)
label, score = np.array(label), np.array(score)
classe = score>T
N = len(label)
TP = np.sum(   classe  &    label )
FP = np.sum(   classe  & (1-label))
FN = np.sum((1-classe) &    label )

P = TP/(TP+FP)
R = TP/(TP+FN)

print('Precision: ' + str(round(100*P,2)) + '%')
print('Recall: '    + str(round(100*R,2)) + '%')