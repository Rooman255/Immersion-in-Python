import Menu


def wealth_tax():
    percent = Menu.in_your_bank_account * Menu.interest_on_wealth
    Menu.in_your_bank_account -= percent
    result = f'Будет произведен вычет на богатство {Menu.interest_on_wealth}% в сумме {percent} руб. На Вашем банковском счёте {Menu.in_your_bank_account} руб.'
    Menu.list_result.append(result)
    print(result)