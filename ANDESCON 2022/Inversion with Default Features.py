from pygimli.physics import ert

font_bar = {'family': 'serif',
            'color':  'black',
            'weight': 'medium',
            'size': 12,
            }

mgr = ert.ERTManager('simple.dat', sr=False, useBert=True, 
                     debug=False, verbose=True)

inv = mgr.invert(lam=0.85)

ax, colorbar = mgr.showResult(cMin=25, cMax=150)
ax.set_ylim(-8, 0)
colorbar.set_label("Apparent Resistivity [$\Omega$m]", fontdict=font_bar)