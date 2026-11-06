n=5

#Прямоугольник
print('Прямоугольник:')
for i in range(n):
    print('*'*n)
#Треугольник
print('/nТреугольник:')
for i in range(1, n+1):
    print('*'*i)
#Елочка
print('/nЕлочка:')
for i in range(1, n+1):
    print(' '*(n-i)+'*'*(2*i-1))

#Ромб
print('/nРомб:')
for i in range(1, n+1):
    print(' '*(n-i)+'*'*(2*i-1))
for i in range(n-1, 0, -1):
    print(' '*(n-i)+'*'*(2*i-1))