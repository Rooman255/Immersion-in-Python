import os

file_path = r'C:\Users\User_11\Desktop\Seminar_5\README.MD'


def file_info(file_path):
    path, filename = os.path.split(file_path)
    name, extension = os.path.splitext(filename)
    return path, name, extension


print(file_info(file_path))
