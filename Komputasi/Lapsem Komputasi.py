#LU GAUSS

import numpy as np
import copy

n = int(input("Masukan ukuran matriks A (matriks persegi):"))
a = np.zeros((n,n))
b = np.zeros((n,1))
print("Masukan elemen matriks A: ")
for i in range (n):
    for j in range (n):
        a[i,j] = float(input("A(%d,%d): " %(i,j)))

print("Masukan elemen matriks B: ")
for i in range (n):
        b[i,0] = float(input("B(%d,%d): " % (i,0)))

#dekomposisi LU
l = np.eye(n)
u = copy.deepcopy(a)
for i in range (n):
    for j in range (n):
        if j < i :
           l[i,j] = u[i,j]/u[j,j]
           if l[i,j] != np.inf:
              for k in range (n) :
                if k >= j:
                    u[i,k] = u[i,k] - l[i,j]*u[j,k]
        else: 
            temp = copy.deepcopy(u[i,:])
            u[i,:] = copy.deepcopy(u[j,:])
            u[j,:] = copy.deepcopy(temp)
            temp2 = copy.deepcopy (l[i,0:j])
            l[i,0:j] = copy.deepcopy(l[i,0:j])
            l[j,0:j] = copy.deepcopy(temp2)
            temp3 = copy.deepcopy(b[i])
            b[i] = copy.deepcopy(b[j])
            b[j] = copy.deepcopy(temp3) 
            l[i,j] = u[i,j] / u[j,j]
            for k in range (n) :
                if k >= j:
                    u[i,k] = u[i,k] - l[i,j]*u[j,k]

print ("Menampilkan matriks L")
print(l)
print("Menampilkan matriks U")
print(u)

y = np.zeros ((n,1))
for i in range (n):
    sum = 0
    for j in range (i) :
        sum += l[i,j] * y[j]
    y[i] = (b[i] - sum)/l[i,i]

print("matriks y")
print(y)

x = np.zeros((n,1))
for i in range (n):
    i = (n-1) - i
    sum =0
    for p in range(i):
        p = (n-1) - p
        sum += u[i,p]*x[p]
    x[i] = (y[i] - sum)/u[i,i]

print("matriks x")
print(x)

        
