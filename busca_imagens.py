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

def proporcao_lin_col(IMGS):
    F = [[],[]]
    for i in range(len(IMGS)):
        for j in range(len(IMGS[i])):
            img = IMGS[i][j][:,:,0]
            m, n = np.shape(img)
            F[i].append(m/n)
    
    pos = np.zeros([len(IMGS), 2]).astype(np.int)
    f = np.zeros([len(IMGS), 2])
    for i in range(len(IMGS)):
        pos[i,:] = [int(np.argmax(F[i])), int(np.argmin(F[i]))]
        for j in range(2):
            f[i,j] = F[i][pos[i,j]]
    return f, pos

def proporcao_prox_de_um(IMGS):
    F = [[],[]]
    for i in range(len(IMGS)):
        for j in range(len(IMGS[i])):
            img = IMGS[i][j][:,:,0]
            m, n = np.shape(img)
            F[i].append(abs(m-n))
    
    pos = np.zeros([len(IMGS), 2]).astype(np.int)
    f = np.zeros([len(IMGS), 2])
    for i in range(len(IMGS)):
        pos[i,:] = [int(np.argmax(F[i])), int(np.argmin(F[i]))]
        for j in range(2):
            f[i,j] = F[i][pos[i,j]]
    return f, pos

def proporcao_ocupacao_na_imagem(IMGS):
    F = [[],[]]
    for i in range(len(IMGS)):
        N = len(IMGS[i])
        for j in range(N):
            if j%500 == 0: clc(); print('Classe ' + classes[i] + ': ' + str(round(j/N*100,2)) + '%'); time.sleep(0.1)
            img = np.sum(IMGS[i][j],2)
            m, n = np.shape(img)
            pos = np.where(img != 0)
            F[i].append(len(pos[0])/(m*n))
    
    pos = np.zeros([len(IMGS), 2]).astype(np.int)
    f = np.zeros([len(IMGS), 2])
    for i in range(len(IMGS)):
        pos[i,:] = [int(np.argmax(F[i])), int(np.argmin(F[i]))]
        for j in range(2):
            f[i,j] = F[i][pos[i,j]]
    return f, pos

# Busca imagens na base que maximizam/minimizam alguma função f
classes = ['0 - Uninfected' , '1 - Parasitized']
f = proporcao_ocupacao_na_imagem

IMGS = [[],[]]
for i in range(len(classes)):
    N = len(os.listdir('cell_images/' + classes[i]))-1
    N0 = 0
    for num in range(N0,N):
        if num%500 == 0: clc(); print('Classe ' + classes[i] + ': ' + str(round((num-N0)/(N-N0)*100,2)) + '%'); time.sleep(0.1)
        img_path = 'cell_images/' + classes[i] + '/' + str(num) + '.png'
        img = np.array(imageio.imread(img_path))/255
        IMGS[i].append(img)

clc()
f, pos = f(IMGS)

plt.figure(figsize=[10,10])
k=0
for i in range(len(IMGS)):
    for j in range(2):
        k+=1
        plt.subplot(2,2,k); plt.imshow(IMGS[i][pos[i,j]])
        plt.axis('off'); plt.title(str(pos[i,j]) + ' (f = ' + str(round(f[i,j],2)) + ')')


            