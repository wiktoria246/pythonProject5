
wygrane_akcje = [0, 0]
akcja = 1
akcje_w_setcie = 21

def czy_druzyna_ma_przwage(wyniki, roznica):
    return abs(wyniki[0] - wyniki[1]) >= roznica

for _ in iter(int, 1):
    print(f'Akcja {akcja}')
    druzyna = int(input('Podaj numer durżyny,która wygrała akcje: '))

    if druzyna == 1 or druzyna == 2:
        i = druzyna - 1
        wygrane_akcje[i] += 1

        print(f'Drużyna {druzyna}') 
        print(f'Wynik {wygrane_akcje[0]}:{wygrane_akcje[1]}')

        # warunek końca gry
        if czy_druzyna_ma_przwage(wygrane_akcje, 2) and (wygrane_akcje[0] >= akcje_w_setcie or wygrane_akcje[1] >= akcje_w_setcie) : # czy_druzna_ma_przynajmniej_21_punktow
            wygrana_druzyna = 1
            if wygrane_akcje[1]> wygrane_akcje[0]:
                wygrana_druzyna = 2


            # wygrana_druzyna = 1 if (wygrane_akcje[0] > wygrane_akcje[1]) else 2
            print(f'Drużyna {wygrana_druzyna} wygrała seta')
            break

    else:
        print(f'Podałes zły numer drużyny')


def func(druzyna):
    return druzyna + 1

    