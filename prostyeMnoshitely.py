n=int(input('Введте число: '))
original=n
factors=[]
divisor=2
while divisor**2<=n:
    while n%divisor==0:
        factors.append(divisor)
        n=n//divisor
    divisor+=1
if n>1:
    factors.append(n)

print(f'{original} = {' x '.join(map(str, factors))}')