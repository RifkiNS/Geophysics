import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv

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

t = np.array(([t11,t12,t13,t21,t22,t23,t31,t32,t33,t41,t42,t43]))

print(v)
print(t)

# matriks G
G = np.zeros((len(t), 16))
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

Gtrans = G.transpose()
perkalian = np.dot(G,Gtrans)
invers = np.linalg.pinv(perkalian)
print(invers)

gtransdikaliinvers = np.dot(Gtrans, invers)

hasilresize = t.reshape(12,1)
print(hasilresize.shape)

m = np.dot(gtransdikaliinvers, hasilresize)
print(m)

mbenar = 1/m

resizem = mbenar.reshape(4,4)
print(resizem)

 #kriteria konvergensi
stop_crit = False
jumlah_iterasi=1000

#set param
error = 1e9
iterasi = 1   


tobs = np.array(([2.014], [0.90186667],[0.82495], 
                 [0.2685333],[0.2685333],[0.2848], 
                 [0.2848], [0.2685333],[0.2685333], 
                 [0.72311667],[0.90186667], [2.014]))
       

mo=mbenar
iterasi_m=[mo]
i=0
errorplot=[]
    
Gtrans = G.transpose()
perkalian = np.dot(G,Gtrans)
invers = np.linalg.pinv(perkalian)            
Gtranskaliinvers=np.dot(Gtrans,invers)

while (not(stop_crit)):
  tcal=np.dot(G,iterasi_m[i])
  dt = tobs-tcal
  dm = np.dot(Gtranskaliinvers,dt)
  iterasi_m.append(iterasi_m[i]+dm)
  print(iterasi_m[i])
  i+=1
  print(iterasi_m[i])
  print('tcal', tcal)
  error = np.sqrt(np.mean(np.power(dt,2)))
  errorplot.append(error)
  iterasi += 1
  plt.plot(errorplot)
  mhasil = 1/iterasi_m[-1]
  resizem = mhasil.reshape(4,4)                        

  x = np.arange(0, 5, 1)
  y = np.arange(0, 5, 1)

  fig, ax = plt.subplots()
  im = ax.imshow(v, extent=[0, 4, 0, 4])
  ax.pcolormesh(x, y, v)
  ax.invert_yaxis()

  fig, ax1 = plt.subplots()
  im = ax1.imshow(resizem, extent=[0, 4, 0, 4])
  ax1.pcolormesh(x, y, resizem)
  ax1.invert_yaxis()
  plt.show()
  print('error',error*100,"%")
  if iterasi == 7:
    stop_crit = True
