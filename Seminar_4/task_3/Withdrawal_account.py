import Menu


def withdrawal_account():

    percent = Menu.amount * Menu.commission

    percent = Menu.minimum_commission if percent < Menu.minimum_commission else Menu.maximum_commission if percent > Menu.maximum_commission else percent

    if Menu.in_your_bank_account >= Menu.amount + percent:
        Menu.counter += 1
        Menu.in_your_bank_account = Menu.in_your_bank_account - Menu.amount - percent

        result = f'Произведено снятие с Вашего счёта {Menu.amount} руб. Процент за снятие составляет {percent}. на Вашем банковском счёте {Menu.in_your_bank_account} руб.'

        Menu.list_result.append(result)

    else:
        result = f'Недостаточно средств на Вашем счёте. Сумма с комиссией {Menu.amount + percent} руб. На Вашем счету {Menu.in_your_bank_account} руб.'
        Menu.list_result.append(result)

    print(result)
