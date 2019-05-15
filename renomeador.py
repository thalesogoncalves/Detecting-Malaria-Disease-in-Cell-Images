'''
Name: Thales de Oliveira Goncalves
USP Number: 11383541
Course Code: SCC5830
Year/Semester: 2019/1
Final Project
'''

import os
flds = os.listdir('cell_images')

for fld in flds:
    fls = os.listdir('cell_images/' + str(fld))
    for i in range(len(fls)):
        os.rename('cell_images/'+str(fld)+'/'+fls[i] , 'cell_images/'+str(fld)+'/'+str(i)+'.png')
