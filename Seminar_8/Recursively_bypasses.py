import os
import json
import csv
import pickle


import os


def create_folder():
    if not os.path.isdir(name_folder):
        os.mkdir(name_folder)
    if not os.path.isdir(f"{name_folder}/{name_folder_1}"):
        os.mkdir(f"{name_folder}/{name_folder_1}")


def create_files():

    for i in range(3):

        with open(f"{name_folder}/text{i}.txt", "w", encoding='utf-8') as text_file:
            text_file.write(f"Это txt файл - № {i}")

        with open(f"{name_folder}/file_csv{i}.csv", "w", encoding='utf-8') as csv_file:
            csv_file.write(f"Это csv файл - № {i}")

        with open(f"{name_folder}/file_md{i}.md", "w", encoding='utf-8') as md_file:
            md_file.write(f"Это md файл - № {i}")

        with open(f"{name_folder}/file_doc{i}.doc", "w", encoding='utf-8') as doc_file:
            doc_file.write(f"Это doc файл - № {i}")

        with open(f"{name_folder}/file_xls{i}.xls", "w", encoding='utf-8') as xls_file:
            xls_file.write(f"Это xls файл - № {i}")

        with open(f"{name_folder}/file_pdf{i}.pdf", "w", encoding='utf-8') as pdf_file:
            pdf_file.write(f"Это pdf файл - № {i}")

        with open(f"{name_folder}/{name_folder_1}/file_ppt{i}.ppt", "w", encoding='utf-8') as ppt_file:
            ppt_file.write(f"Это ppt файл - № {i}")


def getting_size(path):

    count = 0

    for path_folder, directory_names, file_names in os.walk(path):

        for file in file_names:

            connects_given_path = os.path.join(path_folder, file)
            count += os.path.getsize(connects_given_path)

    return count


def directory_crawler(path_to_folder):

    intelligence = []

    for root, folders, files in os.walk(path_to_folder):

        for name in files:

            path_full = os.path.join(root, name)
            intelligence.append({"parent_directory": root,
                                 "is_file": True,
                                 "name": name,
                                 "size_in_bytes": os.path.getsize(path_full)})

        for name in folders:

            path_full = os.path.join(root, name)
            intelligence.append({"parent_directory": root,
                                 "is_file": False,
                                 "name": name,
                                 "size_in_bytes": getting_size(path_full)})

    with open("info.json", "w") as file_json:
        json.dump(intelligence, file_json)

    with open("info.csv", "w") as file_csv:
        writer = csv.DictWriter(file_csv, fieldnames=intelligence[0].keys())
        writer.writeheader()
        writer.writerows(intelligence)

    with open("info.pickle", "wb") as file_pickle:
        pickle.dump(intelligence, file_pickle)


if __name__ == "__main__":

    name_folder = 'folder'
    name_folder_1 = 'folder_1'
    create_folder()
    create_files()
    directory_crawler("./folder")
