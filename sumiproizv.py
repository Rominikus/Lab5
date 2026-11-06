n=int(input('Введите N: '))

sum_numbers=0
product=1
sum_sqares=0

for i in range(1, n+1):
    sum_numbers+=i
    product*=i
    sum_sqares+=i**2


print(f'Сумма: {sum_numbers}')
print(f'Произведение (N!): {product}')
print(f'Сумма квадратов: {sum_sqares}')