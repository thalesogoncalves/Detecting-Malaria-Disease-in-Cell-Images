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
from ccc import clc, clear
clc(); exec(clear())

# Randomize n images of each class e shows each step of the processing with the parameters already adjusted
n = 4
plot_param = {'fontsize' : 15, 'fontweight' : "bold"}
classes = ['0 - Uninfected' , '1 - Parasitized']
path = 'G:/Thales/Documents/Acadêmico/Doutorado/Processamento de Imagem/Trabalho Final/cell_images'

N0 = len(os.listdir(path + '/' + classes[0]))-1
N1 = len(os.listdir(path + '/' + classes[1]))-1
N0_samples = [num for num in np.random.randint(int(0.9*N0),N0+1,n)]
N1_samples = [num for num in np.random.randint(int(0.9*N1),N1+1,n)]
IMGS_path = [path + '/' + classes[0] + '/' + str(num) + '.png' for num in N0_samples] +\
            [path + '/' + classes[1] + '/' + str(num) + '.png' for num in N1_samples]         
IMGS = [np.array(imageio.imread(img_path))/255 for img_path in IMGS_path]


plt.figure(figsize=(15,9))

k = 1
for img in IMGS[:n]:
    plt.subplot(n,3,k)
    plt.imshow(img)
    plt.axis('off')
    if k==1 : plt.title('Uninfected', plot_param)
    k += 3
    
k = 3
for img in IMGS[n:]:
    plt.subplot(n,3,k)
    plt.imshow(img)
    plt.axis('off')
    if k==3 : plt.title('Parasitized', plot_param)
    k += 3
        
        
# Calculate Medians
IMGS_medianas = [np.zeros(np.shape(img)) for img in IMGS]
for i in range(2*n):
    img = IMGS[i].copy()
    pos = np.where(np.sum(img,2)!=0)
    for j in range(3):
        camada = img[:,:,j]
        camada[pos] = np.median(camada[pos])
    IMGS_medianas[i] = img.copy()


plt.figure(figsize=(15,9))

k = 1
for img in IMGS[:n]:
    plt.subplot(n,5,k)
    plt.imshow(img)
    plt.axis('off')
    if k==1 : plt.title('Uninfected', plot_param)
    k += 5

k = 2
for img in IMGS_medianas[:n]:
    plt.subplot(n,5,k)
    plt.imshow(img)
    plt.axis('off')
    if k==2 : plt.title('Median', plot_param)
    k += 5

k = 4
for img in IMGS[n:]:
    plt.subplot(n,5,k)
    plt.imshow(img)
    plt.axis('off')
    if k==4 : plt.title('Parasitized', plot_param)
    k += 5

k = 5
for img in IMGS_medianas[n:]:
    plt.subplot(n,5,k)
    plt.imshow(img)
    plt.axis('off')
    if k==5 : plt.title('Median', plot_param)
    k += 5
        
# Subtract Images From Their Medians
IMGS_centralizadas = [IMGS[i]-IMGS_medianas[i] for i in range(2*n)]


plt.figure(figsize=(15,9))

k = 1
for img in IMGS[:n]:
    plt.subplot(n,5,k)
    plt.imshow(img)
    plt.axis('off')
    if k==1 : plt.title('Uninfected', plot_param)
    k += 5
    
k = 2
for img in IMGS_centralizadas[:n]:
    plt.subplot(n,5,k)
    plt.imshow(abs(img))
    plt.axis('off')
    if k==2 : plt.title('Centralized', plot_param)
    k += 5


k = 4
for img in IMGS[n:]:
    plt.subplot(n,5,k)
    plt.imshow(img)
    plt.axis('off')
    if k==4 : plt.title('Parasitized', plot_param)
    k += 5
    
k = 5
for img in IMGS_centralizadas[n:]:
    plt.subplot(n,5,k)
    plt.imshow(abs(img))
    plt.axis('off')
    if k==5 : plt.title('Centralized', plot_param)
    k += 5

# Separate in Positive and Negative Parts
IMGS_neg = [None]*(2*n)
IMGS_pos = [None]*(2*n)
for i in range(2*n):
    img_neg = -IMGS_centralizadas[i].copy()
    img_pos = IMGS_centralizadas[i].copy()
    img_neg[img_neg<0] = 0
    img_pos[img_pos<0] = 0
    IMGS_neg[i] = img_neg.copy()
    IMGS_pos[i] = img_pos.copy()


plt.figure(figsize=(15,9))

k = 1
for img in IMGS_centralizadas[:n]:
    plt.subplot(n,7,k)
    plt.imshow(abs(img))
    plt.axis('off')
    if k==1 : plt.title('Centralized', plot_param)
    k += 7
    
k = 2
for img in IMGS_neg[:n]:
    plt.subplot(n,7,k)
    plt.imshow(img)
    plt.axis('off')
    if k==2 : plt.title('Negative', plot_param)
    k += 7

k = 3
for img in IMGS_pos[:n]:
    plt.subplot(n,7,k)
    plt.imshow(img)
    plt.axis('off')
    if k==3 : plt.title('Positive', plot_param)
    k += 7

k = 5
for img in IMGS_centralizadas[n:]:
    plt.subplot(n,7,k)
    plt.imshow(abs(img))
    plt.axis('off')
    if k==5 : plt.title('Centralized', plot_param)
    k += 7
    
k = 6
for img in IMGS_neg[n:]:
    plt.subplot(n,7,k)
    plt.imshow(img)
    plt.axis('off')
    if k==6 : plt.title('Negative', plot_param)
    k += 7

k = 7
for img in IMGS_pos[n:]:
    plt.subplot(n,7,k)
    plt.imshow(img)
    plt.axis('off')
    if k==7 : plt.title('Positive', plot_param)
    k += 7

# Coloring Thresholding
T = 0.0725490196078431 # = 18.5/255 (no report está 0.073)

IMGS_filtradas = [img.copy() for img in IMGS_neg]
for i in range(2*n):
    pos = np.where(np.sqrt(np.sum(IMGS_neg[i]**2,2))<T)
    for j in range(3):
        camada = IMGS_filtradas[i][:,:,j]
        camada[pos] = 0


plt.figure(figsize=(15,9))

k = 1
for img in IMGS_neg[:n]:
    plt.subplot(n,7,k)
    plt.imshow(abs(img))
    plt.axis('off')
    if k==1 : plt.title('Negative', plot_param)
    k += 7
    
k = 2
for img in IMGS_neg[:n]:
    plt.subplot(n,7,k)
    plt.imshow(np.clip(img*5,0,1))
    plt.axis('off')
    if k==2 : plt.title('In Other Scale', plot_param)
    k += 7

k = 3
for img in IMGS_filtradas[:n]:
    plt.subplot(n,7,k)
    plt.imshow(np.clip(img*5,0,1))
    plt.axis('off')
    if k==3 : plt.title('Filtered', plot_param)
    k += 7

k = 5
for img in IMGS_neg[n:]:
    plt.subplot(n,7,k)
    plt.imshow(abs(img))
    plt.axis('off')
    if k==5 : plt.title('Negative', plot_param)
    k += 7
    
k = 6
for img in IMGS_neg[n:]:
    plt.subplot(n,7,k)
    plt.imshow(np.clip(img*5,0,1))
    plt.axis('off')
    if k==6 : plt.title('In Other Scale', plot_param)
    k += 7

k = 7
for img in IMGS_filtradas[n:]:
    plt.subplot(n,7,k)
    plt.imshow(np.clip(img*5,0,1))
    plt.axis('off')
    if k==7 : plt.title('Filtered', plot_param)
    k += 7

# Classification by Thresholding
T = 36.70535787931294 # (no report está 36.71)

IMGS_scores = np.array([np.sum(np.sqrt(np.sum(img**2,2))) for img in IMGS_filtradas])
IMGS_labels = IMGS_scores>T


plt.figure(figsize=(15,9))
i=0

k = 1
for img in IMGS[:n]:
    plt.subplot(n,3,k)
    plt.imshow(img)
    plt.axis('off')
    titulo = 'Infectada' if IMGS_labels[i] else 'Não Infectada'
    titulo += ' (' + str(round(IMGS_scores[i],2)) + ')'
    plt.title(titulo)
    i+=1
    k += 3


k = 3
for img in IMGS[n:]:
    plt.subplot(n,3,k)
    plt.imshow(img)
    plt.axis('off')
    titulo = 'Infectada' if IMGS_labels[i] else 'Não Infectada'
    titulo += ' (' + str(round(IMGS_scores[i],2)) + ')'
    plt.title(titulo)
    i+=1
    k += 3























