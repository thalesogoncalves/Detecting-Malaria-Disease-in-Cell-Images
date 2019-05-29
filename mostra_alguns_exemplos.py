'''
Name: Thales de Oliveira Goncalves
USP Number: 11383541
Course Code: SCC5830
Year/Semester: 2019/1
Final Project - Detecting Malaria Desease in Cell Images
'''

import numpy as np
import imageio
import matplotlib.pyplot as plt
from ccc import clc, clear
clc(); exec(clear())

# Mostra alguns exemplos da base de dados
plot_param = {'fontsize' : 15, 'fontweight' : "bold"}
classes = ['0 - Uninfected' , '1 - Parasitized']
Ex_N = [[2891, 1793, 10822, 3206],[4198, 11197, 7448, 4698]]
n = len(Ex_N[0])
path = 'G:/Thales/Documents/Acadêmico/Doutorado/Processamento de Imagem/Trabalho Final/cell_images'

Ex_path = [path + '/' + classes[0] + '/' + str(num) + '.png' for num in Ex_N[0]] +\
          [path + '/' + classes[1] + '/' + str(num) + '.png' for num in Ex_N[1]]
Ex = [np.array(imageio.imread(img_path))/255 for img_path in Ex_path]


plt.figure(figsize=[15,9])

k = 1
for img in Ex[:4]:
    lin, col = np.shape(np.mean(img,2))
    pos = np.where(np.mean(img,2) != 0)
    plt.subplot(n,2,k); plt.imshow(img); plt.axis('off')
    plt.title(str(lin) + ' x ' + str(col) + ' (' + str(round(len(pos[0])/(lin*col)*100,2)) + '% occupation)')
    k += 2
    
k = 2
for img in Ex[4:]:
    lin, col = np.shape(np.mean(img,2))
    pos = np.where(np.mean(img,2) != 0)
    plt.subplot(n,2,k); plt.imshow(img); plt.axis('off')
    plt.title(str(lin) + ' x ' + str(col) + ' (' + str(round(len(pos[0])/(lin*col)*100,2)) + '% occupation)')
    k += 2

# Mostra alguns exemplos de casos que foram classificados de maneira errada
Ex_N = [[13259, 13739, 12488, 13491],[12675, 12409, 12425, 13033]]
Ex_score = [[302.91283961, 146.42072678, 38.83278426, 37.27420164],[1.9074889, 3.56627528, 32.8832166, 36.63244538]]
n = len(Ex_N[0])

Ex_path = ['cell_images/' + classes[0] + '/' + str(num) + '.png' for num in Ex_N[0]] +\
          ['cell_images/' + classes[1] + '/' + str(num) + '.png' for num in Ex_N[1]]
Ex = [np.array(imageio.imread(img_path))/255 for img_path in Ex_path]


plt.figure(figsize=[15,9])

k = 1
k2 = 0
for img in Ex[:4]:
    lin, col = np.shape(np.mean(img,2))
    pos = np.where(np.mean(img,2) != 0)
    plt.subplot(n,2,k); plt.imshow(img); plt.axis('off')
    plt.title('Score = ' + str(round(Ex_score[0][k2],2)))
    k += 2
    k2+= 1
    
k = 2
k2 = 0
for img in Ex[4:]:
    lin, col = np.shape(np.mean(img,2))
    pos = np.where(np.mean(img,2) != 0)
    plt.subplot(n,2,k); plt.imshow(img); plt.axis('off')
    plt.title('Score = ' + str(round(Ex_score[1][k2],2)))
    k += 2
    k2+= 1