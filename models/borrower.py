import datetime

class Borrower:

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.borrowed = []
        self.returned = []

    def borrow(self, item):
        loan_record = {
            'item': item,
            'borrowed': datetime.datetime.now()
        }
        self.borrowed.append(loan_record)
        item.lend(self)

    def unborrow(self, item_title):
        self.borrowed = list(filter(lambda x: x["item"].title is not item_title, self.borrowed))