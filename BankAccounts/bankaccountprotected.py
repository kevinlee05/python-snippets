class AccountP(object):
    def __init__(self, name, account_number, initial_amount):
        self._name = name
        self._no = account_number
        self._balance = initial_amount

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def get_balance(self):
        return self._balance

    def dump(self):
        s = '%s, %s, _balance: %s' %(self._name, self._no, self._balance)
        print(s)

a1 = AccountP('John Olsson', '19371554951', 20000)
a1.deposit(1000)
a1.withdraw(4000)
a1.withdraw(3500)
a1.dump()

print(a1.get_balance()) #correct way of viewing the balance
