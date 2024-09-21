# sample 1 (Brute force method)
def factorial(n: int) -> int:
  assert isinstance(n, int), f"The value must be an integer, and not {type(n)}"

  if n == 1 or n == 0:
    return 1
  elif n == 2:
    return 2
  else:
    count = 1
    fac_value = n * (n-1)

    for i in range(1, n-1):
      count += 1
      next_value = (n-count)
      fac_value *= next_value
    return fac_value

print(factorial(5))


# sample 2 (Brute force method)
n = 10
i = 1
j = n * (n-1)

for i in range(1, n-1):
  i+=1 
  v = (n-i)
  j *= v
print(j)


# sample 3 using recursion
def fact(n: int) -> int:
  if n > 1:
    return (n * fact(n-1))
  return 1

print(fact(5))