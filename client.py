import random


class Client:
    occupied_ID = []

    def __init__(self, lower_needs, upper_needs):
        if not self.occupied_ID:
            self.ID = 1
        else:
            self.ID = self.occupied_ID[-1] + 1
        self.occupied_ID.append(self.ID)

        self.needs = random.randint(lower_needs, upper_needs)
        self.restaurants = dict()

    def __init__(self, id_, needs_, provided):      # musi byc dodatkowy parametr bo inaczej konstruktory beda
        # przyjmowac taka sama ilosc argumentow i beda sie przyslaniac
        self.ID = id_
        self.occupied_ID.append(self.ID)
        self.needs = needs_
        self.restaurants = dict()
