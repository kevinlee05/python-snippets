class Account(object):
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def dump(self):
        s = '%s, %s, balance: %s' %(self.name, self.no, self.balance)
        print(s)

a1 = Account('John', '14234123', 20000)
a2 = Account('Liz', '14234123', 20000)
a1.deposit(1000)
a1.withdraw(4000)
a2.withdraw(10500)
a1.withdraw(3500)
print("a1's balance:", a1.balance)
a1.dump()
a2.dump()
