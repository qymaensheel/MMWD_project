import random
import restaurant
import client
from operator import itemgetter


class Worker:
    occupied_ID = []
    highest_ID_given = 0

    def __init__(self, cl_list, rest_list, conns_list=[]):  # added 3rd parameter as optional
        if not self.occupied_ID:
            self.ID = 1
        else:
            self.ID = self.occupied_ID[-1] + 1
        self.occupied_ID.append(self.ID)
        self.clients_list = cl_list
        self.restaurants_list = rest_list
        self.connections = conns_list
        self.cost_sum = 0
        self.distance_sum = 0
        self.quality = 0

    def do_work(self):
        for c in self.clients_list:
            client_needs = c.needs
            for r in self.restaurants_list:
                if client_needs == 0:
                    break
                if r == self.restaurants_list[-1]:
                    n = client_needs
                else:
                    n = random.randint(0, client_needs)

                if r in c.restaurants:
                    d = c.restaurants[r]
                    self.connections.append(list([c.ID, r.ID, d, n, n * r.cost]))
                    client_needs -= n

    def count(self):
        for i in self.connections:
            self.cost_sum += i[4]
            self.distance_sum += i[2]
        self.quality = self.cost_sum + self.distance_sum

        self.connections.sort(key=itemgetter(0), reverse=False)
