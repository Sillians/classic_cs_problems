"""
Memoization to the rescue

Memoization is a technique in which you store the results of computational 
tasks when they are completed so that when you need them again, 
you can look them up instead of needing to compute them a second (or millionth) time 
"""

from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1}  # our base cases

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)   # memoization
    return memo[n]

# print(fib3(50))

