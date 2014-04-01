class Animal():
    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight

    def get_animal_stats(self):
        conn = sqlite.connect('animal.db')
        c = conn.cursor()

    def grow(self, time):

    def eat(self):

    def die(slef):

    def check_dead(self):
        if 
