n = int(input('podaj ile bedzie liczb'))
suma = 0# zaczynami sumowanie od zera(bo jeszcze nic nie sumowaliśmy)
iloczyn = 1
licznik = 0# zaczynami sumowanie od zera(bo jeszcze nic nie sumowaliśmy)
licznik2 = 0#zaczynami zliczanie od 0(bo jeszcze nic nie naliczyiśmy)
max_liczba = float(input('podaj liczbe nr 1'))#pierwszym max jest po prostu pierwsza liczba
suma = suma + max_liczba#dodajemy pierwsza liczbe do sumy bi byłaby ona przyjeta w petli
min_liczba = max_liczba
iloczyn = iloczyn * max_liczba
if max_liczba < 3:#sprawdzay czy pierwsza liczba jest mniejsza od 3
    licznik = licznik + 1 #jeSli tak to ja zaliczamy
if max_liczba > -2 and max_liczba <= 11:
    licznik2 = licznik2 + 1
for i in range(1, n): #ta petla zaczyna sie od i = 0 do i = n -1 czyli n - 1 razy
    liczba = float(input('podaj liczbe nr{}'.format(i + 1)))#pobieramy kolejna liczbe
    suma = suma + liczba
    if liczba > max_liczba:
        max_liczba = liczba
    if liczba < min_liczba:
        min_liczba = liczba
    if max_liczba < 3: #sprawdzamy czy pierwsza liczba jest mniejsza od 3
        licznik = licznik + 1#jeśli tak to ja zaliczmy

#wyświetlamy wyniki
print('suma = {}'.format(suma))
print('srednia = {}'.format(suma / n))
print('iloczyn = {}'.format( iloczyn))
print('max liczba = {}'.format( max_liczba))
print('min liczba = {}'.format( min_liczba))
print('ile mniejszych od 3 = {}'.format(licznik))
