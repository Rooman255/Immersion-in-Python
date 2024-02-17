import Students
from pathlib import Path


class Main:

    def main():

        name_student = Students.Student(
            "Иванов", "Иван", "Иванович", Path('lessons.csv'))

        name_student.grade("Философия", 4)
        name_student.grade("Философия", 3)
        name_student.grade("Высшая Математика", 4)
        name_student.grade("Высшая Математика", 5)
        name_student.grade("Информатика", 5)
        name_student.grade("Информатика", 4)

        name_student.grade("Философия", 53, "testing")
        name_student.grade("Философия", 78, "testing")
        name_student.grade("Высшая Математика", 69, "testing")
        name_student.grade("Высшая Математика", 84, "testing")
        name_student.grade("Информатика", 96, "testing")
        name_student.grade("Информатика", 87, "testing")

        print(name_student)

    if __name__ == '__main__':
        main()
