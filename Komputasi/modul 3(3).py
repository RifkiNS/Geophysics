print ('Metode Newton - Gregory Forward')
def u_cal(u,n):
    temp = u
    for i in range(1, n):
         temp = temp*(u-i)
    return temp

def fact(n):
    f = 1
    for i in range(2, n+1):
        f *=i
    return f
n = int(input('Masukan jumlah data: '))
x =[]

for i in range(n):
    dataX = float(input('data Pressure ke-%d: '%i))
    x.append(dataX)
y =[[0 for i in range(n)]
      for j in range(n)]
for i in range(n):
    y[i][0] = float(input('data Wind Speed ke-%d: '%i))
print('Data input \n -----------------')
print('X :',x)
print('Y :',y)

value = float(input('Masukan nilai Pressure yang ingin dicari: '))

for i in range(1,n):
    for j in range(n-i):
        y[j][i] = y[j+1][i-1]-y[j][i-1]
print('_'*100)
print('x(i) \t y(i) \t y1(i) \t y2(i) \t y3(i) \t y4(i)')
print('_'*100)
for i in range(n):
    print(x[i],end="\t")
    for j in range(n-i):
        print(y[i][j], end='\t')
    print(' ')
sum = y[0][0]
u = (value - x[0])/(x[1]-x[0])
for i in range(1,n):
    sum = sum +(u_cal(u,i)*y[0][i]/fact(i))
print('\nNilai x: ', value,'adalah: ', round(sum,6))

