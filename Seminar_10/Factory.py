class Bird:
    def __init__(self, animal_name, animal_breed, animal_age):
        self.animal_name = animal_name
        self.animal_breed = animal_breed
        self.animal_age = animal_age

    def speak(self):
        return "Кар"


class Cat:
    def __init__(self, animal_name, animal_breed, animal_age):
        self.animal_name = animal_name
        self.animal_breed = animal_breed
        self.animal_age = animal_age

    def speak(self):
        return "Мяу"


class Dog:
    def __init__(self, animal_name, animal_breed, animal_age):
        self.animal_name = animal_name
        self.animal_breed = animal_breed
        self.animal_age = animal_age

    def speak(self):
        return "Гав"


class AnimalsFactory():

    def animals(self, type_animal, animal_name, animal_breed, animal_age):

        if type_animal.lower() == "птица":
            return Bird(animal_name, animal_breed, animal_age)
        elif type_animal.lower() == "кот":
            return Cat(animal_name, animal_breed, animal_age)
        elif type_animal.lower() == "собака":
            return Dog(animal_name, animal_breed, animal_age)
        else:
            raise ValueError("Животное отсутствует!!!")


factoryAnimals = AnimalsFactory()


bird = factoryAnimals.animals("птица", "Каркуша", "Ворон", 1)
cat = factoryAnimals.animals("кот", "Матроскин", "Мейн-кун", 2)
dog = factoryAnimals.animals("собака", "Шарик", "Немецкая овчарка", 3)

print(f"\n{bird.animal_name}, порода {bird.animal_breed}, в возрасте {bird.animal_age} год(а), говорит {bird.speak()}!")
print(f"{cat.animal_name}, порода {cat.animal_breed}, в возрасте {cat.animal_age} год(а), говорит {cat.speak()}!")
print(f"{dog.animal_name}, порода {dog.animal_breed}, в возрасте {dog.animal_age} год(а), говорит {dog.speak()}!\n")
