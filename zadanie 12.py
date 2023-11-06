a = int(input('podaj wynik egzaminu pisemnego z jezyka polskiego'))
b = int(input('podaj wynik egzaminu pisemnego z jezyka obcego'))
c = int(input('podaj wynik egzaminu dodatkowego'))
d = int(input('podaj wynik egzaminu usntego z jezyka polskiego'))
e = int(input('podaj wynik egzaminu usntego z jezyka obcegp'))

if a >= 30 and b >= 30 and c >= 30 and d >= 30 and e >= 30:
    print('zdałeś mature bez amnesii')
elif a + b + c + d + e / 5 >= 30:
    print('zdałeś mature z amnesiią')
else:
    print('widzimy sie w sierpniu ')