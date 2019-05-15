'''
Name: Thales de Oliveira Goncalves
USP Number: 11383541
Course Code: SCC5830
Year/Semester: 2019/1
Final Project
'''

import os
import numpy as np
import imageio
import matplotlib.pyplot as plt

# Analisa Histogramas de Toda a Base
bins_num = 20
bins_range = [0,1]

classes = ['0 - Uninfected' , '1 - Parasitized']
hist = np.zeros([len(range(classes)), bins_num])
bins_edges = np.linspace(bins_range[0], bins_range[1], bins_num+1)
bins_means = np.mean(np.concatenate(CONCATENA NAS LINHAS E DEPOIS FAZ A MEDIA)
for i in range(len(classes)):
    N = len(os.listdir('cell_images/' + classes[i]))-1
    N = 1
    for num in range(N):
        img_path = 'cell_images/' + classes[i] + '/' + str(num) + '.png'
        img = np.array(imageio.imread(img_path))/255
        pos = np.where(np.sum(img,2)!=0)
        for j in range(3):
            camada = img[:,:,j]
            camada[pos] = camada[pos]-np.median(camada[pos])
        img[img>0] = 0
        img = abs(img)
        h = np.histogram(img, bins=bins_num, range=bins_range)
        
            