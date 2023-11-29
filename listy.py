#1. umieszczenie elementow na liście
#2. recznie wpisane

lista1 = ['kot', 'pies', 'kapibara', 'orzeł']

#3. powielanie listy

lista2 = [1] * 5
print(lista2)

lista3 = [1, 2, 3] * 4
print(lista3)

#4. wrzucanie danych element po elemecie

lista4 = []
for i in range(1, 101):
    lista4.append(i)
print(lista4)

#5. wstawiane elementów na dowolnej pozycji
lista5 = [4, 1, 7, 5]
lista5.insert(1, 56)
print(lista5)

#6.rozszerzanie listy

lista6 = [5, 1, 5, 9, 3]
lista7 = [8, 9, 0, 1]
lista7.extend(lista6)
print(lista7)

#7.konkatynacja list(sklejanie elementów)

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