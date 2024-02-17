import random

bags = {"Хлеб": 69, "Вода": 15, "Соль": 52,
        "Картофель": 24, "Котелок": 25, "Спички": 15, "Нож": 33}

bag_weight = 0
bag_capacity = 100

list_things_in_bag = []


while bag_weight < bag_capacity:

    key, value = random.choice(list(bags.items()))

    if key in list_things_in_bag:

        continue

    if bag_weight + value > bag_capacity:

        break

    bag_weight += value

    list_things_in_bag += (str(key), str(value))

print(
    f"\nВещи, которые поместились в мешок - {list_things_in_bag}\nВес мешка составил -  {bag_weight}\n")
