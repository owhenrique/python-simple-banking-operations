import datetime

def Deposit(balance) -> float and str:
    print('''
        |-------------------------------------------------|
        | github/owhenrique Bank                          |
        |-------------------------------------------------|
        | Input a positive value to deposit:              |
        |-------------------------------------------------|''', end='')

    value = float(input('''
        | Value: '''))
    
    if value < 0:
        print("Invalid deposit value!")
        return
    
    return value, datetime.datetime.now().isoformat()
