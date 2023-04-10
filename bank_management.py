'''

define classes for accounts, customers, transactions, and the bank itself. Each class should have attributes and 
methods that correspond to their real-world counterparts. For example, the account class could have attributes like 
account number, balance, and account type, and methods like deposit(), withdraw(), and check_balance().

'''

class RothschildHoldings:
    def __init__(self):
        self.customers = []
        self.accounts = []
        print("Welcome to Rothschild & Co.")
        
    def open_account(self):
        account_number = input("Enter account number: ")
        name = input("Enter name: ")
        opening_balance = float(input("Enter opening balance(INR): "))
        account = Account(account_number, opening_balance)
        self.accounts.append(account)
        print("Account opened successfully!")
        return account
        
    def add_customer(self):
        name = input("Enter customer name: ")
        address = input("Enter customer address: ")
        customer = {'name': name, 'address': address}
        self.customers.append(customer)
        print("Customer added successfully!")
        return customer
        
        
    def deposit(self):
        account_number = input("Enter account number: ")
        account = self.get_account(account_number)
        if account:
            amount = float(input("Enter amount to deposit(INR): "))
            account.deposit(amount)
            print(f"{amount} deposited successfully into account {account_number}")
        else:
            print(f"Account {account_number} not found")
        
    def withdraw(self):
        account_number = input("Enter account number: ")
        account = self.get_account(account_number)
        if account:
            amount = float(input("Enter amount to withdraw(INR): "))
            if account.withdraw(amount):
                print("Withdrawal successful.")
                print(f"New account balance: INR{account.balance}")
            else:
                print("Withdrawal failed. Insufficient funds.")
        else:
            print(f"Account {account_number} not found.")

            
    def display(self):
        account_number = input("Enter account number: ")
        account = self.get_account(account_number)
        if account:
            print(f"Account number: {account.account_number}")
            print(f"Balance: INR{account.balance}")
        else:
            print(f"Account {account_number} not found")

            
    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None
        
    def withdraw_money(self):
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to withdraw(INR): "))
        account = self.get_account(account_number)
        if account:
            if account.withdraw(amount):
                print(f"Withdrawal successful. New balance: INR{account.balance}")
            else:
                print("Withdrawal failed. Insufficient balance.")
        else:
            print(f"Account {account_number} not found.")
        
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False


            
bank = RothschildHoldings()

while True:
    print("""
        1. Open account
        2. Add customer
        3. Deposit
        4. Withdraw
        5. Display account details
        6. Exit
    """)

    choice = input("Enter your choice: ")

    if choice == '1':
        account = bank.open_account()
        bank.accounts.append(account)

    elif choice == '2':
        customer = bank.add_customer()
        bank.customers.append(customer)

    elif choice == '3':
        bank.deposit()
    
    elif choice == '4':
        bank.withdraw()
        
    elif choice == '5':
        bank.display()
        
    elif choice == '6':
        print("Thank you for banking with Rothschild & Co.")
        break
        
    else:
        print("Invalid choice. Please try again.")


            
            
