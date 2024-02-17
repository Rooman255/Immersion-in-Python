# Задание № 1

#     ✔ Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит 
# уникальные (без повтора) элементы исходного списка.
# *Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.


list_repeating_numbers = [1, 2, 8, 7, 5, 4, 5, 7, 8, 4, 2, 1]
list_non_repeating_numbers = []

# Длинное решение 
for i in range(len(list_repeating_numbers)):
     if list_repeating_numbers[i] not in list_non_repeating_numbers:
         list_non_repeating_numbers.append(list_repeating_numbers[i])

print(list_non_repeating_numbers)

# Короткое решение
print(list(set(list_repeating_numbers)))
