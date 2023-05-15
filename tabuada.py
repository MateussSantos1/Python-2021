tabu = int(input('Digite um número para vver a sua tabuada: '))
n = 0
vez =0
for c in range(1, 11):
    print("{} x {} = {}".format(tabu, n + c, tabu * (vez + c)))