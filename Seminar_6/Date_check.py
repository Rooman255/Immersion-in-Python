from datetime import datetime
from sys import argv


def check_date(date_text: str) -> bool:
    try:
        value = datetime.strptime(date_text, "%d.%m.%Y").date()

        return True
    except:
        return False


def info_year(date_text: str) -> bool:
    
    year = int(date_text.split(".")[-1])
    print(year)
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year)

        return True
    else:
        return False


if __name__ == '__main__':
    
    check_date(argv[2])