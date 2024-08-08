import matplotlib.pyplot as plt
import numpy as np
n= int(input('masukan jumlah data yang ingin diinput: '))
s=[]

x=[]
for i in range(n):
    X = float(input('Masukan data kedalaman ke-%d: '%i))
    x.append(X)

y=[]
for i in range(n):
    Y = float(input('Masukan data temperatur ke-%d: '%i))
    y.append(Y)

print('Data input: ')
print('Kedalaman: ',x)
print('Temperatur:',y)

xsum=0
ysum=0
x2sum=0
jml=0

for i in range(n):
    xsum=xsum+x[i]
    ysum=ysum+y[i]
    x2sum=x2sum+(x[i]**2)
    jml=jml+x[i]*y[i]
a=(n*jml-xsum*ysum)/(x2sum*n-xsum*xsum)
b=(x2sum*ysum-xsum*jml)/(x2sum*n-xsum*xsum)

Y=np.zeros(n)
for i in range(n):
    Y[i]=a*x[i]+b

print("The Linier Fitting Is: ",Y)
print("Fungsi Linier Fitting adalah: T=",a,"Z+",b)
plt.plot(x,y,'o',x,Y)
plt.show()