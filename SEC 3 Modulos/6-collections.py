from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 lista de Frutas (comtagem)
fruits = ['Maça', 'Banana', 'Uva', 'Pera', 'Banana', 'Uva', 
          'Maça', 'Banana', 'Uva', 'Pera', 'Laranja', 'Abacaxi', 'Tangerina',
          'Uva', 'Pera', 'Banana']

print(fruits)
print(Counter(fruits))

# 2 utilizando tupla nomeada 
game = namedtuple('game', ['name', 'price', 'note'])
g1 = game('Minecraft', 99.90, 8.7)
g2 = game('RDR 2', 350.00, 9.7)
g3 = game('GTA 5', 100.00, 9.9)
g4 = game('Clash Royale', 'free', 7.7)

print(g1)
print(g2)
print(g3)
print(g4)

# 3 ordenando por dicionarios 
students = {'Pedro': 18, 'Davis': 19, }

