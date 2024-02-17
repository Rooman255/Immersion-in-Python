import sys

data = [12.3, 4, 'Привет', 42, 'Привет!', 42, (1, 2, 3), 'Привет']

for i, item in enumerate(data, start=1):
    check_int = 'Целое число' if isinstance(item, int) else ''
    check_str = 'Это строковое значение, а не целое число' if isinstance(
        item, str) else ''
    print(f"Порядковый номер элемента - {i}.")
    print(f"Значение - {item} \tАдрес памяти - {id(item)} \tРазмер памяти - {sys.getsizeof(item)} \tХэш объекта - {hash(item)} \tПроверка - {check_int}{check_str}")
