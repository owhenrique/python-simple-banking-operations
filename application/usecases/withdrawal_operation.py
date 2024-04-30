import datetime

def Withdraw(daily_withdraws, account_balance, daily_withdrawal_limit) -> float and str:
    if daily_withdraws >= daily_withdrawal_limit:
        print("The daily withdrawal limit has already been reached!")
        return
    
    print('''
        |-------------------------------------------------|
        | github/owhenrique Bank                          |
        |-------------------------------------------------|
        | Input a positive value to withdraw:             |
        |-------------------------------------------------|''', end='')

    value = float(input('''
        | Value: '''))
    
    if value > 500:
        print('''
        |-------------------------------------------------|
        | The withdrawal value exceeds the account's      |
        | withdrawal limit, type a value bellow R$500!    |
        |-------------------------------------------------|''')
        
        value = float(input('''
        | Value: '''))

    if value > account_balance:
        print(f'''
        |-------------------------------------------------|
        | The withdrawal value exceeds the account's      |
        | balance amount, type a value bellow R${account_balance:.2f}!  |
        |-------------------------------------------------|''')

        value = float(input('''
        | Value: '''))
    
    return value, datetime.datetime.now().isoformat()
    
    