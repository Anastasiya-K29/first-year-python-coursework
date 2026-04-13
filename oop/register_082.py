class CashRegister:
    def __init__(self):
        self.total = 0.0
        self.count = 0

    def add_item(self, price):
        self.total = self.total + price
        self.count = self.count + 1

    def clear(self):
        self.total = 0.0
        self.count = 0

    def __str__(self):
        return 'Items: {}\nTotal: {:.2f}'.format(self.count, self.total)
