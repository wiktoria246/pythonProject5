'''#Zadanie 1
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
scorers.sort()
print(max(scorers)

#Zadanie9
players = ['LeBron', 'Kobe', 'Jordan']
scores = [27, 18, 15]
lista1 = ['Durant']
players.extend(lista1)
scores.insert(2, 22)

#Zadanie10
players = ['LeBron', 'Kobe', 'Jordan', 'Durant']
scores = [27, 18, 22, 15]
players.remove('Kobe')
popped_store = scores.pop(1)
print(players)
print(scores)
print(popped_score)

#Zadanie11

players = ['LeBron', 'Kobe', 'Jordan']
scores = [27, 18, 15]

new_players = ['LeBron', 'Kobe', 'Jordan']
new_scores = [27, 18]

players.extend(new_players)
print(players)

store.extend(new_store)
print(store)'''

#Zadanie12

score_stack = []
score_stack.append('0-0')
print(store_stack[-1])
score_stack.append('1-0')
print(score_stack[-1])
score_stack.append('1-1')
print(score_stack[-1])
score_stack.append('1-2')  
print(score_stack[-1])
score_stack.pop(-1)
print(store_stack)

#zadanie13

