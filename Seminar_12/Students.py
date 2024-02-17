import csv
from functools import reduce
from pathlib import Path
import Validate


class Student:

    first_name = Validate.Validate()
    middle_name = Validate.Validate()
    last_name = Validate.Validate()
    _lessons = None

    def __init__(self, first_name: str, middle_name: str, last_name: str, lessons: Path):

        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.lessons = lessons

    @property
    def lessons(self):

        return self._lessons

    @lessons.setter
    def lessons(self, less: Path):

        if self.lessons is not None:
            raise AttributeError(f'Список предметов')

        self._lessons = {"lessons": {}}

        with open(less, 'r', encoding='utf-8') as csv_file:

            reader = csv.reader(csv_file)

            for row in reader:

                self._lessons["lessons"][row[0]] = {"grade": [],
                                                    "testing": [],
                                                    "middle_grade_testing": None}

        self._lessons["middle_grade"] = None

    def grade(self, name_of_lesson: str, number: int, type_est: str = "lesson"):

        if name_of_lesson not in self.lessons["lessons"].keys():

            raise AttributeError("Урок отсутствует")

        if type_est == "lesson":

            if number < 1 or number > 5:

                raise ValueError("Диапазона оценки от 1 до 5)")

            self.lessons["lessons"][name_of_lesson]["grade"].append(number)
            self.lessons["middle_grade"] = self.middle_grade(self.lessons)

        elif type_est == "testing":

            if number < 0 or number > 100:

                raise ValueError(
                    "Диапазона оценки тестирования от 0 до 100 баллов")

            self.lessons["lessons"][name_of_lesson]["testing"].append(number)

            self.lessons["lessons"][name_of_lesson]["middle_grade_testing"] = \
                reduce(lambda x, y: x + y, self.lessons["lessons"][name_of_lesson]["testing"]) / \
                len(self.lessons["lessons"][name_of_lesson]["testing"])

    @staticmethod
    def middle_grade(lessons: dict):
        all_estimates = []
        [all_estimates.extend(lessons["lessons"][name]["grade"])
         for name in lessons["lessons"]]
        return reduce(lambda x, y: x + y, all_estimates) / len(all_estimates)

    def __repr__(self):

        full_name_student = f'\nФ.И.О студента: \n{self.first_name} {self.middle_name} {self.last_name} \n\nСредняя оценка - {self.lessons["middle_grade"]}\n\n'

        for key, value in self.lessons["lessons"].items():

            full_name_student += f'{key} - {value["middle_grade_testing"]} средний бал по тестированию\n'

        return full_name_student
