import client
import restaurant
import worker
import algorithm
import random

alg = algorithm.Algorithm(clients_number=100,restaurants_number=50,workers_number=96,cycles_number=500)
alg.cycle()
print("done")
