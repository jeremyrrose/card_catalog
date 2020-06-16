import os
from models import *
import catalog_seed
import borrower_seed

run = False
message = '\nCatalog Menu:\n1) Add an item.\n2) List catalog.\n3) Search by title.\n4) Search by author/artist.\n5) View item by catalog number.\n6) View borrowers\n0) Quit.\n\033[5m? \033[0m'
catalog = catalog_seed.catalog_seed
borrowers = borrower_seed.borrower_seed

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_int(val):
    try:
        num = int(val)
    except ValueError:
        return False
    return True

def add_item():
    print('You need administrator privileges to add items. Returning to main menu.')

    # title = input("Title: ")
    # item_type = input("Type of item \n1) Fiction \n2) Compact Disc \n")
    # if int(item_type) == 1:
    #     author = input("Author: ")
    #     publication_year = input("Publication Year:")
    #     item = Fiction(len(catalog), title, author, publication_year)
    #     catalog.append(item)
    #     print(f'You added {title} to your library.')

def print_list(list):
    if len(list) > 0:
        print(f'Found {len(list)} items.\n')
        for item in list:
            item.row_print()
    else:
        print('\nNo items found.')

def search_by_title():
    input_title = input("Enter a word in the title and press Enter: ")
    result = list(filter(lambda item: input_title.lower() in item.title.lower(), catalog))
    print_list(result)
    view_item()

def search_by_author():
    input_author = input("Enter the author's first or last name and press Enter: ")

    recordings = filter(lambda item: type(item).__name__ == "CompactDisc" or type(item).__name__ == "VinylRecord", catalog)
    recordings_result = list(filter(lambda item: input_author.lower() in item.artist.lower(), recordings))

    books = filter(lambda item: type(item).__name__ == "Fiction" or type(item).__name__ == "Nonfiction", catalog)
    books_result = list(filter(lambda item: input_author.lower() in item.author.lower(), books))

    print_list(recordings_result + books_result)
    view_item()

def print_borrowers(list = borrowers):
    for person in list:
        print(f'\n\033[33m{person.name}\033[0m Phone: {person.phone_number}')
        for item in person.borrowed:
            print(f'      {str(item["borrowed"])[:11]}: {item["item"].title}')

def view_item():
    input_id = input("\nEnter a catalog number to view item. Press Enter to return to menu.\n\033[5m? \033[0m")
    if not is_int(input_id):
        print('Catalog number not recognized. Returning to menu.')
        pass
    else:
        clear()        
        item_filter = list(filter(lambda item: item.cat_number == int(input_id), catalog))
        if len(item_filter) > 0:
            for key, value in vars(item_filter[0]).items():
                if key == "borrower":
                    if value == None:
                        continue
                    else:
                        print(f'\033[32mChecked out\033[0m to: \033[33m{value.name}\033[0m')
                else:
                    print(f'{key.title()}: \033[33m{value}\033[0m')
            item_options(item_filter[0])
        else:
            print('Item not found. Returning to menu.')

def check_out(item):
    clear()
    print(f'Item to loan out: \033[33m{item.title}\033[0m\nCurrent borrowers:', end='')
    for person in borrowers:
        print(f' : \033[32m{person.name}\033[0m ',end=' ')
    name = input("\nType a current borrower's name, or type another name to create new borrower.\n\033[5m? \033[0m")
    borrower_filter = list(filter(lambda b: b.name.lower() == name.lower(), borrowers))
    if len(borrower_filter) < 1:
        print(f'Adding new borrower "{name.title()}." Type 10-digit phone number to complete, or hit Enter to cancel.')
        phone_number = input()
        if len(phone_number) == 10:
            borrower = Borrower(name.title(), phone_number)
            borrowers.append(borrower)
            if item.lend(borrower):
                borrower.borrow(item)
                print(f'{item.title} has been lent to {borrower.name}.')
            else:
                print('This item is already checked out. Returning to main menu.')
        else:
            pass
    else:
        borrower = borrower_filter[0]
        if item.lend(borrower):
            borrower.borrow(item)
            print(f'{item.title} has been lent to {borrower.name}.')
        else:
            print('This item is already checked out. Returning to main menu.')

def check_in(item):
    if item.borrower:
        item.borrower.unborrow(item.title)
        item.check_in()
        print('Item checked in.')
    else:
        print('The item is not currently checked out.')


def item_options(item):
    item_class = type(item).__name__
    if item_class == 'Fiction' or item_class == "Nonfiction": 
        item_string = '\n3) Read item'
        item_methods = [
            item.read
        ]
    elif item_class == 'CompactDisc' or item_class == "VinylRecord":
        item_string = '\n3) Listen to item'
        item_methods = [
            item.listen
        ]
    elif item_class == 'Reference':
        item_string = "\n3) Look up an entry"
        item_methods = [
            item.research
        ]

    action = input(f'\nItem actions:\n1) Lend item\n2) Return item{item_string}\n\033[5m? \033[0m')

    if action == '1':
        check_out(item)

    elif action == '2':
        check_in(item)

    elif action == '3':
        if item_class == "Reference":
            entry = input("What would you like to research?\n")
            item_methods[0](entry)
        else:
            item_methods[0]()
    else:
        print('Option not recognized. Returning to main menu.')

    # print(options)

def run_catalog():
    run = True
    print('Welcome to your card catalog!')
    while run:
        command = input(message)
        if not is_int(command) or int(command) > 6:
            clear()
            print('Please enter a number from the list.')
        else:
            if int(command) == 0:
                clear()
                print('Goodbye!')
                run = False
            if int(command) == 1:
                clear()
                add_item()
            if int(command) == 2:
                clear()
                print_list(catalog)
            if int(command) == 3:
                clear()
                search_by_title()
            if int(command) == 4:
                clear()
                search_by_author()
            if int(command) == 5:
                clear()
                view_item()
            if int(command) == 6:
                clear()
                print_borrowers()
        
# seed some checkout data
catalog[3].lend(borrowers[1])
borrowers[1].borrow(catalog[3])

catalog[5].lend(borrowers[1])
borrowers[1].borrow(catalog[5])

catalog[12].lend(borrowers[2])
borrowers[2].borrow(catalog[12])

catalog[6].lend(borrowers[0])
borrowers[0].borrow(catalog[6])

clear()
run_catalog()