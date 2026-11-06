# Задача 3
# print(f"{'x':>8} {'x**2 - 2*x + 1':>17}")
# print('-'*30)

# for i in range(-5, 6):
#     y = i**2 - 2 * i + 1
#     print(f"{i:8} {y:10}")


# Задача 6
print("Выберите 1 или 2.")
print("1) в десятичную")
print("2) В двоичную")
ans = int(input("(1/2?) "))
if ans == 1:
    n = int(input("Введите целое число в двоичной системе счисления: "))
    res = 0
    temp = n
    m = 0
    while temp > 0:
        digit = temp % 10
        res += digit * 2 ** m
        m+=1
        temp //= 10
    print(f"{n} в десятичной будет: {res}")
elif ans == 2:
    n = int(input("Введите целое число: "))
    res = ''
    temp = n
    while temp > 0:
        res = str(temp % 2) + res
        temp //= 2
    print(f"{n} в двоичной будет: {res}")
else:
    print("Некорректный ввод, перезапустите программу")