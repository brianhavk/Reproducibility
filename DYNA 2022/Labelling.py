import matplotlib.pyplot as plt
import matplotlib.colors as pls
import numpy as np
import pybert as pb
import pygimli as pg

file = 'Linea-3 (Resistance of res2Dinv format).dat'

data = pb.importData(file)
data.markInvalid(data('r') < 0), data.removeInvalid()
data['k'] = pg.physics.ert.createGeometricFactors(data)
pg.physics.ert.ERTManager().checkData(data) #data['rhoa'] = data['r']*data['k']
data['err'] = pg.physics.ert.estimateError(data)

a = np.array(data['a']); b = np.array(data['b']); m = np.array(data['m']); n = np.array(data['n']); 
err = np.array(data['err']); i = np.array(data['i']); ip = np.array(data['ip']); ip1 = np.array(data['ip1']); 
ip2 = np.array(data['ip2']); ip3 = np.array(data['ip3']); ip4 = np.array(data['ip4']); ip5 = np.array(data['ip5']);
ip6 = np.array(data['ip6']); ip7 = np.array(data['ip7']); ip8 = np.array(data['ip8']); 
iperr = np.array(data['iperr']); k = np.array(data['k']); r = np.array(data['r']); rhoa = np.array(data['rhoa']); 
u = np.array(data['u']); valid = np.array(data['valid'])

information = np.zeros((348, 21))
information = np.vstack((a, b, m, n, err, i, ip, ip1, ip2, ip3, ip4, ip5, ip6, ip7, ip8, iperr, k, r, rhoa, u, valid))

'''########## Zoning ##########'''
Snrs_Value = np.array(data.sensorPositions()); Snrs_Value = Snrs_Value[:,0]
depth = np.zeros((1, 12))
copy = np.zeros((348, 21))

guide = np.zeros((0, 21)); k = 0
for i in range(0, 348):
    count = information[:,i]
    if(count[3]==0):
        guide = np.vstack((guide, count))
        k += 1
guide = np.delete(guide, (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 18, 20), axis = 1)

j = 0; k = 0
for i in range(348):
    count = information[:,i]
    if(count[0]==j+2 and count[1]==j+3 and count[2]==j+1 and count[3]==j):
        copy[k] = count
        j += 1; k += 1
    if i == 347:
        j = 0

for i in range(348):
    count = information[:,i]
    if(count[0]==j+4 and count[1]==j+5 and count[2]==j+1 and count[3]==j):
        copy[k] = count
        j += 1;  k += 1
    if i == 347:
        j = 0
 
for i in range(348):
    count = information[:,i]
    if(count[0]==j+6 and count[1]==j+7 and count[2]==j+1 and count[3]==j):
        copy[k] = count
        j += 1;  k += 1
    if i == 347:
        j = 0

for i in range(348):
    count = information[:,i]
    if(count[0]==j+8 and count[1]==j+9 and count[2]==j+1 and count[3]==j):
        copy[k] = count
        j += 1;  k += 1
    if i == 347:
        j = 0

for i in range(348):
    count = information[:,i]
    if(count[0]==j+4 and count[1]==j+6 and count[2]==j+2 and count[3]==j):
        copy[k] = count
        j += 1;  k += 1
    if i == 347:
        j = 0

for i in range(348):
    count = information[:,i]
    if(count[0]==j+8 and count[1]==j+10 and count[2]==j+2 and count[3]==j):
        copy[k] = count
        j += 1;  k += 1
    if i == 347:
        j = 0
 
for i in range(348):
    count = information[:,i]
    if(count[0]==j+12 and count[1]==j+14 and count[2]==j+2 and count[3]==j):
        copy[k] = count
        j += 1;  k += 1
    if i == 347:
        j = 0
     
for i in range(348):
    count = information[:,i]
    if(count[0]==j+16 and count[1]==j+18 and count[2]==j+2 and count[3]==j):
        copy[k] = count
        j += 1;  k += 1
    if i == 347:
        j = 0

for i in range(348):
    count = information[:,i]
    if(count[0]==j+6 and count[1]==j+9 and count[2]==j+3 and count[3]==j):
        copy[k] = count
        j += 1;  k += 1
    if i == 347:
        j = 0        
    
for i in range(348):
    count = information[:,i]
    if(count[0]==j+12 and count[1]==j+15 and count[2]==j+3 and count[3]==j):
        copy[k] = count
        j += 1;  k += 1
    if i == 347:
        j = 0

for i in range(348):
    count = information[:,i]
    if(count[0]==j+18 and count[1]==j+21 and count[2]==j+3 and count[3]==j):
        copy[k] = count
        j += 1;  k += 1
    if i == 347:
        j = 0

for i in range(348):
    count = information[:,i]
    if(count[0]==j+24 and count[1]==j+27 and count[2]==j+3 and count[3]==j):
        copy[k] = count
        j += 1;  k += 1
    if i == 347:
        j = 0

data['a'] = pg.Vector(copy[:,0]); data['b'] = pg.Vector(copy[:,1])
data['m'] = pg.Vector(copy[:,2]); data['n'] = pg.Vector(copy[:,3])
data['err'] = pg.Vector(copy[:,4]); data['i'] = pg.Vector(copy[:,5])
data['ip'] = pg.Vector(copy[:,6]); data['ip1'] = pg.Vector(copy[:,7])
data['ip2'] = pg.Vector(copy[:,8]); data['ip3'] = pg.Vector(copy[:,9])
data['ip4'] = pg.Vector(copy[:,10]); data['ip5'] = pg.Vector(copy[:,11])
data['ip6'] = pg.Vector(copy[:,12]); data['ip7'] = pg.Vector(copy[:,13])
data['ip8'] = pg.Vector(copy[:,14]); data['iperr'] = pg.Vector(copy[:,15])
data['k'] = pg.Vector(copy[:,16]); data['r'] = pg.Vector(copy[:,17])
data['rhoa'] = pg.Vector(copy[:,18]); data['u'] = pg.Vector(copy[:,19])
data['valid'] = pg.Vector(copy[:,20])
data.save('Linea-3 (Resistance of unified data format).dat')

'''##########  Depth  ##########'''
for i in range(12):
    for j in range(4):
        guide[i, j] = Snrs_Value[int(guide[i, j])]
        
depth = np.zeros((12,))
for i in range(12):
    depth[i] = (guide[i, 1]-guide[i, 3])*0.25
depth_ticks = []
for i in range(len(depth)):
    depth_ticks.append(i)
depth.sort() 
depth_labels = ["%.1f" % i for i in depth]

def getABMN(scheme, idx):
    """ Get coordinates of four-point cfg with id `idx` from DataContainerERT
    `scheme`."""
    coords = {}
    for elec in "abmn":
        elec_id = int(scheme(elec)[idx])
        elec_pos = scheme.sensorPosition(elec_id)
        coords[elec] = elec_pos.x(), elec_pos.y()
    return coords


def plotABMN(ax, scheme, idx):
    """ Visualize four-point configuration on given axes. """
    coords = getABMN(scheme, idx)
    for elec in coords:
        x, y = coords[elec]
        if elec in "ab":
            color = "red"
        else:
            color = "blue"
        ax.plot(x, y, marker=".", color=color, ms=5)
        ax.annotate(elec.upper(), xy=(x, y), size=12, ha="center", fontsize=8, bbox=dict(
            boxstyle="round", fc=(0.8, 0.8, 0.8), ec=color), xytext=(0, 15),
                    textcoords='offset points', arrowprops=dict(
                        arrowstyle="wedge, tail_width=.5", fc=color, ec=color,
                        patchA=None, alpha=0.75))
        ax.plot(coords["a"][0],)

figure, axis =plt.subplots(1, 1, figsize=(10, 5))
#idx = 1
#plotABMN(axis, data, idx)

axis, cbar = pg.physics.ert.show(data, ax=axis, orientation='vertical', 
                                 location='right', cMin=5.82, cMax=3120)

cbar.ax.tick_params(labelsize=15)
cbar.set_label(label='Apparent Resistivity ($\Omega$m)', size=15)

axis.set_ylabel('Depth (m)', size=15)
axis.set_yticks(depth_ticks)
axis.set_yticklabels(depth_labels, fontsize=15)

abscissas = [0, 25, 50, 75, 100, 125, 150, 175, 200]
depth_labels = ['0', '25', '50', '75', '100', '125', '150', '175', '200']
axis.set_xlabel('Surface Position (m)', size=15)
axis.set_xticks(abscissas)
axis.set_xticklabels(depth_labels, fontsize=15)