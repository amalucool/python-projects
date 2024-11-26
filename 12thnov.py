# Q1
def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]

# Q2
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")


# Q3
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food

# Q4
def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

# Q4
def average_heat_level(spicy_foods):
    total_heat = sum([food['heat_level'] for food in spicy_foods])
    return total_heat // len(spicy_foods)

# Q5
def get_spiciest_foods(spicy_foods):
    return {food for food in spicy_foods if food['heat_level'] > 5}

spicy_foods = [
    {'name': 'Buffalo Wings', 'cuisine': 'American', 'heat_level': 3},
    {'name': 'butter chicken', 'cuisine': 'indina', 'heat_level': 6},
    {'name': 'Kimchi', 'cuisine': 'Korean', 'heat_level': 4},
    {'name': 'Habanero Salsa', 'cuisine': 'Mexican', 'heat_level': 8},
]
print(spicy_foods)