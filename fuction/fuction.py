def open_account():
    print("새로운 계좌가 생성되었습니다.")


def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은{0}원 입니다.".format(balance+money))
    return balance+money


def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은{0}원 입니다.".format(balance-money))
        return balance-money
    else:
        print("잔액이 부족합니다. 잔액은 {0}원 입니다.".format(balance))


def withdrow_night(balance, money):
    commission = 100
    return commission, balance - money - commission


open_account()
balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 400)
commission, balance = withdrow_night(balance, 200)
print("수수료 {0}원이며, 잔액은 {1}원 입니다.".format(commission, balance))
