class BankAccount:
    bank_name = "Dojo_bank"
    accounts = []
    def __init__(self, int_rate = .10, balance = 200):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance = self.balance + amount 
        print(self.balance)
        return self
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance = self.balance - amount 
            print(self.balance)
            return self
        else:
            self.balance = self.balance - 5 
            print("insufficient funds: charging a $5 fee")
            return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
            return self
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()


Tima = BankAccount(.1, 200)
Phan = BankAccount(.15, 100)

Tima.deposit(40).deposit(10).withdraw(90).yield_interest().display_account_info()
Phan.deposit(40).deposit(40).withdraw(80).withdraw(60).withdraw(10).withdraw(70).yield_interest().display_account_info()

BankAccount.print_all_accounts()