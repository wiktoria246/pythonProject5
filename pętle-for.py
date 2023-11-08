#dodatkowo-import math
#1. petla for - powtarzaniie tej samej czynności ustaloną liczbe raz
'''for i in range(10):
    print('{} ok'.format(i))

#1.zamiennie:
# for i in range(10):
    #print(str(i) + 'ok')'''

#2 petla for - generowanie określonych liczb
# liczny całkowite dodatnie podzielne przez 3 z przedziału <1; 1000>
'''for i in range(3, 1001, 3):
    print(i)'''

#dodatkowo-print(math.gcd(24, 36))

'''for i in range(1, 1001):
    if i % 3 == 0 and i % 12 == 0: #i % 3 - obliczenie reszty z dzielenia przez 3
        print(i)'''

#3 petla for - chodzenie po liście
lista = [3, 8, 1, 9, 16, 38, 4250]

#sposób 1
for i in lista:
    print('{} no i ok'.format(i))

#4. nieskończona petla for
'''lista = [1]
j = 0
for i in lista:
    print(j)
    j = j + 1
    lista.append(1)'''

j = 0
while 1 ==1:
    print(j)
    j = j + 1
    lista.append(1)
