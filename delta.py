import math

a = float(input('podaj współczynnik a'))
b = float(input('podaj współczynnik b'))
c = float(input('podaj współczynnik c'))

if b == 0 and c == 0:
    print('x = 0')
elif b == 0 and c != 0:
    if -c / a > 0:
        print('x1 = {}'.format(math.sqrt(-c / a))) #math,sqrt(x) = pierwiastek
        print('x2 = {}'.format(-math.sqrt(-c / a)))
    elif -c / a < 0:
        print('sprzeczne')
elif c == 0 and b != 0:
    print('x1 = {}'.format(0))
    print('x2 = {}'.format(-b / a))
else:
    delta = b ** 2 - 4 * a * c #b ** 2 = b do potegi 2
    if delta > 0:
        print('x1 = {}'.format((-b + math.sqrt(delta)) / (2 * a)))
        print('x2 = {}'.format((-b - math.sqrt(delta)) / (2 * a)))
    elif delta == 0:
        print('x = {}'.format(-b / (2 * a)))
    else:
        print('sprzeczne')
5