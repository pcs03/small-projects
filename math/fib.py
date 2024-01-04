import time


cache = {}
def fib(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    

    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

def fib_dyn(n):
    cache = {}

    cache[0] = 0
    cache[1] = 1

    for i in range(2, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[n]


starttime = time.time()
print(fib(100))
print(time.time() - starttime)

starttime = time.time()
print(fib_dyn(100))
print(time.time() - starttime)
