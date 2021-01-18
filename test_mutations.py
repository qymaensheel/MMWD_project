import numpy
import matplotlib.pyplot as plt
import algorithm

mtop1 = []
mtop2 = []
mtop3 = []
mtop4 = []
mtop5 = []

mmeans = []
mutation_count = [0.12, 0.3, 0.66, 0.9]


def run(provided):

    alg_base = algorithm.Algorithm(clients_number=100, restaurants_number=50,
                                   mutation_probability=0.66, isDataProvided=provided)
    for i in range(5):
            alg1 = algorithm.Algorithm(clients_number=100, restaurants_number=50,
                                           mutation_probability=0.12)
            alg1.generate_workers(96)
            alg1.genetic_alg(50)
            mtop1.append(alg1.best[-1])
            alg2 = algorithm.Algorithm(clients_number=100, restaurants_number=50,
                                       mutation_probability=0.3)
            alg2.generate_workers(96)
            alg2.genetic_alg(50)
            mtop2.append(alg2.best[-1])
            alg3 = algorithm.Algorithm(clients_number=100, restaurants_number=50,
                                           mutation_probability=0.66)
            alg3.generate_workers(96)
            alg3.genetic_alg(50)
            mtop3.append(alg3.best[-1])
            alg4 = algorithm.Algorithm(clients_number=100, restaurants_number=50,
                                           mutation_probability=0.9)
            alg4.generate_workers(96)
            alg4.genetic_alg(50)
            mtop4.append(alg4.best[-1])

    plt.title("Prawdopodobieństwo mutacji = 0,66")
    plt.ylabel("koszty")
    plt.xlabel("losowe dane")
    plt.scatter(range(1, 6), mtop3)
    plt.show()
    plt.xticks(range(1, 6))

    mmeans.append(numpy.mean(mtop1))
    mmeans.append(numpy.mean(mtop2))
    mmeans.append(numpy.mean(mtop3))
    mmeans.append(numpy.mean(mtop4))

    plt.title("Średnia dla rosnącego prawdopodobieństwa mutacji")
    plt.ylabel("koszty")
    plt.xlabel("prawdopodobieństwo mutacji")
    plt.scatter(mutation_count, mmeans)
    plt.xticks(mutation_count)
    plt.show()