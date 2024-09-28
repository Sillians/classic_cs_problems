# Generating Fibonacci numbers with a generator

from typing import Generator
import sys

def fib6(n: int) -> Generator:
    if n == 0: return 0 # special case
    last = 0  # initially set to fib(0)
    next = 1  # initially set to fib(1)
    
    for _ in range(1, n):
        last, next = next, last + next
        yield next # main generation step
    

if __name__ == "__main__":
    for i in fib6(50):
        print(i)


