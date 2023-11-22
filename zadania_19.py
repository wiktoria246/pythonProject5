n = int(input('podaj ilosc uczniów '))

oceny_uczniów = []

# zbieranie ocen i wag dla uczniów
for i, nr_ucznia in enumerate(range(1, n + 1)):
    print(f'****Numer ucznia {nr_ucznia}*****')
    oceny_uczniów.append([])
    m = int(input(f'podaj ilość ocen dla ucznia nr {nr_ucznia} '))
    for nr_oceny in range(1, m + 1):
        ocena = int(input(f'podaj ocene {nr_oceny} ucznia nr {nr_ucznia} '))
        waga = int(input(f'podaj wage oceny {nr_oceny} ucznia nr {nr_ucznia} '))
        oceny_uczniów[i].append((ocena, waga))

# liczenie średnich i wyświetlenie
for i, oceny_ucznia in enumerate(oceny_uczniów, 1):
    # srednie = 0
    # wagi = 0
    # ilosc = 0
    for j, (ocena, waga) in enumerate(oceny_ucznia, 1):
        # średnia += ocena * waga
        # wagi += waga
        # suma wag
        # ilosc += 1
        print(f'Uczen {i}, ocena {j}, {ocena}, waga {waga}')
    # ilosc = len(oceny_ucznia)
    # sredia [i] = sredania [i] / suma_wag
    # print ( średnia uczni {i} {srednia/wagi}})

