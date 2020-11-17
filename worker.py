import random
import restaurant
import client

class Worker:
    occupied_ID = []


    def __init__(self, cl_list, rest_list):
        if self.occupied_ID == []:
            self.ID = 1
        else:
            self.ID = self.occupied_ID[-1] + 1
        self.occupied_ID.append(self.ID)
        self.clients_list = cl_list
        self.restaurants_list = rest_list
        self.connections = []
        self.is_old = False
        self.cost_sum = 0
        self.distance_sum = 0



    def do_work(self):
        for c in self.clients_list:
            client_needs = c.needs
            for r in self.restaurants_list:
                if client_needs==0:
                    break
                if r==self.restaurants_list[-1]:
                    n = client_needs
                else:
                    n = random.randint(0,client_needs)

                if r in c.restaurants:
                    d = c.restaurants[r]
                    self.connections.append(list([c.ID, r.ID, d, n, n*r.cost]))
                    client_needs-=n

        for i in self.connections:
            self.cost_sum+=i[4]
            self.distance_sum+=i[2]
