import pybert as pb
import pygimli as pg

data = pb.import("linea-3.dat")
data['k'] = pg.physics.ert.createGeometricFactors(data)
data['rhoa'] = data['r']*data['k']
data['err'] = pg.physics.ert.estimateError(data)

manager = pg.physics.ert.ERTManager(data, sr=True, verbose = True)
inversion = manager.invert(lam=5, paraMaxCellSize=1, 
paraDepth=33.8, paraBoundary=0, robustData=True)
manager.showResult(cMin=5.82, cMax=3120)
