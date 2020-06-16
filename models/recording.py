from .catalog_item import CatalogItem
import math
import random

class CompactDisc(CatalogItem):

    def __init__(self, cat_number, title, artist, publication_year, num_tracks):
        super().__init__(cat_number, title)
        self.artist = artist
        self.publication_year = publication_year
        self.num_tracks = num_tracks

    def listen(self):
        listening = True
        while listening:
            print(f'You are listening to {self.title}. This time through, you particularly enjoy Track {math.ceil(random.random() * self.num_tracks)}.')
            listening = input('You are listening on repeat. Type 0 to quit.')

    def row_print(self):
        print(f'\033[33m{str(self.cat_number).zfill(4)}\033[0m: {self.title} by {self.artist} ({type(self).__name__}) \033[32m{str("CHECKED OUT") if self.borrower else str("")}\033[0m')

class VinylRecord(CatalogItem):

    def __init__(self, cat_number, title, artist, publication_year, num_tracks):
        super().__init__(cat_number, title)
        self.artist = artist
        self.publication_year = publication_year
        self.num_tracks = num_tracks

    def listen(self):
        listening = True
        side = 'A'
        while listening:
            record_action = int(input(f'You listened to side {side} of {self.title}.\nOptions:\n0) Quit\n1) Listen again\n2) Flip side\n\033[5m? \033[0m'))
            if record_action == 0:
                listening = False
            elif record_action == 2:
                if side == 'A':
                    side = 'B'
                else:
                    side = 'A'
            else:
                continue

    def row_print(self):
        print(f'\033[33m{str(self.cat_number).zfill(4)}\033[0m: {self.title} by {self.artist} ({type(self).__name__}) \033[32m{str("CHECKED OUT") if self.borrower else str("")}\033[0m')