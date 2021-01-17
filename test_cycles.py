import numpy
import copy
import matplotlib.pyplot as plt
import algorithm

ctop1 = []
ctop2 = []
ctop3 = []
ctop4 = []
ctop5 = []
ctop6 = []
ctop7 = []
ctop8 = []
ctop9 = []
ctop10 = []
cmeans = []
cycles_count = [x*50 for x in range(1,11)]


def run(provided=False):

    alg_base = algorithm.Algorithm(clients_number=100, restaurants_number=50,
                                   mutation_probability=0.66, isDataProvided=provided)
    for i in range(5):
        alg1 = copy.deepcopy(alg_base)
        alg1.generate_workers(96)
        alg1.genetic_alg(50)
        ctop1.append(alg1.best[-1])
        alg2 = copy.deepcopy(alg_base)
        alg2.generate_workers(96)
        alg2.genetic_alg(100)
        ctop2.append(alg2.best[-1])
        alg3 = copy.deepcopy(alg_base)
        alg3.generate_workers(96)
        alg3.genetic_alg(150)
        ctop3.append(alg3.best[-1])
        alg4 = copy.deepcopy(alg_base)
        alg4.generate_workers(96)
        alg4.genetic_alg(200)
        ctop4.append(alg4.best[-1])
        alg5 = copy.deepcopy(alg_base)
        alg5.generate_workers(96)
        alg5.genetic_alg(250)
        ctop5.append(alg5.best[-1])
        alg6 = copy.deepcopy(alg_base)
        alg6.generate_workers(96)
        alg6.genetic_alg(300)
        ctop6.append(alg6.best[-1])
        alg7 = copy.deepcopy(alg_base)
        alg7.generate_workers(96)
        alg7.genetic_alg(350)
        ctop7.append(alg7.best[-1])
        alg8 = copy.deepcopy(alg_base)
        alg8.generate_workers(96)
        alg8.genetic_alg(400)
        ctop8.append(alg8.best[-1])
        alg9 = copy.deepcopy(alg_base)
        alg9.generate_workers(96)
        alg9.genetic_alg(450)
        ctop9.append(alg9.best[-1])
        alg10 = copy.deepcopy(alg_base)
        alg10.generate_workers(96)
        alg10.genetic_alg(500)
        ctop10.append(alg10.best[-1])

    plt.title("Cycles = 50")
    plt.ylabel("quality")
    plt.xlabel("random_cases")
    plt.scatter(range(1, 6), ctop1)
    plt.show()
    plt.xticks(range(1, 6))

    cmeans.append(numpy.mean(ctop1))
    cmeans.append(numpy.mean(ctop2))
    cmeans.append(numpy.mean(ctop3))
    cmeans.append(numpy.mean(ctop4))
    cmeans.append(numpy.mean(ctop5))
    cmeans.append(numpy.mean(ctop6))
    cmeans.append(numpy.mean(ctop7))
    cmeans.append(numpy.mean(ctop8))
    cmeans.append(numpy.mean(ctop9))
    cmeans.append(numpy.mean(ctop10))

    plt.title("Średnia dla rosnącej liczby cykli")
    plt.ylabel("quality")
    plt.xlabel("cycles")
    plt.scatter(cycles_count, cmeans)
    plt.xticks(cycles_count)
    plt.show()