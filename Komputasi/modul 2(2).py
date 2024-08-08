print('Metode Newton Divide Difference')
def proterm(i,value,x):
    pro = 1
    for j in range(i):
        pro = pro *(value - x[j])
    return pro

def divideDiffTable(x,y,n):

    for i in range(1,n):
        for j in range(n-i):
            y[j][i] = ((y[j][i-1]-y[j+1][i-1])/(x[j]-x[i+j]))
    return y

def applyFormula(value,x,y,n):
    sum = y[0][0]
    for i in range(1,n):
        sum = sum + (proterm(i,value,x)*y[0][i])
    return sum

def printDiffTable(y,n):
    for i in range (n):
        for j in range(n-i):
            print (round(y[i][j],4),'\t',end=' ')
        print(' ')

n = int(input('Masukan jumlah data: '))

x =[]
y = [[0 for i in range(n)]
      for j in range (n)]

for i in range(n):
    dataX = float(input('data pressure ke- %d: '%i))
    x.append(dataX)

for i in range(n):
    y[i][0] = float(input('data wind speed ke-%d: '%i))

value = float(input('Masukan nilai pressure yang ingin dicari: '))

print('_'*100)
print('x(i) \t y(i) \t y1(i) \t y2(i) \t y3(i) \t')
print('_'*100)

y = divideDiffTable(x,y,n)

printDiffTable(y,n)

print('\nNilai x: ',value,'adalah: ',round(applyFormula(value, x, y,n),2))
  