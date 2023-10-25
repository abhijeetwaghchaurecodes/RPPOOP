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


    def transfer_funds(self):
        sender_account_number = input("Enter sender's account number: ")
        receiver_account_number = input("Enter receiver's account number: ")

        sender_account = self.get_account(sender_account_number)
        receiver_account = self.get_account(receiver_account_number)

        if sender_account and receiver_account:
            amount = float(input("Enter the amount to transfer(INR): "))
            if sender_account.withdraw(amount):
                receiver_account.deposit(amount)
                print(f"Transfer successful. New balance for {sender_account_number}: INR{sender_account.balance}")
            else:
                print(f"Transfer failed. Insufficient balance in {sender_account_number}.")
        else:
            print("One or both of the accounts not found.")

    def list_customers(self):
        print("\nList of Customers:")
        for customer in self.customers:
            print(f"Name: {customer['name']}, Address: {customer['address']}")

    def list_accounts(self):
        print("\nList of Accounts:")
        for account in self.accounts:
            print(f"Account Number: {account.account_number}, Balance: INR{account.balance}")

    def account_statement(self):
        account_number = input("Enter account number: ")
        account = self.get_account(account_number)
        if account:
            print(f"Account Statement for Account Number: {account_number}")
            print(f"Balance: INR{account.balance}")
            # Add more details to the statement, e.g., transaction history, etc.
        else:
            print(f"Account {account_number} not found.")
            
bank = RothschildHoldings()

while True:
    print("""
        1. Open account
        2. Add customer
        3. Deposit
        4. Withdraw
        5. Display account details
        6. Exit
        7. List customers
        8. List accounts
        9. Account statement
        10. Exit
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
        bank.display()

    elif choice == '7':
        bank.list_customers()

    elif choice == '8':
        bank.list_accounts()

    elif choice == '9':
        bank.account_statement()

    elif choice == '10':
        print("Thank you for banking with Rothschild & Co.")
        break
        
    else:
        print("Invalid choice. Please try again.")


            
            
