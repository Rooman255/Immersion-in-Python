original_list = [9, 6, 5, 7, 4, 3, 4, 1, 6,
                 7, 5, 4, 9, 7, 6, 5, 5, 4, 2, 6, 7, 5]

resulting_list = []

for item in original_list:

    if original_list.count(item) > 1:

        resulting_list.append(item)

print(f"\nИсходный список -  {original_list}\n")

print(f"\nРезультирующий список - {list(set(resulting_list))}\n")
