class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawel(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(self.name)
        self.account.display_account_info()
        return self



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


Dave = BankAccount(.1, 200)
Pan = BankAccount(.15, 100)

Dave.deposit(40).deposit(10).withdraw(30).yield_interest().display_account_info()
Pan.deposit(40).deposit(40).withdraw(20).withdraw(60).withdraw(10).withdraw(70).yield_interest().display_account_info()

BankAccount.print_all_accounts()


user1 = User("tima", "tima@tima.com")
user1.make_deposit(100).make_deposit(250).display_user_balance()
user2 = User("Phan", "T@ball.com")
user2.make_deposit(900).display_user_balance().make_withdrawel(300).display_user_balance()
