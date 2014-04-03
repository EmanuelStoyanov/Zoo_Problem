import sqlite3

conn = sqlite3.connect("animals.db")
c = conn.cursor()


class Zoo():
    def __init__(self, capacity, budget):
        self.capacity = capacity
        self.budget = budget
        self.animals = []

    def accomodate_animal(self, animal):
        self.animals.append(animal)

    def daily_incomes(self):
        return len(self.animals)*60

    def daily_outcomes(self, cursor):
        sum = 0
        for animal in self.animals:
            """ if method eat() return kilos food that animal should eat 
                and method is_carnivore which return True if its so"""
            if is_carnivore(animal):
                sum += animal.eat()*4
            else:
                sum += animal.eat()*2
        return sum
