#!/usr/bin/env python3.3

import curses
#import Pyro4

class Library(object):
    def __init__(self):
        self.contents = ["Ania z Zielonego Wzgorza", "Ogniem i mieczem", 
                        "Quo vadis", "Zemsta", "Wesele", "Krol Edyp", 
                        "Faraon", "Lalka", "Dzien wiatru", "Gra aniola", 
                        "Ksiezycowa dama"]

    def list_contents(self):
        return self.contents

    def lend_book(self, client, item):
        self.contents.remove(item)
        print("{0} wypozyczyl(a) {1}.".format(client,item))

    def return_book(self, client, item):
        self.contents.append(item)
        print("{0} zwrocil(a) {1}.".format(name, item))

def main():
    library = Library()