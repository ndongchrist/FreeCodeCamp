
class Category:
    def __init__(self, description):
        self.ledger = []
        self.description = description
        self.balance = 0.0

    def deposit(self, amount, description = ''):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description = ''):
        if self.balance < amount:
            return False
        elif self.balance > amount:
            self.ledger.append({"amount": -(amount), "description": description})
            self.balance -= amount
            return True    

    def get_balance(self):
        return self.balance

    def transfer(self, amount, Cat_object):
        if self.withdraw(amount, f'Transfer to {Cat_object.description}'):
            Cat_object.deposit(amount, f'Transfer from {self.description}')
            return True
        else:
            return False
    def check_funds(self, amount):
        if amount > self.balance:
            return True
        else:
            return False

    def display(self):
        for elmt in self.ledger:
            title = "{:*^30}\n".format(self.description) 
            Records = ''
            description_side = "{:<22}".format(elmt['description'])
            amount_side = "{:>8.3f}".format(elmt['amount'])
            Records += "{description_side[:22]}{amount_side[:7]}\n".format(description_side[:22], amount_side[:7])
        total = "Total: {:.2f}".format(self.balance)
        return title, Records, total
            