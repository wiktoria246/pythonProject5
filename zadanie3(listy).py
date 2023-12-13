#zaamiana wszystkich liter na małe
text = 'Programowanier w języku Python'
text = text.lower()
print(text)

#zaamiana wszystkich liter na duże
'''text = text.upper()
print(text)'''

#zmiana znaków 'ę' -> 'e'

#1. Przekształcamy napis na liste pojedyńczych znaków
text_lista = list(text)
print(text_lista)

#2. Zaminienamy wszystkie 'ę' na 'e'
for i in range(len(text_lista)):#i = 0, 1, 2, ..., długość - 1
    if text_lista[i] == 'ę':
        text_lista[i] = 'e'
#3. Sklejamy liste z powrotem na napis
text = ''.join(text_lista)#'' pusty zbiór(bez spacji)
print(text)

#4. Usuwanie duplikatów
'''(list(set(text)))#przed połączeniem w cały napis
text_unikatowy = ''.join(list(set(text)))#set tworzy zbior unikatowych znaków
print(text_unikatowy)'''

print(list(set(text)))
lista_unikatowy = list(set(text))

#5. Usuwanie spacji z tekstu
lista_unikatowy.remove(' ')

#6.Sortowanie:
lista_unikatowy.sort()

#7.Łączymy znaki w gotowy napis:
print(''.join(lista_unikatowy))
