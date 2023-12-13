#Zadanie 1
cities = ['Warszawa', 'Łódź', 'Kraków']
lista1 = ['Gdańsk']
cities.extend(lista1)
print(cities)
#Zadanie 2
idx = ['001', '002', '001', '003', '001']
print(idx.count('001'))

#Zadanie 4
filenames = ['view jpg', 'bear.jpg', 'ball.png']
filenames.insert(0, 'phone.jpg')
del filenames[3]
print(filenames)

#Zadanie5
day1 = ['3984', '900042', '4829', '2380']
day2 = ['4231', '5234', '1345', '2455']
day1.extend(day2)
print(day1)

#Zadanie6
techs = ['python', 'java', 'sql', 'aws']
techs.sort()
print(techs)

#Zadanie7
hashtags = ['summer', 'time', 'vibes']
hashtags ='#'.join(hashtags)
print(hashtags)

#Zadanie8
scorers = [27, 8, 15, 2, 9, 10, 21, 4, 20, 5]

