import random


class Client:
    occupied_ID = []

    def __init__(self, lower_needs, upper_needs, provided=False):
        if not provided:                #random data
            if not self.occupied_ID:
                self.ID = 1
            else:
                self.ID = self.occupied_ID[-1] + 1
            self.occupied_ID.append(self.ID)

            self.needs = random.randint(lower_needs, upper_needs)
        else:                           #predefined data
            self.ID = lower_needs
            self.occupied_ID.append(self.ID)
            self.needs = upper_needs

        self.restaurants = dict()
