class CatalogItem:
    '''
    This is the parent class for all items in the catalog.
    '''

    def __init__(self, cat_number, title):
        self.title = title
        self.cat_number = cat_number
        self.borrower = None

    def lend(self, borrower):
        if self.borrower:
            return False
        else:
            self.borrower = borrower
            return 'This item has been lent to ', borrower.name

    def check_in(self):
        self.borrower = None
