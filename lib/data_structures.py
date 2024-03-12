spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names_list = [spicy_food.get("name") for spicy_food in spicy_foods]

    return names_list
    

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for spicy_food in spicy_foods:
        if spicy_food.get("heat_level") > 5:
            spiciest_foods.append(spicy_food)
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        print(spicy_food.get("name"), end = " ")
        print(f"({spicy_food.get('cuisine')})", end = " | ")
        print("Heat Level:", end = " ")
        print(spicy_food.get("heat_level") * '🌶')

print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if cuisine == spicy_food.get("cuisine"):
            return spicy_food
        
get_spicy_food_by_cuisine(spicy_foods, "American")

def print_spiciest_foods(spicy_foods):
    for spicy_food in spicy_foods:
        if spicy_food.get("heat_level") > 5:
            print(spicy_food.get("name"), end = " ")
            print(f"({spicy_food.get('cuisine')})", end = " | ")
            print("Heat Level:", end = " ")
            print(spicy_food.get("heat_level") * '🌶')

def get_average_heat_level(spicy_foods):
    sum_heat_level = 0
    for spicy_food in spicy_foods:
        sum_heat_level += spicy_food.get("heat_level")
        average = sum_heat_level / len(spicy_foods)
    return average    


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
