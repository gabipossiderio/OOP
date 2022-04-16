class Account:

    def __init__(self, account_number, name, balance=0):
        self._account_number = account_number
        self._name = name
        self._balance = balance

    def change_name(self, new_name):
        self._name = new_name

    def deposit(self, value):
        self._balance += value

    def bank_draft(self, value):
        if value <= self._balance:
            self._balance -= value
        else:
            print(f'Your balance is: {self._balance}. Please enter a valid amount.')


my_account = Account(444, 'Gabriella')
my_account.change_name('Jùlio')
my_account.bank_draft(20)
print(vars(my_account))
