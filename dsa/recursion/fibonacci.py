# Brute force algorithm
def fibo(n: int):
    assert isinstance(n, int), f"The provided value must be an integer, not {type(n)}"
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        first_num = 0
        second_num = 1
        next_term = first_num + second_num
        i = 3

        while i <= n:
            i+=1
            first_num = second_num
            second_num = next_term
            next_term = first_num + second_num
        return next_term

print(fibo(9))


# Better improvement of the first algorithm
def fibonacci_gen(stop: int):
    current_fib, next_fib = 0, 1
    for _ in range(0, stop):
        fib_number = current_fib
        current_fib, next_fib = (
            next_fib, current_fib + next_fib
        )
    return current_fib

print(fibonacci_gen(9))


# using Recursive method
def fibonacci(n: int) -> None:
    assert isinstance(n, int), f"The provided value must be an integer, not {type(n)}"
    
    if n < 0:
        print("Incorrect input value")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1  # Base case
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # recursive case
    
print(fibonacci(9))


# improvement on using recursion method
def fibonacci(n: int):
  if n >= 3:
    return fibonacci(n-1) + fibonacci(n-2)  # recursive case
  else:
    return 1     # Base case

print(fibonacci(9))