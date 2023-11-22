#petla zagnieżdżona
'''for i in range(10):
    for j in range(6):
        print('{}\t{}'.format(i, j))'''

#tabliczka mnożenia
'''for i in range(1, 11):#wiersze tabelki
    for j in range(1, 11):#kolumny
        print(i * j, end = '\t')
    print()'''

#choinka z gwiazdek
n = int(input('podaj wysokość chioinki'))
#g = 1#gwiazdki
#s = n - 1#spacja
for i in range(n):
    #g = 2 * i +1
    #s = n - 1 - i
    for j in range(s):
        print(' ', end='')#wypisujemy spacje i nie przechodzimy do nowej liniki
    for j in range(g):
        print('*', end='')
    print()
    g += 2
    s -= 1
