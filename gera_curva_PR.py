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

# Generate Precision x Recall Curve (of the Training Part)
T = 18.5/255
classes = ['0 - Uninfected' , '1 - Parasitized']
path = 'G:/Thales/Documents/Acadêmico/Doutorado/Processamento de Imagem/Trabalho Final/cell_images'

score = []
label = []
for i in range(len(classes)):
    N = len(os.listdir(path + '/' + classes[i]))-1
    N0, N = 0, int(0.9*N)
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
label, score = np.array(label), np.array(score)
pos = np.argsort(score)
label, score = label[pos], score[pos]
N = len(label)
TP = np.array([np.sum(label[i:]   ) for i in range(N)])
FP = np.array([np.sum(label[i:]==0) for i in range(N)])
FN = np.array([np.sum(label[:i]   ) for i in range(N)])

precis = np.divide(TP,TP+FP)
recall = np.divide(TP,TP+FN)

dist2 = (1-precis)**2 + (1-recall)**2
pos = np.argmin(dist2)
T = np.mean(score[[pos-1,pos]])
P = precis[pos]
R = recall[pos]
print('Threshold: ' + str(round(T    ,2))      )
print('Precision: ' + str(round(100*P,2)) + '%')
print('Recall: '    + str(round(100*R,2)) + '%')

plt.figure(figsize=[14,7])
plt.subplot(1,2,1); plt.xlabel('Threshold'); plt.ylabel('Metric')
plt.plot(score, precis); plt.plot(score, recall, 'r'); plt.legend(['Precision', 'Recall'])
plt.plot(T, P, 'ok'); plt.plot(T, R, 'ok')
plt.subplot(1,2,2); plt.xlabel('Precision'); plt.ylabel('Recall');
plt.plot(precis, recall, 'black'); plt.plot(P, R, 'ok')