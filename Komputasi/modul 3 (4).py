print ('Metode Newton - Gregory Backward')
def u_cal(u,n):
    temp = u
    for i in range(1, n):
         temp = temp*(u+i)
    return temp

def fact(n):
    f = 1
    for i in range(2, n+1):
        f *=i
    return f
n = int(input('Masukan jumlah data: '))
x =[]

for i in range(n):
    dataX = float(input('data x ke-%d: '%i))
    x.append(dataX)
y =[[0 for i in range(n)]
      for j in range(n)]
for i in range(n):
    y[i][0] = float(input('data y ke-%d: '%i))
print('Data input \n _______________')
print('X :',x)
print('Y :',y)

value = float(input('Masukan nilai x yang ingin dicari: '))

for i in range(1,n):
    for j in range(n):
        y[j][i] = y[j][i-1]-y[j-1][i-1]
print('_______________')
print('x(i) \t y(i) \t y1(i) \t y2(i) \t y3(i) \t y4(i)')
print('_______________')
for i in range (0,n):
    print(x[i], end="\t")
    for j in range(0,i):
        print(y[i][j], end="\t")
    print(" ")

sum = y[n-1][0]
u = (value - x[n-1])/(x[1]-x[0])
for i in range (1,n):
    sum = sum + (u_cal(u,i)*y[n-1][i]/fact(i))
print('\n Nilai Pressure :', value, 'adalah:',round(sum,6))
