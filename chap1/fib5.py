def fib5(n: int):
    if n == 0: return n   # special case
    last = 0  # initially set to fib(0)
    next = 1  # initially set to fib(1)
    
    for i in range(1, n):
        last, next = next, next + last
    
    return next

for i in range(11):
    print(fib5(i))
    

# With this approach, the body of the for loop will run a maximum of n - 1 times. 
# In other words, this is the most efficient version yet. Compare 19 runs of the for loop body to 21,891 
# recursive calls of fib2() for the 20th Fibonacci number. That could make a serious difference in a real-world application!

# In the recursive solutions, we worked backward. In this iterative solution, we work forward. 
# Sometimes recursion is the most intuitive way to solve a problem.

# Naive recursive solutions can also come with significant performance costs. 
# Remember, any problem that can be solved recursively can also be solved iteratively.