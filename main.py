import sys
from collections import namedtuple

from application.utils.menu import Menu
from application.usecases.statement_operation import Statement

def main():
    menu_option = Menu()
    while menu_option != 'q':
        if menu_option == 's':
            Deposit = namedtuple('Deposit', ['date', 'value'])
            Withdraw = namedtuple('Withdraw', ['date', 'value'])
            deposits = [
                Deposit(date='2024-04-29T02:36:55.437668', value=1200.45),
                Deposit(date='2024-04-29T02:36:55.437668', value=180.45)
            ]

            withdraws = [
                Withdraw(date='2024-04-29T02:36:55.437668', value=20.35),
                Withdraw(date='2024-04-29T02:36:55.437668', value=115.00)
            ]

            funds = 1234567.89
            Statement(deposits, withdraws, funds)
        break
        #Menu()

if __name__ == "__main__":
    sys.exit(main())