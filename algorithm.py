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
        self.workers_number = workers_number
        self.clients_number = clients_number
        self.restaurants_number = restaurants_number

        for i in range(restaurants_number):
            self.rest.append(restaurant.Restaurant(5, 20, 5, 10))
        for i in range(clients_number):
            self.cl.append(client.Client(1, 5))

        for r in self.rest:
            for c in self.cl:
                distance = random.randint(1, 20)
                if distance <= r.max_distance:
                    r.clients[c] = distance
                    c.restaurants[r] = distance

        for i in range(workers_number):
            self.workers.append(worker.Worker(self.cl, self.rest))

    def cycle(self):
        for w in self.workers:
            w.do_work()
            w.count()
        self.ranking()
        self.death()
        self.give_birth()

    def ranking(self):
        self.workers.sort(key=attrgetter('quality'), reverse=False)
        # for w in self.workers:
        #     print(w.ID)

    def death(self):
        for w in self.workers[-(self.workers_number // 3):]:
            w.occupied_ID.remove(w.ID)
        self.workers = self.workers[0:-(self.workers_number // 3)]

    def give_birth(self):  # repopulating workers # TODO: prawdopodobieństwo zostania rodzicem, operatory krzyżowania i mutacji
        random.shuffle(self.workers)
        for i in range(0, len(self.workers), 2):
            print("pair ", i)
            conns = []
            for c in self.workers[i].connections:
                if c[0] <= self.clients_number / 2:
                    conns.append(c)
            for c in self.workers[i + 1].connections:
                if c[0] > self.clients_number / 2:
                    conns.append(c)
            self.workers.append(worker.Worker(self.cl, self.rest, conns))
            self.workers[-1].count()
