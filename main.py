import copy
import matplotlib.pyplot as plt
import algorithm

top1 = []
top2 = []
top3 = []
alg_base = algorithm.Algorithm(clients_number=100, restaurants_number=50,
                               mutation_probability=0.66, isDataProvided=True)

# rozne liczby cykli
# alg_base.generate_workers(96)
#
# for i in range(5):
#     alg1 = copy.deepcopy(alg_base)
#     alg1.genetic_alg(50)
#     top1.append(alg1.best[-1])
#     alg2 = copy.deepcopy(alg_base)
#     alg2.genetic_alg(100)
#     top2.append(alg2.best[-1])
#     alg3 = copy.deepcopy(alg_base)
#     alg3.genetic_alg(150)
#     top3.append(alg3.best[-1])


# rozne liczby populacji
for i in range(5):
    alg1 = copy.deepcopy(alg_base)
    alg1.generate_workers(96)
    alg1.genetic_alg(50)
    top1.append(alg1.best[-1])
    alg2 = copy.deepcopy(alg_base)
    alg2.generate_workers(144)
    alg2.genetic_alg(50)
    top2.append(alg2.best[-1])
    alg3 = copy.deepcopy(alg_base)
    alg3.generate_workers(192)
    alg3.genetic_alg(50)
    top3.append(alg3.best[-1])

# sprawdzanie wynikow tylko dla liczby populacji = 96!!!!!
plt.scatter(range(5), top1)
plt.show()
plt.xticks(range(5))

print("done")
