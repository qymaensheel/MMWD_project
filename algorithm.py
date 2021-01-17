import client
import restaurant
import worker
import random
from operator import attrgetter


class Algorithm:
    def __init__(self, clients_number, restaurants_number, mutation_probability, isDataProvided=False):
        self.cl = []
        self.rest = []
        self.workers = []
        self.clients_number = clients_number
        self.restaurants_number = restaurants_number
        self.mutation_probability = mutation_probability
        self.probability = []
        self.worst = []
        self.best = []
        self.workers_number = 0

        dtxt = []

        if not isDataProvided:
            for i in range(restaurants_number):
                self.rest.append(restaurant.Restaurant(lower_distance=5, upper_distance=20, lower_cost=5, upper_cost=10))
            for i in range(clients_number):
                self.cl.append(client.Client(1, 5))

            for r in self.rest:
                dtxt.append([])
                for c in self.cl:
                    distance = random.randint(1, 20)
                    if distance <= r.max_distance:
                        r.clients[c] = distance
                        c.restaurants[r] = distance
                        dtxt[-1].append(distance)
                    else:
                        dtxt[-1].append(0)
            # for c in dtxt:
            #     print(c)
            # with open('distsData.txt', 'a') as f:
            #     for c in dtxt:
            #         for i in c:
            #             f.write(str(i)+"\t")
            #         f.write("\n")

        else:
            restsFile = open("restsData.txt")
            restsString = restsFile.read().split("\n")
            restsTable = []
            for r in restsString:
                restsTable.append(list(map(int, r.split("\t"))))
            for r in restsTable:
                self.rest.append(restaurant.Restaurant(r[0], r[1], r[2]))
            restsFile.close()

            clientsFile = open("clientsData.txt")
            clientsString = clientsFile.read().split("\n")
            clientsTable = []
            for c in clientsString:
                clientsTable.append(list(map(int, c.split("\t"))))
            for c in clientsTable:
                self.cl.append(client.Client(c[0], c[1], True))
            clientsFile.close()

            distsFile = open("distsData.txt")
            distsString = distsFile.read().split("\n")
            distsTable = []
            for d in distsString:
                l = list(map(int, d.split("\t")))
                distsTable.append(l)
            distsFile.close()
            for r in self.rest:
                for c in self.cl:
                    distance = distsTable[r.ID-1][c.ID-1]
                    if distance > 0:
                        r.clients[c] = distance
                        c.restaurants[r] = distance

    def generate_workers(self, workers_number):
        self.workers = []
        self.workers_number = workers_number
        for i in range(self.workers_number):
            self.workers.append(worker.Worker(self.cl, self.rest))
        for w in self.workers:
            w.do_work()

    def genetic_alg(self, cycles):
        for i in range(cycles):
            self.ranking()
            self.death()
            self.probability_birth()
            self.give_birth()
            self.worst.append(self.workers[-1].quality)
            self.best.append(self.workers[0].quality)
        self.ranking()

    def ranking(self):
        self.workers.sort(key=attrgetter('quality'), reverse=False)

    def probability_birth(self):
        quality_sum = 0
        self.probability = []
        for i in self.workers:
            quality_sum = quality_sum + i.quality
        for i in self.workers:
            self.probability.append(quality_sum-i.quality/quality_sum*100)

    def death(self):
        del self.workers[-(self.workers_number // 3):]

    def give_birth(self):
        pairs = []
        for i in range(len(self.workers)//2):
            one_pair = []
            while len(one_pair)<2:
                one_worker = random.choices(self.workers, self.probability, k=1)[0]
                if one_worker not in one_pair:
                    one_pair.append(one_worker)
            pairs.append(one_pair)

        for i in pairs:
            conns = []
            random_conns = random.sample(range(1, self.clients_number+1), self.clients_number//2)

            mutation_choice = random.randint(0, 10)/100
            if mutation_choice <= self.mutation_probability:
                mutation_con = random_conns[-1]
                random_conns.remove(random_conns[-1])
                mutation_needs = self.cl[mutation_con-1].needs
                for r in self.rest:
                    if mutation_needs == 0:
                        break
                    if r == self.rest[-1]:
                        n = mutation_needs
                    else:
                        n = random.randint(0, mutation_needs)

                    if r in self.cl[mutation_con-1].restaurants and n!=0:
                        d = self.cl[mutation_con-1].restaurants[r]
                        conns.append(list([self.cl[mutation_con-1].ID, r.ID, d, n, n * r.cost]))
                        mutation_needs -= n

            for c in i[0].connections:
                if c[0] in random_conns:
                    conns.append(c)
            for c in i[1].connections:
                if c[0] not in random_conns and c[0] != mutation_con:
                    conns.append(c)
            new_worker = worker.Worker(self.cl, self.rest, conns)
            new_worker.count()
            self.workers.append(new_worker)

