from .catalog_item import CatalogItem

class Fiction(CatalogItem):

    def __init__(self, cat_number, title, author, publication_year):
        super().__init__(cat_number, title)
        self.author = author
        self.publication_year = publication_year

    def read(self):
        reading = True
        while reading:
            print(f'You are reading {self.title}.')
            reading = input('Press Enter to quit.')

    def row_print(self):
        print(f'\033[33m{str(self.cat_number).zfill(4)}\033[0m: {self.title} by {self.author} ({type(self).__name__}) \033[32m{str("CHECKED OUT") if self.borrower else str("")}\033[0m')

class Nonfiction(CatalogItem):

    def __init__(self, cat_number, title, author, publication_year):
        super().__init__(cat_number, title)
        self.author = author
        self.publication_year = publication_year

    def read(self):
        reading = True
        while reading:
            print(f'You are reading {self.title}. You are learning quite a lot!')
            reading = input('Press Enter to quit.')
    
    def row_print(self):
        print(f'\033[33m{str(self.cat_number).zfill(4)}\033[0m: {self.title} by {self.author} ({type(self).__name__}) \033[32m{str("CHECKED OUT") if self.borrower else str("")}\033[0m')

class Reference(CatalogItem):

    def __init__(self, cat_number, title, subject, publication_year):
        super().__init__(cat_number, title)
        self.publication_year = publication_year
        self.subject = subject

    def research(self, entry):
        while entry:
            print(f'You looked up {entry} in {self.title}. If that falls under {self.subject}, you found your answer!')
            entry = input("Type Enter to quit. Type another entry title to look it up.")

    def row_print(self):
        print(f'\033[33m{str(self.cat_number).zfill(4)}\033[0m: {self.title} ({type(self).__name__}) \033[32m{str("CHECKED OUT") if self.borrower else str("")}\033[0m')