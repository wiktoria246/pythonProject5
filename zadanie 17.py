n = int(input('podaj ile bedzie liczb'))
suma = 0
iloczyn = 1
for i in range(n): #od i = 0 do i = n -1
    liczba = float(input('podaj liczbe nr{}'.format(i + 1))
    suma = suma + liczba
print('suma = {}'.format(suma))
print('srednia = {}'.format(suma / n))
print('iloczyn = {}'.format( iloczyn / n))