#Scinanie pierwszej liczby
'''n = 12345

while n > 0:#tzw warunek trwania petli(czyli dopóki to bedzie prawda to pentla sie wykonuje)
    print(n)
    n = // 10# wykonujemy dzielenie bez czesci ułamkowej(dzielenie // oznacza ze dzielimy i ucinamy liczbe po przecienku)'''

#szukanie prawidłowego hasła
poprawne_hasło = 'Mercedes2000'
h = ' '
próby = 3
czy_udało_sie = 0
while h != poprawne_hasło:#dopuki hasła nie są takie same pętla ma sie wykonywać
    if próby == 0:
        exit()#wyjście z programu
    h = input('podaj hasło')
    if h == poprawne_hasło:
        czy_udało_sie = 1
    próby = próby - 1
if czy_udało_sie == 1:
    print('udało sie :)')
else:
    print('nie ma hasła = nie ma dostepu')

#petla nieskończona(do szukania hasła)
'''poprawne_hasło = 'Mercedes2000'
while 1 == 1:
    h = input('podaj hasło')
    if h == poprawne_hasło:
        break
    else:
       print('źle')
print('udało sie :)')'''

