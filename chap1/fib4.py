from functools import lru_cache

@lru_cache(maxsize=None)
def fib4(n: int) -> int:  # same definition as fib2()
    if n < 2:   # Base case
        return n
    return fib4(n - 1) + fib4(n - 2) #recursive case

# print(fib4(5))
# print(fib4(50))