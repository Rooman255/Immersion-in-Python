import Menu


def account_replenishment():
    Menu.counter += 1
    Menu.in_your_bank_account += Menu.amount
    result = f'Счёт пополнен на {Menu.amount} руб. на Вашем банковском счёте {Menu.in_your_bank_account} руб.'
    Menu.list_result.append(result)
    print(result)
