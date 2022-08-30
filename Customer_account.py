class CustomerAccount:
    """This is a blueprint"""
    balance = 0.0

    def deposite(self, amount):
        self.balance += amount

    def withdarw(self, amount):
        self.balance -= amount

    def check_balance(self):
        return self.balance
