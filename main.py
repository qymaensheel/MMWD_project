import copy
import matplotlib.pyplot as plt
import algorithm

top1 = []
top2 = []
top3 = []
alg_base = algorithm.Algorithm(clients_number=100,restaurants_number=50, mutation_probability=0.66)

for i in range(5):
    alg1 = copy.deepcopy(alg_base)
    alg1.genetic_alg(50, 96)
    top1.append(alg1.best[-1])
    alg2 = copy.deepcopy(alg_base)
    alg2.genetic_alg(100, 96)
    top2.append(alg2.best[-1])
    alg3 = copy.deepcopy(alg_base)
    alg3.genetic_alg(150, 96)
    top3.append(alg3.best[-1])

plt.scatter(range(5), top1)
plt.show()
plt.xticks(range(5))
print("done")
