class BankAccount:
    def __init__(self, balance=0):
        self.balance = float(balance)
        self.opening = float(balance)
        self.history = []

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.history.append('{:.2f} deposit for a new balance of {:.2f}'.format(
            amount, self.balance))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            self.history.append('-{:.2f} withdrawal for a new balance of {:.2f}'.format(
                amount, self.balance))

    def __str__(self):
        recent = self.history[-3:]
        if len(self.history) > 3:
            opening = self.history[-3]
            prev_balance = float(opening.split('balance of ')[1])
            prev_amount = float(opening.split(' ')[0].replace('-', ''))
            if 'deposit' in opening:
                opening_balance = prev_balance - prev_amount
            else:
                opening_balance = prev_balance + prev_amount
        else:
            opening_balance = self.opening
        result = 'Opening balance: {:.2f} euros\n'.format(opening_balance)
        i = 0
        while i < len(recent):
            result = result + recent[i] + '\n'
            i = i + 1
        result = result + 'Current balance: {:.2f} euros'.format(self.balance)
        return result
