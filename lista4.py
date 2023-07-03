#1
zdanie = input('Wprowadź zdanie: ')
j = 0
for i in zdanie:
    print(i, end=' ')
    j += 2
print('\n', j)

#2
zdanie = input('Wprowadź zdanie: ')
j = 0
for i in zdanie:
    if i == 'a':
        j += 1
print('Mamy', j, 'literek a')

#3
zdanie = input('Wprowadź zdanie: ')
j = 0
for i in zdanie:
    if i != ' ':
        print(i, end='')
    else:
        print(i)
        j += 1
j += 1
print('\nW zdaniu wystąpiło', j, 'słów')

#4
ln = 1
pi = 1
for i in range(2, 10001):
    if i % 2 == 0:
        ln -= (1/i)
    else:
        ln += (1/i)
print('ln(2)=', ln)
j = 1
for i in range(3, 10001, 2):
    if j % 2 == 1:
        pi -= (1/i)
    else:
        pi += (1/i)
    j += 1
pi *= 4
print('pi=', pi)

#5
ileliczb = int(input('Z ilu liczb średnia: '))
srednia = 0
for i in range(0, ileliczb):
    liczba = int(input('Liczba: '))
    srednia += liczba
srednia /= ileliczb
print('średnia: ', srednia)

#6
from math import sqrt
from math import sin
print('\npierwiastki kwadratowe:\n')
for i in range(1, 21):
    print(sqrt(i))
print('\n')
print('sinusy:\n', end='\n')
for i in range(1, 21):
    print(sin(i))

#7
from math import sqrt
s = 1
for i in range(2, 10001):
    s += (1/i**2)
print('s=', s)
print('wynik=', sqrt(6*s))

#8
t = input('Wprowadź zdanie: ')
for i in range(len(t)-1, -1, -1):
    print(t[i], end='')

print('\n')
#9
a = -1
b = 0
for i in range(1001):
    c = (a + b) / 2
    if c**5 + c + 1 >= 0 and a**5 + a + 1 >= 0:
        a = c
    elif c**5 + c + 1 <= 0 and a**5 + a + 1 <= 0:
        a = c
    else:
        b = c
print('c=', c)
print(c**5 + c + 1)
