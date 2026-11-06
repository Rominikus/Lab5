n=int(input('Введите число: '))
o=n
rev=0

temp=n
while temp>0:
    dig=temp%10
    rev=rev*10+dig
    temp//=10

if o==rev:
    print(f'{o} - палиндром.')
else:
    print(f'{o} - не палиндром.')

