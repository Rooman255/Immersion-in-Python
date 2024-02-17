

class MyArchive:


    list_numbering = []
    list_values = []

    def __new__(cls, number: int, value: str):

        instance = super().__new__(cls)
        cls.list_numbering.append(number)
        cls.list_values.append(value)

        return instance

    def __init__(self, number: int, value: str):


        self.number = number
        self.value = value


if __name__ == '__main__':
    
    my_archive_1 = MyArchive(1, "Текст_1")

    print(f"\n{my_archive_1.list_numbering} {my_archive_1.list_values}")

    my_archive_2 = MyArchive(2, "Текст_2")

    print(f"\n{my_archive_2.list_numbering} {my_archive_2.list_values}\n")

