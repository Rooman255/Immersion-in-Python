# Задание № 3.

# 1. Создайте вручную кортеж содержащий элементы разных типов.

# 2. Получите из него словарь списков, где:
#           ключ — тип элемента,
#           значение — список элементов данного типа.


tuple_with_data = (123, 'Кортеж', True, 24.5, ["text", 45])

dictionary_of_lists = {}



for item in tuple_with_data:
    
    item_type = type(item)
    
    if item_type in dictionary_of_lists:
        
        dictionary_of_lists[item_type].append(item)
        
    else:
        
        dictionary_of_lists[item_type] = [item]


print(f"\n{dictionary_of_lists}")

