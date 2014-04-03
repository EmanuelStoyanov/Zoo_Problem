import sqlite3


class Database:
    # Connect to database
    conn = sqlite3.connect('animals.db')
    c = conn.cursor()

    def get_animal_stats(animal_id):
        # Form a query
        query = '''
                SELECT
                zoo_animals.species,
                zoo_animals.name,
                zoo_animals.gender,
                zoo_animals.weight,
                zoo_animals.age,
                animals.life_expectancy,
                animals.food_type,
                animals.gestation,
                animals.newborn_weight,
                animals.average_weight,
                animals.weight_age_ratio,
                animals.food_weight_ratio
                FROM zoo_animals
                JOIN animals
                ON zoo_animals.species = animals.species
                WHERE zoo_animals.id = ?
                '''
        result = c.execute(query, (animal_id, )).fetchone()
        # Put the result in a dictionary and return
        to_return = {
            'species': result[0],
            'name': result[1],
            'gender': result[2],
            'weight': result[3],
            'age': result[4],
            'life_expectancy': result[5],
            'food_type': result[6],
            'gestation': result[7],
            'newborn_weight': result[8],
            'average_weight': result[9],
            'weight_age_ratio': result[10],
            'food_weight_ratio': result[11],
        }
        return to_return

    def set_aminal(dict):
        query = '''
                INSERT INTO zoo_animals
                (zoo_animals.species,
                zoo_animals.name,
                zoo_animals.gender,
                zoo_animals.weight,
                zoo_animals.age)
                VALUES
                (?,?,?,?,?)
                '''
        c.execute(query, (dict[species], dict[name],
            dict[gender], dict[weight], dict[age]))

    def update_animal(animal_id, dict):
        query = '''
                UPDATE zoo_animals
                SET
                zoo_animals.species = ?,
                zoo_animals.name = ?,
                zoo_animals.gender = ?,
                zoo_animals.weight = ?,
                zoo_animals.age = ?
                WHERE
                zoo_animals.id = ?
                '''
        c.execute(query, (dict[species], dict[name],
            dict[gender], dict[weight],
            dict[age], animal_id))
