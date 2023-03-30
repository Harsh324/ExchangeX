from kyc import KYCForm, kyc_form
from login import UserManager
import Exchange.exchange.exchange_functions as Ex

import User.user.user_functions as User

print("1. Fill kyc form")
print("2. Login/Register")
choose = input("\nChoose option : ")

if(choose == '1'):
    kyc = KYCForm()
    kyc_form()

elif(choose == '2'):
    user_manager = UserManager('databases/users.db')
    print("1. Register")
    print("2. Login")
    choice = input("\nEnter your choice: ")
    if choice == '1':
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        user_manager.register(username, password)
    elif choice == '2':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user_manager.login(username, password)
    else:
        print("Invalid choice. Please try again.")