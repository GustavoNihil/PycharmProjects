
#         PAREI EM 55MIN


class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passagers = []
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passagers.append(name)
        return True
    def open_seats(self):
        return  self.capacity - len(self.passagers)
flight = Flight(3)
people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight sucessfully.")
    else:
        print(f"No available seats for {person}.")

#passagens aereas

class Point():
    def __init__(self, input1, input2): #Uma função chamada "init" que cria espaço para 2 inputs dentro do objeto x e y
        self.x = input1
        self.y = input2
p = Point(2, 8)
print(p.x)
print(p.y)
#classes

from functions import square #puchando a função de outro arquivo .py
#poderia ser "import functions"
for i in range(10):
    print(f"The square of {i} is {square(i)}")

#functions

houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
houses["Hermione"] = "Gryffindor"
print(houses["Hermione"])

#dictionaries

for i in [0, 1, 2, 3, 4, 5]:
    print(i)
for i2 in range(6):
    print(i2)
names = ["Harry", "Ron", "Hermione"]
for name in names:
    print(name)
name = "Harry"
for character in name:
    print(character)

#loop

s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
print(s)
s.remove(2)
print(s)
print(f"The set has {len(s)} elements.") #len = length (comprimento)

#add elements to set

names = ["André", "João", "Marquinhos", "Guinho"]
names.append("Draco") #Adiciona o elemento na última posição
names.sort()
print(names)

#Lista de nomes

n=float(input('Digite um número: '))
if n == 0:
    print('O número digitado foi 0')
else:
    if n > 0:
        print('Seu número é positivo')
    else: print('Seu número é negativo')

#zero, positivo, negativo
