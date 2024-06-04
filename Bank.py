class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        BankAccount.account_number_counter += 1
        self.account_number = BankAccount.account_number_counter

    def get_account_number(self):
        return self.account_number

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if self.balance < amount:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def __str__(self):
        return f"Account Number: {self.account_number}, Balance: ${self.balance:.2f}"

BankAccount.account_number_counter = 0

num_accounts = 5
accounts = []
for _ in range(num_accounts):
    account = BankAccount()
    print(account)  


