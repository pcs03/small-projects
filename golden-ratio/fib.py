from functools import cache

@cache
def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n

    return fib(n - 1) + fib(n - 2)

for n in range(1, 10000):

    print(fib(n + 1) / fib(n))
