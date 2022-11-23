import matplotlib.pyplot as plt
import matplotlib.colors as pls
import numpy as np
import pygimli as pg

data = pg.load('Dataset.dat')
manager =  pg.physics.ert.ERTManager(sr=False, useBert=True, debug=False, verbose=True)
inversion = manager.invert(data, lam=0.8, paraMaxCellSize=1, paraDepth=33.75, 
                           maxIter=6, paraBoundary=0, robustData=True)

'''Mapa de Caracterización'''
characterization_map = np.zeros((311418, 4))
azul = np.array([0.21568627, 0.49411765, 0.72156863, 1])
verde = np.array([0.30196078, 0.68627451, 0.29019608, 1])
amarillo = np.array([1, 1, 0.2, 1])
cafe = np.array([0.65098039, 0.3372549, 0.15686275, 1])
marron= np.array([0.90196078, 0.67058824, 0.00784314, 1])
rojo = np.array([0.89411765, 0.10196078, 0.10980392, 1])

#Conglomerados
characterization_map[:3418, :] = rojo
characterization_map[5418:6418, :] = rojo

#Arcilla arenosa
characterization_map[3418:5418, :] = marron

#Arena
characterization_map[6418:8418, :] = cafe

#Arena arcillosa
characterization_map[8418:24418, :] = amarillo

#Materia orgánica
characterization_map[24418:, :] = verde

characterization_map = pls.ListedColormap(characterization_map)

figure, axes = plt.subplots(1, 1, figsize=(10,5))

axis, cbar = manager.showResult(ax=axes, cMap=characterization_map, cMin=5.82, cMax=3120, logScale=False)
axis.set_title('Characterization')
axis.set_ylim(-24, 0)
#cbar.set_ticks([10, 30, 50, 137.5, 236])
#cbar.set_ticklabels(['Clay', 'Clay-Sand', 'Sand-Clay', 'Conglomered', 'Topsoil'])

plt.tight_layout(w_pad=1.0, h_pad=5.0)
# plt.savefig('Pictures/Linea-3 (Resistance 1).jpeg', bbox_inches="tight")
