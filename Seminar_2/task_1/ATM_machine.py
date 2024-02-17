import decimal


multiplicity_number = 50
commission = decimal.Decimal(15) / decimal.Decimal(1000)
minimum_commission = decimal.Decimal(30)
maximum_commission = decimal.Decimal(600)
deposit_interest = decimal.Decimal(3) / decimal.Decimal(100)
percent_counter = 3
interest_on_wealth = decimal.Decimal(10) / decimal.Decimal(100)
wealth_tax_limit = decimal.Decimal(10_000_000)
in_your_bank_account = decimal.Decimal(0)

counter = 0

while True:

    print("Выберите действие согласно цифре")
    menu = int(
        input(f'Пополнить счёт - 1, снять со счёта деньги - 2, выйти - 0: '))
    if menu == 0:
        print(f'Заберите карту, на Вашем счету {in_your_bank_account} руб.')
        break
    if in_your_bank_account > wealth_tax_limit:
        percent = in_your_bank_account * interest_on_wealth
        in_your_bank_account -= percent
        print(
            f'Будет произведен вычет на богатство {interest_on_wealth}% в сумме {percent} руб. На Вашем банковском счёте {in_your_bank_account} руб.')
    if menu in (1, 2):
        amount = 1
        while (amount % multiplicity_number) != 0:
            amount = decimal.Decimal(
                input(f'Введите сумму кратную {multiplicity_number} руб. '))
    if menu == 1:
        counter += 1
        in_your_bank_account += amount
        result = f'Счёт пополнен на {amount} руб. на Вашем банковском счёте {in_your_bank_account} руб.'
    elif menu == 2:
        percent = amount * commission
        percent = minimum_commission if percent < minimum_commission else maximum_commission if percent > maximum_commission else percent

        if in_your_bank_account >= amount + percent:
            counter += 1
            in_your_bank_account = in_your_bank_account - amount - percent
            result = f'Произведено снятие с Вашего счёта {amount} руб. Процент за снятие составляет {percent}. на Вашем банковском счёте {in_your_bank_account} руб.'
        else:
            result = f'Недостаточно средств на Вашем счёте. Сумма с комиссией {amount + percent} руб. На Вашем счету {in_your_bank_account} руб.'
    else:
        result = f'Неверное действие для карты на которой {in_your_bank_account} руб.'
        if counter % percent_counter == 0:
            amount_percent = in_your_bank_account * deposit_interest
            in_your_bank_account += amount_percent
            result = f'{result}\nПризведено начисление на Ваш счёт {deposit_interest}% за {percent_counter} ' \
                f'операций в сумме {amount_percent} руб. на Вашем банковском счёте {in_your_bank_account} руб.'
print(result)
