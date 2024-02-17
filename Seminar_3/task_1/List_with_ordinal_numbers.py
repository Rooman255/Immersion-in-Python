# Задание № 5.

# 1. Создайте вручную список с повторяющимися целыми числами
# 2. Сформируйте список с порядковыми номерами нечётных элементов исходного списка
# 3. Нумерация начинается с единицы

#                [ 1   2  3  4  5  6  7  8  9  10  11 12 13 14 15  16  17  18  19]

list_with_data = [95, 47, 8, 7, 6, 5, 2, 1, 2, 47, 3, 4, 5, 6, 45, 25, 36, 47, 95]

list_odd_element_numbers = []

for i in range(len(list_with_data)):

    if list_with_data[i] % 2 != 0:
        
        list_odd_element_numbers.append(i + 1)

print(f"\n{list_odd_element_numbers}")
