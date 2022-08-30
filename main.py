from Customer_account import CustomerAccount

cust = CustomerAccount()


def welcome_screen():
    print('**** Welcome To Access Bank ****')
    user_input = int(input('1. Check Balance\n'
                           '2. Deposite\n'
                           '3. Withdraw\n'
                           '4. Cancel\n\n'
                           'Enter Your Request: '))

    user_options(user_input)


# function to display customers balance
def user_balance():
    print(f'Your Account Balance Is GHC:{cust.check_balance()}')


# function to deposite into customer's account
def user_deposite():
    amount = float(input('Enter Amount To Deposite: '))
    if amount > 0:
        cust.deposite(amount)
        print('Deposite Successfully Done')
    else:
        print('Unable To Deposite, Try Again.')


# function to withdraw from customer's account.
def user_withdraw():
    amount = float(input('Enter Amount To Withdraw : '))
    if amount > 0:
        if cust.check_balance() < amount:
            print(f'Amount GHC: {amount} was unable to process, due to insufficient balanace.')
        else:
            cust.withdarw(amount)
            print(f'GHC:{amount} withdraw Successfully Done, Your Balance is GHC:{cust.check_balance()} ')
    else:
         print('Unable to process request , Try Again.')

#cancel

def user_options(user_input):
    if user_input == 1:
        user_balance()
        welcome_screen()

    elif user_input == 2:
        user_deposite()
    elif user_input == 3:
        user_withdraw()
    elif user_input == 4:
        pass
    else:
        print('Invalid Request')


welcome_screen()
