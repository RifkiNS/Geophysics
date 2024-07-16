import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

# Nilai Z kecepatan
def Z():
    Z = np.array(([1000,1000,1000,1000],
            [1000,200,200,1000],
            [1000,200,200,1000],
            [1000,1000,1000,1000]))
    return Z 

Z()


verts = np.array(([1., 1.],
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

im = ax.imshow(Z(), extent=[0, 4, 0, 4])
ax.set_title('Crosshole Tomography')
ax.set_xlabel('Jarak (x10^2 meter) ')
ax.set_ylabel('Kedalaman (x10^2 meter')
ax.invert_yaxis()
plt.show()

#Menghitung Panjang Ray
l_r = np.zeros((12, 16))
   
deltax=1
deltay=1

#Menghitung Ray Source 1 ke Receiver 1     
R1S1 = np.sqrt(xs1[1]**2+(ys1[1]-ys1[0])**2)   
 
R1d = R1S1*deltax/xs1[1] 
R1e = R1S1*2*deltax/xs1[1] 
R1f = R1S1*3*deltax/xs1[1]

ab = ((R1S1*2*deltax)-(R1d*xs1[1]))/xs1[1]
bc = ((R1S1*3*deltax)-(R1e*xs1[1]))/xs1[1]   
cS1 = R1S1 - (R1d+ab+bc)

#Menghitung Ray Source 1 Ke Receiver 2   
R2S1 = np.sqrt(xs1[3]**2+(ys1[3]-ys1[2])**2)

R2d = R2S1*deltax/xs1[3]   
R2e = R2S1*2*deltax/xs1[3] 
R2f = R2S1*3*deltax/xs1[3] 
 
de = ((R2S1*2*deltax)-(R2d*xs1[3]))/xs1[3]
ef = ((R2S1*3*deltax)-(R2e*xs1[3]))/xs1[3]
fS1 = R2S1 - (R2d+de+ef)

g_z = xs1[3]*(ys1[1]-ys1[0])/(ys1[1]+ys1[0])
g_S1 = R2S1*g_z/xs1[3]   
g_h = g_S1-fS1
g_g = ef-g_h

#Menghitung Ray Source 1 Ke Receiver 3   
R3S1 = np.sqrt(xs1[5]**2+(ys1[5]-ys1[4])**2)

R3d = R3S1*deltax/xs1[5]   
R3e = R3S1*2*deltax/xs1[5] 
R3f = R3S1*3*deltax/xs1[5]

hi = ((R3S1*2*deltax)-(R3d*xs1[5]))/xs1[5]
ij = ((R3S1*3*deltax)-(R3e*xs1[5]))/xs1[5]
jS1 = R3S1 - (R3d+ij+hi)

k_z = xs1[5]*(ys1[1]-ys1[0])/(ys1[3]+ys1[0])
k_S1 = R3S1*k_z/xs1[5]   
j_k = jS1-k_S1 

l_z = xs1[5]*(ys1[3]-ys1[0])/(ys1[3]+ys1[0])
l_S1 = R3S1*l_z/xs1[5]   
l_h = l_S1-(ij+jS1)
l_g = hi-l_h
        
l_r[0][0] = cS1
l_r[0][1] = bc
l_r[0][2] = ab
l_r[0][3] = R1d
l_r[1][0] = fS1
l_r[1][1] = g_h
l_r[1][5] = g_g
l_r[1][6] = de
l_r[1][7] = R2d
l_r[2][0] = k_S1
l_r[2][4] = j_k
l_r[2][5] = ij
l_r[2][6] = l_h
l_r[2][10] = l_g
l_r[2][11] = R3d
l_r[9][6] = R3d
l_r[9][7] = l_g
l_r[9][8] = l_h
l_r[9][9] = ij
l_r[9][10] = j_k
l_r[9][12] = k_S1
l_r[10][9] = R2d
l_r[10][10] = de
l_r[10][11] = g_g
l_r[10][12] = g_h
l_r[10][13] = fS1
l_r[11][12] = R1d
l_r[11][13] = ab
l_r[11][14] = bc
l_r[11][15] = cS1

#Menghitung Ray Source 2 ke Reciever 1   
R1S2 = np.sqrt(xs2[1]**2+(ys2[1]-ys2[0])**2)   
 
R1m = R1S2*deltax/xs2[1] 
R1n = R1S2*2*deltax/xs2[1] 
R1o = R1S2*3*deltax/xs2[1]

mn = ((R1S2*2*deltax)-(R1m*xs2[1]))/xs2[1]
no = ((R1S2*3*deltax)-(R1n*xs2[1]))/xs2[1]   
oS2 = R1S2 - (R1m+mn+no)

#Menghitung Ray Source 2 ke Reciever 2   
R2S2 = np.sqrt (xs2[3]**2+(ys2[3]-ys2[2])**2)

R2m = R2S2*deltax/xs2[3]   
R2n = R2S2*2*deltax/xs2[3] 
R2o = R2S2*3*deltax/xs2[3] 
 
pq = ((R2S2*2*deltax)-(R2m*xs2[3]))/xs2[3]
qr = ((R2S2*3*deltax)-(R2n*xs2[3]))/xs2[3]
rS2 = R2S2 - (R2m+pq+qr)

#Menghitung Ray Source 2 ke Reciever 3   
R3S2 = np.sqrt(xs2[5]**2+(ys2[5]-ys2[4])**2)

R3m = R3S2*deltax/xs2[5]   
R3n = R3S2*2*deltax/xs2[5] 
R3o = R3S2*3*deltax/xs2[5]

st = ((R3S2*2*deltax)-(R3m*xs2[5]))/xs2[5]
tu = ((R3S2*3*deltax)-(R3n*xs2[5]))/xs2[5]
uS2 = R3S2 - (R3m+tu+st)

u_z = xs2[3]*(ys2[3]-ys2[2])/(ys2[5]-ys2[0])
u_S2 = R3S2*u_z/xs2[5]
u_h = u_S2-uS2
u_g= tu-u_h

l_r[3][4] = oS2
l_r[3][5] = no
l_r[3][6] = mn
l_r[3][7] = R1m
l_r[4][4] = rS2
l_r[4][5] = qr
l_r[4][6] = pq
l_r[4][7] = R2m
l_r[5][4] = uS2
l_r[5][5] = u_h  
l_r[5][9] = u_g  
l_r[5][10] = st
l_r[5][11] = R3m
l_r[6][5] = R3m
l_r[6][6] = st
l_r[6][7] = u_g
l_r[6][8] = u_h
l_r[6][9] = uS2
l_r[7][8] = R2m
l_r[7][9] = pq
l_r[7][10] = qr
l_r[7][11] = rS2
l_r[8][8] = R1m
l_r[8][9] = mn
l_r[8][10] = no
l_r[8][11] = oS2

panjang = np.dot(100,l_r)
for i in range(12):
  for j in range(16):
    if panjang[i][j]!=0:
      print(panjang[i][j])

v = np.array(([200,200,200,200],
   [200,3000,3000,200],
   [200,3000,3000,200],
   [200,200,200,200]))

s = 1/v
#tcal
t11 = 100.7*s[0][0]+100.7*s[0][1]+100.7*s[0][2]+100.7*s[0][3]
t12 = 106.8*s[0][0]+35.6*s[0][1]+71.2*s[1][1]+106.8*s[1][2]+106.8*s[1][3]
t13 = 94.33*s[0][0]+23.5*s[0][1]+117.9*s[1][1]+47.1*s[1][2]+70.7*s[2][2]+117.9*s[2][3]
t21 = 100.7*s[1][0]+100.7*s[1][1]+100.7*s[1][2]+100.7*s[1][3]
t22 = 100.7*s[1][0]+100.7*s[1][1]+100.7*s[1][2]+100.7*s[1][3]
t23 = 106.8*s[1][0]+35.6*s[1][1]+71.2*s[2][1]+106.8*s[2][2]+106.8*s[2][3]
t31 = 106.8*s[2][0]+35.6*s[2][1]+71.2*s[1][1]+106.8*s[1][2]+106.8*s[1][3]
t32 = 100.7*s[2][0]+100.7*s[2][1]+100.7*s[2][2]+100.7*s[2][3]
t33 = 100.7*s[2][0]+100.7*s[2][1]+100.7*s[2][2]+100.7*s[2][3]
t41 = 94.33*s[3][0]+23.5*s[2][0]+117.9*s[2][1]+47.1*s[2][2]+70.7*s[1][2]+117.9*s[1][3]
t42 = 106.8*s[3][0]+35.6*s[3][1]+71.2*s[2][1]+106.8*s[2][2]+106.8*s[2][3]
t43 = 100.7*s[3][0]+100.7*s[3][1]+100.7*s[3][2]+100.7*s[3][3]

tcal = np.array(([t11,t12,t13,t21,t22,t23,t31,t32,t33,t41,t42,t43]))

print(v)
print(tcal)

# matriks G
G = np.zeros((len(tcal), 16))
G[0][0]=100.7782219
G[0][1]=100.7782219
G[0][2]=100.7782219
G[0][3]=100.7782219
G[1][0]=106.8000468
G[1][1]=35.60001561
G[1][5]=71.20003121
G[1][6]=106.8000468
G[1][7]=106.8000468
G[2][0]=94.33981132
G[2][4]=23.58495283
G[2][5]=117.9247642
G[2][6]=47.16990566
G[2][10]=70.75485849
G[2][11]=117.9247642
G[3][4]=100.7782219
G[3][5]=100.7782219
G[3][6]=100.7782219
G[3][7]=100.7782219
G[4][4]=100.7782219
G[4][5]=100.7782219
G[4][6]=100.7782219
G[4][7]=100.7782219
G[5][4]=106.8000468
G[5][5]=35.60001561
G[5][9]=71.20003121
G[5][10]=106.8000468
G[5][11]=106.8000468
G[6][5]=106.8000468
G[6][6]=106.8000468
G[6][7]=71.20003121
G[6][8]=35.60001561
G[6][9]=106.8000468
G[7][8]=100.7782219
G[7][9]=100.7782219
G[7][10]=100.7782219
G[7][11]=100.7782219
G[8][8]=100.7782219
G[8][9]=100.7782219
G[8][10]=100.7782219
G[8][11]=100.7782219
G[9][6]=117.9247642
G[9][7]=70.75485849
G[9][8]=47.16990566
G[9][9]=117.9247642
G[9][10]=23.58495283
G[9][12]=94.33981132
G[10][9]=106.8000468
G[10][10]=106.8000468
G[10][11]=71.20003121
G[10][12]=35.60001561
G[10][13]=106.8000468
G[11][12]=100.7782219
G[11][13]=100.7782219
G[11][14]=100.7782219
G[11][15]=100.7782219

#tobs 
tobs = np.array(([2.014], [0.90186667],
                 [0.82495], [0.2685333],
                 [0.2685333], [0.2848], 
                 [0.2848], [0.2685333],
                 [0.2685333], [0.72311667],
                 [0.90186667], [2.014]))

mo = 1/v.reshape(16,1)
Stop_crit = 0.01
Iter_max = 100
E = 1e9
Iter=1
mi = mo

while E > Stop_crit:

     tcal = np.dot(G,mi)
     dt = tobs-tcal
     dm = np.dot(np.linalg.pinv(np.dot(G, G.transpose())) , np.dot(G.transpose(),dt))
     mi = mi+dm

     E = np.sqrt(np.mean(dt**2))
     m = mi

     Iter=Iter+1
     if Iter==Iter_max:
         break
     
v = 1/m

plt.imshow(E)
plt.show()