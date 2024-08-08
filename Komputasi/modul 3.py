n = int (input('Masukkan jumlah data yang ingin diinput: '))
x = []
for i in range(n):
    data = float (input('Masukkan data X ke-%d : ' %i))
    x.append(data)
 
y = []
for i in range(n):
    Y = float (input('Masukkan data Y ke-%d: ' %i))
    y.append(Y)
 
print('Data Input : ')
print('Data X : ', x)
print('Data Y : ', y)
 
d = 1
k = 0
t = 1
while (True):
    find = float (input('Masukkan nilai x yang akan dicari: '))
    for i in range(n):
        s = 1
        t = 1
        for j in range(n):
            if (j != i):
                 s = s*(find-x[j])
                 t = t*(x[i]-x[j])
        k = k+((s/t)*y[i])
    print('Maka nilai y(x) : %f' %k)
    k = 0
exit()
    
   



  