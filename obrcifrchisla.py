n=int(input('Введите число: '))
original=n

k=0
t=0
pr=1
rev=0

while n>0:
    dig=n%10
    k+=1
    t+=dig
    pr*=dig
    rev=rev*10+dig
    n//=10

print(f'Количество цифр: {k}')
print(f'Сумма цифр: {t}')
print(f'Произведение чисел: {pr}')
print(f'Перевернутое число: {rev}')
