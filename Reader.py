#!/usr/bin/env python3.3
#import Pyro4

class Reader(object):
    def __init__(self, client):
        self.client = client

    def visit(self, library):
        print("To jest {0}.".format(self.client))
        self.give_back(library)
        self.borrow(library)
        print("Dziekujemy.")

    def give_back(self, library):
        print("Zawartosc biblioteki: ", library.list_contents())
        item = input("Wpisz tytul ksiazki, ktora chcesz oddac: ").strip()
        if item:
            library.return_book(self.client, item)

    def borrow(self, library):
        print("Zawartosc biblioteki: ",library.list_contents())
        item = input("Wpisz tytul ksiazki, ktora chcesz wypozyczyc: ").strip()
        if item:
            library.lend_book(self.client, item)
