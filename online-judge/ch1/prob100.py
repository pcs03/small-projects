import time
from functools import cache


@cache
def recurse(n):
    if n == 1:
        return 1

    if n % 2 != 0:
        n = 3 * n + 1
    else:
        n = n / 2
    return 1 + recurse(n)


if __name__ == "__main__":
    starttime = time.time()
    with open("./data/prob100.txt", "r") as file:
        lines = file.read().splitlines()

    for line in lines:
        numbers = [int(x) for x in line.split()]

        max_cycle = -1
        for n in range(numbers[0], numbers[1] + 1):
            cycle_length = recurse(n)
            if cycle_length > max_cycle:
                max_cycle = cycle_length
        print(f"Max cycle of {numbers[0]} to {numbers[1]}: {max_cycle}")
    print(f"Time: {time.time() - starttime}")
