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

n = 4
plotar = True
plot_param = {'fontsize' : 15, 'fontweight' : "bold"}
classes = ['0 - Uninfected' , '1 - Parasitized']
#ajusta = (1+np.arange(n*4)).reshape([n,4]).T.flatten()

# Sorteia figuras e plota
N0 = len(os.listdir('cell_images/' + classes[0]))-1
N1 = len(os.listdir('cell_images/' + classes[1]))-1
IMGS_path = ['cell_images/' + classes[0] + '/' + str(num) + '.png' for num in np.random.randint(0,N0+1,n)] +\
            ['cell_images/' + classes[1] + '/' + str(num) + '.png' for num in np.random.randint(0,N1+1,n)]
IMGS = [np.array(imageio.imread(img_path))/255 for img_path in IMGS_path]

if plotar:
    plt.figure(figsize=(15,9))
    
    k = 1
    for img in IMGS[:n]:
        plt.subplot(n,3,k)
        plt.imshow(img)
        plt.axis('off')
        if k==1 : plt.title('Não infectadas', plot_param)
        k += 3
        
    k = 3
    for img in IMGS[n:]:
        plt.subplot(n,3,k)
        plt.imshow(img)
        plt.axis('off')
        if k==3 : plt.title('Infectadas', plot_param)
        k += 3
        
        
# Calcula Medianas
IMGS_medianas = [np.zeros(np.shape(img)) for img in IMGS]
for i in range(2*n):
    img = IMGS[i].copy()
    pos = np.where(np.sum(img,2)!=0)
    for j in range(3):
        camada = img[:,:,j]
        camada[pos] = np.median(camada[pos])
    IMGS_medianas[i] = img.copy()

if plotar:
    plt.figure(figsize=(15,9))
    
    k = 1
    for img in IMGS[:n]:
        plt.subplot(n,5,k)
        plt.imshow(img)
        plt.axis('off')
        if k==1 : plt.title('Não infectadas', plot_param)
        k += 5
    
    k = 2
    for img in IMGS_medianas[:n]:
        plt.subplot(n,5,k)
        plt.imshow(img)
        plt.axis('off')
        if k==2 : plt.title('Mediana', plot_param)
        k += 5
    
    k = 4
    for img in IMGS[n:]:
        plt.subplot(n,5,k)
        plt.imshow(img)
        plt.axis('off')
        if k==4 : plt.title('Infectadas', plot_param)
        k += 5
    
    k = 5
    for img in IMGS_medianas[n:]:
        plt.subplot(n,5,k)
        plt.imshow(img)
        plt.axis('off')
        if k==5 : plt.title('Mediana', plot_param)
        k += 5
        
# Retira Medianas
IMGS_centralizadas = [IMGS[i]-IMGS_medianas[i] for i in range(2*n)]

if plotar:
    plt.figure(figsize=(15,9))
    
    k = 1
    for img in IMGS[:n]:
        plt.subplot(n,5,k)
        plt.imshow(img)
        plt.axis('off')
        if k==1 : plt.title('Não infectadas', plot_param)
        k += 5
        
    k = 2
    for img in IMGS_centralizadas[:n]:
        plt.subplot(n,5,k)
        plt.imshow(abs(img))
        plt.axis('off')
        if k==2 : plt.title('Centralizadas', plot_param)
        k += 5
    
    
    k = 4
    for img in IMGS[n:]:
        plt.subplot(n,5,k)
        plt.imshow(img)
        plt.axis('off')
        if k==4 : plt.title('Infectadas', plot_param)
        k += 5
        
    k = 5
    for img in IMGS_centralizadas[n:]:
        plt.subplot(n,5,k)
        plt.imshow(abs(img))
        plt.axis('off')
        if k==5 : plt.title('Centralizadas', plot_param)
        k += 5

# Separa em Partes Positivas e Negativas
IMGS_neg = [None]*(2*n)
IMGS_pos = [None]*(2*n)
for i in range(2*n):
    img_neg = -IMGS_centralizadas[i].copy()
    img_pos = IMGS_centralizadas[i].copy()
    img_neg[img_neg<0] = 0
    img_pos[img_pos<0] = 0
    IMGS_neg[i] = img_neg.copy()
    IMGS_pos[i] = img_pos.copy()

if plotar:
    plt.figure(figsize=(15,9))
    
    k = 1
    for img in IMGS_centralizadas[:n]:
        plt.subplot(n,7,k)
        plt.imshow(abs(img))
        plt.axis('off')
        if k==1 : plt.title('Centralizadas', plot_param)
        k += 7
        
    k = 2
    for img in IMGS_neg[:n]:
        plt.subplot(n,7,k)
        plt.imshow(img)
        plt.axis('off')
        if k==2 : plt.title('Negativas', plot_param)
        k += 7
    
    k = 3
    for img in IMGS_pos[:n]:
        plt.subplot(n,7,k)
        plt.imshow(img)
        plt.axis('off')
        if k==3 : plt.title('Positivas', plot_param)
        k += 7
    
    k = 5
    for img in IMGS_centralizadas[n:]:
        plt.subplot(n,7,k)
        plt.imshow(abs(img))
        plt.axis('off')
        if k==5 : plt.title('Centralizadas', plot_param)
        k += 7
        
    k = 6
    for img in IMGS_neg[n:]:
        plt.subplot(n,7,k)
        plt.imshow(img)
        plt.axis('off')
        if k==6 : plt.title('Negativas', plot_param)
        k += 7
    
    k = 7
    for img in IMGS_pos[n:]:
        plt.subplot(n,7,k)
        plt.imshow(img)
        plt.axis('off')
        if k==7 : plt.title('Positivas', plot_param)
        k += 7































