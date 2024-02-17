import decimal
from Account_replenishment import account_replenishment
from Withdrawal_account import withdrawal_account
from Wealth_tax import wealth_tax


def menu():

    global multiplicity_number
    global commission
    global minimum_commission
    global maximum_commission
    global deposit_interest
    global percent_counter
    global interest_on_wealth
    global wealth_tax_limit
    global in_your_bank_account
    global counter
    global amount
    global list_result

    multiplicity_number = 50
    commission = decimal.Decimal(15) / decimal.Decimal(1000)
    minimum_commission = decimal.Decimal(30)
    maximum_commission = decimal.Decimal(600)
    deposit_interest = decimal.Decimal(3) / decimal.Decimal(100)
    percent_counter = 3
    interest_on_wealth = decimal.Decimal(10) / decimal.Decimal(100)
    wealth_tax_limit = decimal.Decimal(10_000_000)
    in_your_bank_account = decimal.Decimal(0)

    list_result = []
    counter = 0

    while True:

        print("Выберите действие согласно цифре")
        menu = int(
            input(f'Пополнить счёт - 1, снять со счёта деньги - 2, выйти - 0: '))
        if menu == 0:

            print(
                f'Заберите карту, на Вашем счету {in_your_bank_account} руб.')
            break
        if in_your_bank_account > wealth_tax_limit:
            wealth_tax()
        if menu in (1, 2):
            amount = 1
            while (amount % multiplicity_number) != 0:
                amount = decimal.Decimal(
                    input(f'Введите сумму кратную {multiplicity_number} руб. '))
        if menu == 1:
            account_replenishment()
        elif menu == 2:
            withdrawal_account()

        else:
            result = f'Неверное действие для карты на которой {in_your_bank_account} руб.'
            if counter % percent_counter == 0:
                amount_percent = in_your_bank_account * deposit_interest
                in_your_bank_account += amount_percent
                result = f'{result}\nПризведено начисление на Ваш счёт {deposit_interest}% за {percent_counter} ' \
                    f'операций в сумме {amount_percent} руб. на Вашем банковском счёте {in_your_bank_account} руб.'
                list_result.append(result)

    print(list_result)
