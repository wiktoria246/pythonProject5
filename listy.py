#1. umieszczenie elementow na liście
#2. recznie wpisane

lista1 = ['kot', 1, 3.1, [4, 4, 3], 'pies', 'kapibara', 'orzeł']

#3. powielanie listy

lista2 = [1] * 5
print(lista2)

lista3 = [1, 2, 3] * 4
print(lista3)

#4. wrzucanie danych element po elemecie(funkcja append)

lista4 = []
n = int(input('ile bedzie liczb?'))
for i in range(n):
    liczba = float(input('podaj kolejna liczbe'))
    lista4.append(i)#wsatwiamy liczbe na koncu
print(lista4)

#5. wstawiane elementów na dowolnej pozycji(funkcja insert)
lista5 = [4, 1, 7, 5]
lista5.insert(1, 56)#na pozycji 1 wstawiamy liiczbe 56
print(lista5)

#6.rozszerzanie listy

lista6 = [5, 1, 5, 9, 3]
lista7 = [8, 9, 0, 1]
lista7.extend(lista6)#dopisanie do listy 3 elementów listy 4
print(lista7)

#7.konkatynacja list(sklejanie elementów)- rozszerzenie liczby sposób 2

lista8 = [6, 1, 4, 9]
lista9 = [-1, 8, 0, 5]
lista10 = lista8 + lista9
print(lista10)

#8.wyświetlanie długości listy:

lista11 = [6, 3, 1, 9]
print(len(lista11))

#9.pare przydatnych funkcji:
#10. zlicznaie elementów

lista12 = ['a', 'b', 'a', 'b', 'c', 'a']
print(lista12.count('a'))

lista13 =[4, 2, 1, 7, 8, 11, 9]
print('suma = {}'.format(sum(lista13)))
print('max = {}'.format(max(lista13)))
print('min = {}'.format(min(lista13)))

#11. zamiana słowa na liste

slowo1 = 'informatyka'
slowo1_lista = lista(slowo1)
print(slowo1_lista)

#12.zamiana listy na słowo







#13.jak pobrać pojedyńcze elementy
#a)korzystahjaćz indeksów dodatnich
lista14 = [6, 4, 7, 2]
print(lista14[2])#pobieramy 3 element(numerujemy od 0)
#b)korzystajac z elementów ujemnych
lista15[2, 4, 6, 8, 5, 3]
print(lista15[-2])#pobieramy drugi element od konca(numerujemy od -1 do -długości)