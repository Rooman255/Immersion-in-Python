# Задание № 4.

# 1. Создайте вручную список с повторяющимися элементами
# 2. Удалите из него все элементы, которые встречаются дважды

list_with_data = [95, 47, 8, 7, 6, 5, 2, 1, 2, 47, 3, 4, 5, 6, 45, 25, 36, 47, 95]


for item in list_with_data:

    count_elements = list_with_data.count(item)

    if count_elements > 1:
         
         for i in range(count_elements):

            list_with_data.remove(item)
            

print(f"\n{list_with_data}")