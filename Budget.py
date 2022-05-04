
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

def create_spend_chart(objects):
    spent_amounts = []
    # Get total spent in each category
    for category in objects:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(round(spent, 2))

    # Calculate percentage rounded down to the nearest 10
    total = round(sum(spent_amounts), 2)
    spent_percentage = list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), spent_amounts))

    # Create the bar chart substrings
    header = "Percentage spent by category\n"

    chart = ""
    for value in reversed(range(0, 101, 10)):
        chart += str(value).rjust(3) + '|'
        for percent in spent_percentage:
            if percent >= value:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    footer = "    " + "-" * ((3 * len(objects)) + 1) + "\n"
    descriptions = list(map(lambda category: category.description, objects))
    max_length = max(map(lambda description: len(description), descriptions))
    descriptions = list(map(lambda description: description.ljust(max_length), descriptions))
    for x in zip(*descriptions):
        footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

    return (header + chart + footer).rstrip("\n")
