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
    for j in range (n):
        a[i,j] = float(input("B(%d,%d): " % (i,0)))

l = np.eye(n)
u = np.zeros((n,n))
for p in range (n):
    for j in np.arange(p,n):
        if p == 0:
            u[p,j] = copy.deepcopy(a[p,j])
        else:
            sum = 0
            for k in range (p):
                sum += l[p,k]*u[k,j]
            u[p,j] = a[p,j] - sum

    for i in np.arange(p+l,n):
        if p < n - l:
            sum = 0
            for k in range (p):
                sum += l[i,k]*u[k,p]
            l[i,p] =(a[i,p] - sum )/u[p,p]

print("Menampilkan matriks L",l)

print("Menampilkan matriks U",u)


y = np.zeros((n,l))
for i in range (n):
    sum = 0
    for j in range (i):
        sum += l[i,j] * y[j]
    y[i] = (b[i] - sum)/ l[i,i]

print("matriks y")
print(y)

x = np.zeros((n,l))
for i in range (n):
    i = (n - l) - i
    sum = 0
    for p in range(i):
        p = (n - l) - p
        sum += u[i,p]*x[p]
    x[i] = (y[i] - sum )/u[i,i]

print("mattiks x")
print(x)

#Dekomposisi LU dengan Metode Reduksi Crout
l = np.eye(n)
u = np.zeros((n,n))
for p in range(n):
    for j in np.arange(p,n):
        if p = 0:
            u[p,j] = copy.deepcopy(a[p,j])
        else:
            sum =0
            for k in range(p):
                sum += l[p,k]*u[k,j]
            u[p,j] = a[p,j] - sum

    for i in np.arange(p+1,n):
        if p < n - 1:
            sum = 0
            for k in range(p):
                sum += l[i,k]*u[k,p]
            l[i,p]=(a[i,p]-sum)/u[p,p]

print("Menampilkan Matriks L",l)
print("Menampilkan Matriks U",u)

#Menghitung nilai y
y = np.zeros((n,1))
for i in range(n):
    sum = 0
    for j in range(i):
        sum += l[i,j]*y[i]
    y[i] = (b[i] - sum)/l[i,j]
print ("Matriks Y",y)

#Menghitung nilai X
x = np.zeros((n,1))
for i in range(n):
    i = (n-1)-i
    sum = 0
    for p in range(i):
        p - (n-1)-p
        sum += u[i,p]*x[p]
    x[i] = (y[i]-sum)/u[i,i]
print("Matriks X",x)
