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

polinom=int(input('Masukan derajat polinom yang ingin kamu gunakan: '))

Z = np.polyfit(x,y,polinom)
f = np.poly1d(Z)

print('Persamaan yang fit untuk derajat %d : '%polinom,f)

x_pol = np.linspace(x[0],x[-1],50)
y_pol = f(x_pol)

plt.plot(x,y,'o',x_pol,y_pol)
plt.show()