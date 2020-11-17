import client
import restaurant
import worker
import random
from operator import attrgetter


class Algorithm:
    def __init__(self, clients_number, restaurants_number, workers_number):
        self.cl = []
        self.rest = []
        self.workers = []

        for i in range(restaurants_number):
            self.rest.append(restaurant.Restaurant(5, 10, 5, 10))
        for i in range(clients_number):
            self.cl.append(client.Client(1, 5))

        for r in self.rest:
            for c in self.cl:
                distance = random.randint(1, 20)
                if (distance <= r.max_distance):
                    r.clients[c] = distance
                    c.restaurants[r] = distance

        for i in range(workers_number):
            self.workers.append(worker.Worker(self.cl, self.rest))

    def cycle(self):
        for w in self.workers:
            w.do_work()
        self.ranking()

    def ranking(self):
        self.workers.sort(key=attrgetter('distance_sum'),reverse=True)