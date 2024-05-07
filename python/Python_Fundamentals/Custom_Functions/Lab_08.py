
# Creating a bank process

r_account = {
    'name': 'okan',
    'user name': 'resilient',
    'password': '954752',
    'account number': '744123547',
    'balance': 20000,
    'additional balance': 2000,

}

m_account = {
    'name': 'kadirhan',
    'user name': 'movement',
    'password': '116247',
    'account number': '652664324',
    'balance': 25000,
    'additional balance': 2000,

}

user_list = [m_account, r_account]


def log_in(user_name: str, password: str) -> dict:

    account = {}

    for user in user_list:
        if user.get('user name') == user_name and user.get('password') == password:

            account = user

    return account


def menu(account: dict) -> None:

    print(f"""
        Welcome! {account['name']}
        -----------------------------------------
        Please choose your process you wish to do:
        Withdraw money = withdraw
        Deposit money = deposit
        EFT/Money Order = money Transfer
        Account Info = details
        Exit = exit   
        """)


def balance_result(account: dict) -> None:
    print(f"You have {account['balance']} in your {account['account number']} TL account"
          f"Your additional balance is {account['additional balance']}")


def withdrawing_money(amount: float, account: dict) -> None:

    if account["balance"] >= amount:
        account["balance"] -= amount
        print('Please do not forget to take your money...!')
        balance_result(account)
    else:

        total_balance = account["balance"] + account["additional balance"]

        if total_balance >= amount:
            answer = input('Would you like to use additional balance? ').lower()
            match answer:
                case 'yes':
                    amount_must_be_used = amount - account["balance"]
                    account["balance"] = 0
                    account['additional balance'] -= amount_must_be_used
                    balance_result(account)
                case 'no':
                    print('Transaction has been canceled...! ')
                    balance_result(account)
        else:
            print('You do not have enough balance...!')


def depositing_money(amount: int, account: dict) -> None:
    if account["additional balance"] >= 2000:

        account["balance"] += amount
        print(f'You have deposited {amount} TL successfully...! ')
        balance_result(account)
    else:

        needed_amount = 2000 - account["additional balance"]
        transfer_amount = amount - needed_amount
        account["additional balance"] += needed_amount
        account["balance"] += transfer_amount

        print(f"You have deposited {amount} TL successfully. Since you used additional balance heretofore, "
              f"{needed_amount} TL has been transfered to your additional account. ")
        balance_result(account)


def money_order_eft(receivable_account: str, sender_account: dict, amount: float) -> None:

    for user in user_list:
        if user["account number"] == receivable_account:
            if sender_account["balance"] >= amount:
                sender_account["balance"] -= amount
                user["balance"] += amount
                print('Money transfer has been completed successfully...!')
                balance_result(sender_account)
            else:
                total_balance = sender_account["balance"] + sender_account["additional balance"]

                if total_balance >= amount:
                    answer = input('Would you like to use additional balance? ').lower()

                    match answer:
                        case 'yes':
                            amount_must_be_used = amount - sender_account["balance"]
                            sender_account["balance"] = 0
                            sender_account["additional account"] -= amount_must_be_used
                            user["balance"] += amount
                            print('Money transfer has been completed successfully...!')
                            balance_result(sender_account)
                else:
                    print('You do not have enough balance...!')
        else:
            print('Please check the account number of receiver...! ')


def main():

    user_account = log_in(input('User Name: ').lower(), input('Password: '))

    if user_account != {}:
        menu(user_account)

        while True:

            process = input('Please choose your process: ')

            match process:
                case 'exit':
                    print('You are being logged out...! ')
                    break
                case 'withdraw':
                    withdrawing_money(int(input('Please type the amount you wish to withdraw: ')), user_account)
                case 'deposit':
                    depositing_money(int(input('Please type the amount you wish to deposit: ')), user_account)
                case 'money transfer':
                    money_order_eft(input('Please type the account number/Iban: '), user_account,
                                    float(input('Please type the amount: ')))
                case 'details':
                    balance_result(user_account)

    else:
        print('Please check your details..:! ')


main()
