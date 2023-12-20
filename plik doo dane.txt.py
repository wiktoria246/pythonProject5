'''#1. wczytywanie danych gdy w każdym wierszu jest dana
#open('dane.txt) - otwieramy pliki
# .readlines() - wczytywanie danych do listy
dane = open('dane.txt').readlines()
print(dane)


#usuwamy znaki noej linii z końca kaźdego elementu (\n)
dane = [x.strip() for x in dane]
print(dane)

#zmieniamy wszystkue teksty na liczby
dane = list(map(int,dane))
print(dane)


#2. wczytywanie danych, gdy w kaźdym wierszu jest jedna dana - wersja skondensowana
dane2 = [int(x) for x in open('dane.txt').readlines()]
print(dane2)'''

#wczytywanie danych wielowierszowych i wielukolumnowych
dane = open('dane2.txt').readlines()
print(dane)

#usuwamy znaki nowej liniki z końca kaźdego wiersza
dane = [x.strip() for x in dane]
print(dane)

#dzielimy za pomocą spacji kaźdy wiersza na pojedyńcze elementy
dane = [x.split() for x in dane]
print(dane)

#zamieniamy dane liczbowe z string na int
for i in range(len(dane)):
    for j in range(2, len(dane[i])):
        dane[i][j] = int(dane[i][j])
print(dane)

