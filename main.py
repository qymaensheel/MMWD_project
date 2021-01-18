import test_workers
import test_cycles
import test_mutations

isDataProvided = False

print("[1] - Korzystaj z danych w plikach txt")
print("[2] - Wygeneruj losowe dane")
in1 = input()
if in1 == "1":
    isDataProvided = True
    print("Korzystam z danych z plikow txt...")
else:
    print("Korzystam z losowych danych...")
print("\n")


print("[1] - wykonaj test na rozna ilosc workerow")
print("[2] - wykonaj test na rozna ilosc cykli")
print("[3] - wykonaj test na rozne wspolczynniki mutacji")
in2 = input()
if in2 == "1":
    print("Wykonuje test na rozna ilosc workerow...")
    test_workers.run(isDataProvided)
elif in2 == "2":
    print("Wykonuje test na rozna ilosc cykli...")
    test_cycles.run(isDataProvided)
elif in2 == "3":
    print("Wykonuje test na rozne wspolczynniki mutacji...")
    test_mutations.run(isDataProvided)
else:
    print("Błędny wybór")

print("\n")
