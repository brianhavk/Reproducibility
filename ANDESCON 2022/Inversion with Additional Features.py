from pygimli.physics import ert

font_bar = {'family': 'serif',
            'color':  'black',
            'weight': 'medium',
            'size': 12,
            }

mgr = ert.ERTManager('simple.dat')

inv = mgr.invert(lam=3.6, paraMaxCellSize=0.1, paraDepth=8, 
                 robustData=True, verbose=True, maxIter=3)

ax, colorbar = mgr.showResult(cMin=25, cMax=150)
colorbar.set_label("Apparent Resistivity [$\Omega$m]", fontdict=font_bar)