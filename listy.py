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

#14.Jak wyciąć fragment listy
lista15 = [1, 3, 5, 7, 6, 7, 4, 7]
print(lista15[2:5])#wycinamy emenemty nr 2 do nr 4 (1 -7) : <2, 5)
print(lista15[1:6:2])#wycinamy element nr 1 do nr 5 (6 -1) co drugi element
print(lista15[-1:-6:-2])
print(lista15[::-1])#odwracanie listy na trwałe

 #15.funkcje specjalne
 #a) sum()- bylo
 #b) max() - było
 #c) min() - było

lista16 = [-1, 9, 5, 23, 80]
print(min(lista16))

 #d)długość(ilość elementów)
 print(len(lista16))

 #e)sortowanie llisty - modyfikacja listhy na trwałe
 lista17 = [-13, 2, 4, -5, 7]
 lista17.sort()#domyślnie stosujemy rosnąco
 print(lista17)

 lista18 = [2, 4, -4, 7, 8, 1]
 lista18.sort(reverse=True)#domysln9e sortujemy malejaco

 #jak zobaczyć liste posortowana ale nie na trwałe
 lista19 = [4, 7, ,-8, 1, 3, 6]
print(list(sorted(lista19)))
print(lista19)

#f)odwracanie listy - wersja z funkcja reverse()
lista20 = [2, 5, 8, 3, 9, 2]
lista20.reversed()
print(lista20)

#g)zlicznie elementów na liście
lista21 = [3, 5, 7, 4, 77, 8]
print(lista21,count(2))

#h)funkcja map - czyli odwzorowanie
lista22 = [3, 5, 7, 3, 86, 67]
lista22_jako_liczby = list(map(int, lista22))#każdy napis zmieniamy na liczbe int
print(lista22_jako_liczby)

lista23 = [3, 6, 7]
lista23_jako_str = list(map(str, lista23))
print(lista23_jako_str)

#i)usuwanie elementów
lista24 = [1, 5, 7, 24, 6]
lista24.remove(6)#usuwanie elementu na bazie jego wartości(tutaj 6) - tylko pierwszy raz
print(lista24)

lista25 = [5, 7, 3, 6, 2, 4, 5, 6, 5]

while 5 in lista25:#usuwanie wszystkich licz o podanej wartości(tutaj usuwamy 5)
   lista25.remove(5)
print(lista25)

#j)usuwanie elementów na bazie ivh pozycji na liście 
lista26 = ['jezyk polski', 'filozofia', 'wiedza o kulturze', 'etyka', 'hit']
del lista26[2]#usunięcie elementu 3 
print(lista26)

lista27 = [1410, 1939, 2004, 2000, 1795, -1]

del lista27[1:4]
print(lista27)

#WYRAŻENIA LISTOWE

#wyłapywanie liczb parzystych z listy - metoda hałupnicz
lista28 = [3, 8, 1, 9, 44, 16, 7, 50, 48]
lista29 = []
for e in lista28:
 #liczba1 % liczb2 - obliczamy reszte z dzielenia liczby "liczba 1" przez "liste2"
    if lista29.append(e) #badanie czy lista przy dieleniu przez 2 daje reszte 0 (parzysta)
print(lista29)

#wyłapywanie liczb parzystych z listy - metoda piekna
lista30 = [e for e in lista30 if e % 2 == 0]