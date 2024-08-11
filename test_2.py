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
        # if isinstance(other, int):
        return self.number_of_floors == other.number_of_floors
    def __add__(self, value):
        value = 10
        if isinstance(value, int):
            self.number_of_floors += value
    def __iadd__(self, value):
        value = 10
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2)  # eq
h1 + 10  # add
print(h1)
h1 + 10 # __iadd__
print(h1)
h2 + 10  # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__