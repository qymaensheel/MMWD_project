import random


class Restaurant:
    occupied_ID = []

    def __init__(self, lower_distance, upper_distance, lower_cost, upper_cost):
        if not self.occupied_ID:
            self.ID = 1
        else:
            self.ID = self.occupied_ID[-1] + 1
        self.occupied_ID.append(self.ID)
        self.max_distance=random.randint(lower_distance, upper_distance)
        self.cost = random.randint(lower_cost, upper_cost)
        self.clients = dict()
