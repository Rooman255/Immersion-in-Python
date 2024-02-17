# Задание № 8.

# 1. Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
#   * Какие вещи взяли все три друга
#   * Какие вещи уникальны, есть только у одного друга
#   * Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
#   * Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

dict_friends_with_things = {"Ivan":("food", "sleeping_bag", "first_aid_kit"), "Petr":("knife", "food", "fishing_rod"), "Oleg":("food", "fishing_rod", "knife")}

list_of_things = []
list_of_unique_items = {}


all_items = list(dict_friends_with_things.values())
must_have_item = set(all_items[0])


for key, value in dict_friends_with_things.items():

    list_of_things += value    
    
print(f"\nСписок вещей, которые взяли друзья:\n{list_of_things}\n")


all_items = list(dict_friends_with_things.values())

must_have_item = set(all_items[0])

for value in all_items:

    must_have_item = must_have_item.intersection(set(value))

print(f"\nВещи, которые взяли каждый из друзей: \n{must_have_item}")


for key, value in dict_friends_with_things.items():

    list_of_unique_items[key] = set(value).difference(must_have_item)
    
print(f"\nУникальные вещи у друзей: \n{list_of_unique_items}")
