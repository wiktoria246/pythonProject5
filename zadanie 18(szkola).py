lista = [1]
a = 1
punkty_d1 = 0
punkty_d2 = 0
for i in lista:
    print('akcja nr{}'.format(a))
    nr_druzyny = int(input('podaj nr druzyny, która wygrała akckje nr {}\n'.format(a)))
    if nr_druzyny == 1:
        punkty_d1 += 1
    else:
        punkty_d2 += 1
        print('{} : {}'.format(punkty_d1, punkty_d2))
    if punkty_d1 >= 5 and punkty_d1 - punkty_d2 >= 2:
        print('druzyna 1 wyrała')
        break
    elif punkty_d2 >= 5 and punkty_d2 - punkty_d1 >= 2:
        print('druzyna 2 wygrała')
        break
    a += 1
    #a +=1 to samo co a = a + 1
    lista.append(1)
