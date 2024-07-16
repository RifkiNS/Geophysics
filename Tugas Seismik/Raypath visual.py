import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

Z = np.array(([1000,1000,1000,1000],
            [1000,200,200,1000],
            [1000,200,200,1000],
            [1000,1000,1000,1000]))

verts = np.array (([1., 1.],
[1., 3.],
[3., 3.],
[3., 1.],
[1., 1.],
))

codes = [
    Path.MOVETO,
    Path.LINETO,
    Path.LINETO,
    Path.LINETO,
    Path.CLOSEPOLY,
]

path = Path(verts, codes)


rays1 = [
    (0., 0.5),
    (4., 1.),

    (0., 0.5),
    (4., 2.),

    (0., 0.5),
    (4., 3.),
]

codesrays1 = [
    Path.MOVETO,
    Path.LINETO,
    
    Path.MOVETO,
    Path.LINETO,

    Path.MOVETO,
    Path.LINETO,
]

rays2 = [
    (0., 1.5),
    (4., 1.),

    (0., 1.5),
    (4., 2.),

    (0., 1.5),
    (4., 3.),
]

codesrays2 = [
    Path.MOVETO,
    Path.LINETO,
    
    Path.MOVETO,
    Path.LINETO,

    Path.MOVETO,
    Path.LINETO,
]

rays3 = [
    (0., 2.5),
    (4., 1.),

    (0., 2.5),
    (4., 2.),

    (0., 2.5),
    (4., 3.),
]

codesrays3 = [
    Path.MOVETO,
    Path.LINETO,
    
    Path.MOVETO,
    Path.LINETO,

    Path.MOVETO,
    Path.LINETO,
]

rays4 = [
    (0., 3.5),
    (4., 1.),

    (0., 3.5),
    (4., 2.),

    (0., 3.5),
    (4., 3.),
]

codesrays4 = [
    Path.MOVETO,
    Path.LINETO,
    
    Path.MOVETO,
    Path.LINETO,

    Path.MOVETO,
    Path.LINETO,
]

raypaths1 = Path(rays1, codesrays1)
raypaths2 = Path(rays2, codesrays2)
raypaths3 = Path(rays3, codesrays3)
raypaths4 = Path(rays4, codesrays4)

grid = [
    (1., 0.),
    (1., 4.),

    (2., 0.),
    (2., 4.),

    (3., 0.),
    (3., 4.),

    (4., 0.),
    (4., 4.),

    (0., 1.),
    (4., 1.),

    (0., 2.),
    (4., 2.),

    (0., 3.),
    (4., 3.),

    (0., 4.),
    (4., 4.),
]

codesgrid = [
    Path.MOVETO,
    Path.LINETO,

    Path.MOVETO,
    Path.LINETO,

    Path.MOVETO,
    Path.LINETO,

    Path.MOVETO,
    Path.LINETO,

    Path.MOVETO,
    Path.LINETO,

    Path.MOVETO,
    Path.LINETO,

    Path.MOVETO,
    Path.LINETO,

    Path.MOVETO,
    Path.LINETO,
]

gridpath = Path(grid, codesgrid)

fix,ax = plt.subplots()
patch = patches.PathPatch(path, facecolor='red', lw=2)
patch1 = patches.PathPatch(raypaths1, edgecolor='blue', lw=2)
patch2 = patches.PathPatch(raypaths2, edgecolor='green', lw=2)
patch3 = patches.PathPatch(raypaths3, edgecolor='white', lw=2)
patch4 = patches.PathPatch(raypaths4, edgecolor='orange', lw=2)
patch5 = patches.PathPatch(gridpath, edgecolor='black', lw=1)

ax.add_patch(patch)
ax.add_patch(patch1)
ax.add_patch(patch2)
ax.add_patch(patch3)
ax.add_patch(patch4)
ax.add_patch(patch5)

xs1, ys1 = zip(*rays1)
xs2, ys2 = zip(*rays2)
xs3, ys3 = zip(*rays3)
xs4, ys4 = zip(*rays4)

ax.plot(xs1, ys1, 'o', color='black', ms=10)
ax.plot(xs2, ys2, 'o', color='black', ms=10)
ax.plot(xs3, ys3, 'o', color='black', ms=10)
ax.plot(xs4, ys4, 'o', color='black', ms=10)

ax.text(0.4, 0.6, 'V1')
ax.text(1.4, 0.6, 'V2')
ax.text(2.4, 0.6, 'V3')
ax.text(3.4, 0.6, 'V4')
ax.text(0.4, 1.6, 'V5')
ax.text(1.4, 1.6, 'V6')
ax.text(2.4, 1.6, 'V7')
ax.text(3.4, 1.6, 'V8')
ax.text(0.4, 2.6, 'V9')
ax.text(1.4, 2.6, 'V10')
ax.text(2.4, 2.6, 'V11')
ax.text(3.4, 2.6, 'V12')
ax.text(0.4, 3.6, 'V13')
ax.text(1.4, 3.6, 'V14')
ax.text(2.4, 3.6, 'V15')
ax.text(3.4, 3.6, 'V16')

ax.text(0 , 0.5, 'S1', fontsize=16)
ax.text(0 , 1.5, 'S2', fontsize=16)
ax.text(0 , 2.5, 'S3', fontsize=16)
ax.text(0 , 3.5, 'S4', fontsize=16)

ax.text(4 , 1.1, 'R1', fontsize=16)
ax.text(4 , 2.1, 'R2', fontsize=16)
ax.text(4 , 3.1, 'R3', fontsize=16)

im = ax.imshow(Z, extent=[0, 4, 0, 4])
ax.set_title('Crosshole Tomography')
ax.set_xlabel('Jarak (x10^2 meter) ')
ax.set_ylabel('Kedalaman (x10^2 meter')
ax.invert_yaxis()
plt.show()

#Menghitung Panjang Ray
deltax=1
deltay=1

#Menghitung Ray Source 1 ke Receiver 1
R1S1 = np.sqrt(xs1[1]**2+(ys1[1]-ys1[0])**2)

R1d = R1S1*deltax/xs1[1]
R1e = R1S1*2*deltax/xs1[1]
R1f = R1S1*3*deltax/xs1[1]

de = ((R1S1*2*deltax)-(R1d*xs1[1]))/xs1[1]
ef = ((R1S1*3*deltax)-(R1e*xs1[1]))/xs1[1]
fS1 = R1S1 - (R1d+de+ef)

