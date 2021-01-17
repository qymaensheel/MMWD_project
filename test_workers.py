import numpy
import copy
import matplotlib.pyplot as plt
import algorithm

ptop1 = []
ptop2 = []
ptop3 = []
ptop4 = []
ptop5 = []
ptop6 = []
ptop7 = []
ptop8 = []
ptop9 = []
ptop10 = []
pmeans = []
workers_count = [33, 66, 96, 129, 156, 198, 234, 267, 300, 345]


def run(provided=False):

    alg_base = algorithm.Algorithm(clients_number=100, restaurants_number=50,
                                   mutation_probability=0.66, isDataProvided=provided)

    for i in range(5):
        alg1 = copy.deepcopy(alg_base)
        alg1.generate_workers(workers_count[0])
        alg1.genetic_alg(50)
        ptop1.append(alg1.best[-1])
        alg2 = copy.deepcopy(alg_base)
        alg2.generate_workers(workers_count[1])
        alg2.genetic_alg(50)
        ptop2.append(alg2.best[-1])
        alg3 = copy.deepcopy(alg_base)
        alg3.generate_workers(workers_count[2])
        alg3.genetic_alg(50)
        ptop3.append(alg3.best[-1])
        alg4 = copy.deepcopy(alg_base)
        alg4.generate_workers(workers_count[3])
        alg4.genetic_alg(50)
        ptop4.append(alg4.best[-1])
        alg5 = copy.deepcopy(alg_base)
        alg5.generate_workers(workers_count[4])
        alg5.genetic_alg(50)
        ptop5.append(alg5.best[-1])
        alg6 = copy.deepcopy(alg_base)
        alg6.generate_workers(workers_count[5])
        alg6.genetic_alg(50)
        ptop6.append(alg6.best[-1])
        alg7 = copy.deepcopy(alg_base)
        alg7.generate_workers(workers_count[6])
        alg7.genetic_alg(50)
        ptop7.append(alg7.best[-1])
        alg8 = copy.deepcopy(alg_base)
        alg8.generate_workers(workers_count[7])
        alg8.genetic_alg(50)
        ptop8.append(alg8.best[-1])
        alg9 = copy.deepcopy(alg_base)
        alg9.generate_workers(workers_count[8])
        alg9.genetic_alg(50)
        ptop9.append(alg9.best[-1])
        alg10 = copy.deepcopy(alg_base)
        alg10.generate_workers(workers_count[9])
        alg10.genetic_alg(50)
        ptop10.append(alg10.best[-1])



    pmeans.append(numpy.mean(ptop1))
    pmeans.append(numpy.mean(ptop2))
    pmeans.append(numpy.mean(ptop3))
    pmeans.append(numpy.mean(ptop4))
    pmeans.append(numpy.mean(ptop5))
    pmeans.append(numpy.mean(ptop6))
    pmeans.append(numpy.mean(ptop7))
    pmeans.append(numpy.mean(ptop8))
    pmeans.append(numpy.mean(ptop9))
    pmeans.append(numpy.mean(ptop10))

    print("done")



    plt.title("Populacja = 33")
    plt.ylabel("quality")
    plt.xlabel("random_cases")
    plt.scatter(range(1, 6), ptop1)
    plt.show()
    plt.xticks(range(1, 6))


    plt.title("Średnia dla rosnących populacji")
    plt.ylabel("quality")
    plt.xlabel("growing population")
    plt.scatter(workers_count, pmeans)
    plt.xticks(workers_count)
    plt.show()
