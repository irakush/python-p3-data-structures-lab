import ipdb

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
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "🌶" * food["heat_level"]
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level = food["heat_level"]
            heat_pic = "🌶" * heat_level
            print(f"{name} ({cuisine}) | Heat Level: {heat_pic}")


def get_average_heat_level(spicy_foods):
    heat_sum = sum(food["heat_level"] for food in spicy_foods)
    return int(heat_sum / len(spicy_foods))

    # or

    # heat_sum = 0
    # for food in spicy_foods:
    #     heat_sum += food["heat_level"]

    # return int(heat_sum / len(spicy_foods))


def create_spicy_food(spicy_foods, spicy_food):
    return spicy_foods + [spicy_food]


# ipdb.set_trace()
