from collections import namedtuple
from datetime import datetime

Deposit = namedtuple('Deposit', ['date', 'value'])
Withdraw = namedtuple('Withdraw', ['date', 'value'])

def Statement(deposits, withdraws, funds) -> None:
    print('''
        |-------------------------------------------------|
        | github/owhenrique Bank                          |
        | Account Statatement                             |
        |-------------------------------------------------|
        | Deposits:                                       |
        |                                                 |
        | date                 | value                    |''', end='')

    for deposit in deposits:
        deposit_date = datetime.strptime(deposit.date, "%Y-%m-%dT%H:%M:%S.%f")
        formatted_date = deposit_date.strftime("%d/%m/%Y %H:%M:%S")
        print(f'''
        | {formatted_date:<20} | R$ {deposit.value:>21.2f} |''', end='')
    
    print('''
        |-------------------------------------------------|
        | Withdraws:                                      |
        |                                                 |
        | date                 | value                    |''', end='')

    for withdraw in withdraws:
        withdraw_date = datetime.strptime(withdraw.date, "%Y-%m-%dT%H:%M:%S.%f")
        formatted_date = withdraw_date.strftime("%d/%m/%Y %H:%M:%S")
        print(f'''
        | {formatted_date:<20} | R$ {withdraw.value:>21.2f} |''', end='')

    print(f'''
        |-------------------------------------------------|
        | Funds: R$ {funds:>36.2f}  |
        |-------------------------------------------------|''',)
    print()
