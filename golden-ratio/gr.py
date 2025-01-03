n_prev = 1
n = 1

for i in range(10000):
    print(n_prev, n)
    print("Ratio: ", n / n_prev)
    print()
    new = n + n_prev

    n_prev = n
    n = new
