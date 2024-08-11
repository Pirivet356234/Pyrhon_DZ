class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if new_floor <= 0 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            nf = 1
            while nf <= new_floor:
                print(nf)
                nf = nf + 1
                
    def __len__(self):
        return self.number_of_floors
    
    def __str__(self):
        return f'Название: {self.name,} кол-во этажей: {self.number_of_floors}'
    
    def __eq__(self, other):
        isinstance(other, int)
        return self.number_of_floors == other.number_of_floors
        
    def __add__(self, value):
        value = 10
        self.number_of_floors = self.number_of_floors + value
    
    def __iadd__(self, value):
        value = 10
        self.number_of_floors = self.number_of_floors + value
     
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

#h1 = h1 + 10 # __add__
#print(h1)
#print(h1 == h2) # __eq__

h1 += 10 # __iadd__
print(h1)


