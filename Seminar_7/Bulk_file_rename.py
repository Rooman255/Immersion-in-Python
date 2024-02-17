import os


def create_folder():
    if not os.path.isdir(name_folder):
        os.mkdir(name_folder)


def create_files():

    for i in range(3):

        with open(f"{name_folder}/text{i}.txt", "w", encoding='utf-8') as text_file:
            text_file.write(f"Это текстовый файл - № {i}")

        with open(f"{name_folder}/file_csv{i}.csv", "w", encoding='utf-8') as csv_file:
            csv_file.write(f"Это csv файл - № {i}")

        with open(f"{name_folder}/file_md{i}.md", "w", encoding='utf-8') as md_file:
            md_file.write(f"Это md файл - № {i}")


def bulk_file_renaming(filename_new, quantity, desired_extension, replacement_extension, letter_range, name_folder='.'):

    counter = 1

    for file_name in os.listdir(name_folder):

        if file_name.endswith(desired_extension):

            filename_is_old = os.path.splitext(file_name)[0]

            old_name_substring = filename_is_old[letter_range[0]:letter_range[1]] if letter_range else ""

            new_filename = f"{old_name_substring}{filename_new}{str(counter).zfill(quantity)}{replacement_extension}"

            os.rename(os.path.join(name_folder, file_name),
                      os.path.join(name_folder, new_filename))

            counter += 1


if __name__ == "__main__":

    name_folder = 'folder'

    create_folder()
    create_files()

    print(
        f"\nСписок имён файлов до группового переименования файлов:\n{os.listdir(name_folder)}\n")

    bulk_file_renaming("_new_file_", 3, ".txt", ".doc",
                       [0, 4], f"./{name_folder}")

    print(
        f"Список имён файлов после группового переименования файлов:\n{os.listdir(name_folder)}\n")
