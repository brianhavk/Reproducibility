# -*- coding: utf-8 -*-
"""
2D ERT modeling and inversion
-----------------------------
"""
# sphinx_gallery_thumbnail_number = 6

# One fontdict
font_bar = {'family': 'serif',
            'color':  'black',
            'weight': 'medium',
            'size': 12,
            }

import numpy as np

import pygimli as pg
import pygimli.meshtools as mt
from pygimli.physics import ert
###############################################################################
# Create geometry definition for the modelling domain.
#
# worldMarker=True indicates the default boundary conditions for the ERT
world = mt.createWorld(start=[-50, 0], end=[50, -50], layers=[-1, -5],
                       worldMarker=True)

###############################################################################
# Create some heterogeneous circular anomaly
block = mt.createCircle(pos=[-5, -3.], radius=[4, 1], marker=4,
                        boundaryMarker=10, area=0.1)

###############################################################################
poly = mt.createPolygon([(1,-4), (2,-1.5), (4,-2), (5,-2),
                         (8,-3), (5,-3.5), (3,-4.5)], isClosed=True,
                         addNodes=3, interpolate='spline', marker=5)

###############################################################################
# Merge geometry definition into a Piecewise Linear Complex (PLC)
geom = world + block + poly

###############################################################################
# Create a Dipole Dipole ('dd') measuring scheme with 21 electrodes.
scheme = ert.createData(elecs=np.linspace(start=-15, stop=15, num=21),
                           schemeName='dd')

###############################################################################
# Put all electrode (aka sensors) positions into the PLC to enforce mesh
# refinement. Due to experience, its convenient to add further refinement
# nodes in a distance of 10% of electrode spacing to achieve sufficient
# numerical accuracy.
for p in scheme.sensors():
    geom.createNode(p)
    geom.createNode(p - [0, 0.1])

# Create a mesh for the finite element modelling with appropriate mesh quality.
mesh = mt.createMesh(geom, quality=34)

# Create a map to set resistivity values in the appropriate regions
# [[regionNumber, resistivity], [regionNumber, resistivity], [...]
rhomap = [[1, 100.],
          [2, 75.],
          [3, 50.],
          [4, 150.],
          [5, 25]]

###############################################################################
# Perform the modeling with the mesh and the measuring scheme itself
# and return a data container with apparent resistivity values,
# geometric factors and estimated data errors specified by the noise setting.
# The noise is also added to the data. Here 1% plus 1µV.
# Note, we force a specific noise seed as we want reproducable results for
# testing purposes.
data = ert.simulate(mesh, scheme=scheme, res=rhomap, noiseLevel=1,
                    noiseAbs=1e-6, seed=1337)

pg.info(np.linalg.norm(data['err']), np.linalg.norm(data['rhoa']))
pg.info('Simulated data', data)
pg.info('The data contains:', data.dataMap().keys())

pg.info('Simulated rhoa (min/max)', min(data['rhoa']), max(data['rhoa']))
pg.info('Selected data noise %(min/max)', min(data['err'])*100, max(data['err'])*100)

###############################################################################
# Optional: you can filter all values and tokens in the data container.
# Its possible that there are some negative data values due to noise and
# huge geometric factors. So we need to remove them.
data.remove(data['rhoa'] < 0)
pg.info('Filtered rhoa (min/max)', min(data['rhoa']), max(data['rhoa']))

# You can save the data for further use
data.save('simple.dat')

# You can take a look at true model
ax1, cb1 = pg.show(mesh, rhomap, hold=True, cMap="Spectral_r", logScale=True,
        cMin=25, cMax=150)
ax1.set_xlim(-18, 18)
ax1.set_ylim(-8, 0)
cb1.set_label("Apparent Resistivity [$\Omega$m]", fontdict=font_bar)
###############################################################################
# Initialize the ERTManager, e.g. with a data container or a filename.
mgr = ert.ERTManager('simple.dat')
###############################################################################
# Run the inversion with the preset data. The Inversion mesh will be created
# with default settings.
inv = mgr.invert(lam=20, paraDepth=8, verbose=True)

###############################################################################
# Let the ERTManger show you the model of the last successful run and how it
# fits the data. Shows model response.
ax2, cb2 = mgr.showResult(cMin=25, cMax=150)
cb2.set_label("Apparent Resistivity [$\Omega$m]", fontdict=font_bar)