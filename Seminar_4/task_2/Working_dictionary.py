def dict_kwargs(**kwargs):

    dict_reverse = dict()

    for key, value in kwargs.items():

        if isinstance(value, (list, dict, set)):

            value = str(value)

        dict_reverse[value] = key

    return dict_reverse


def print_initial_data():

    print(
        '\nИсходные данные: \ncars=["Mercedes", "BMW", "Audi"], trees=["Oak", "Maple", "Aspen"], mobile_phone = {"Smartphone" : "Android", "Iphone": "IOS"}\n')


def print_dict_reverse():

    print(
        f'\nРезультат: \n{dict_kwargs(cars=["Mercedes", "BMW", "Audi"], trees=["Oak", "Maple", "Aspen"], mobile_phone = {"Smartphone" : "Android", "Iphone": "IOS"})}\n')


def main():

    print_initial_data()
    print_dict_reverse()


if __name__ == '__main__':
    main()
