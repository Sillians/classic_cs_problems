def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2) # There is no natural base case specified

if __name__ == "__main__":
    fib1(5) # Infinite Recursion

