# 1. Implementexplicitly: 2.Use builtin Python tool
# Memoization Fibonacci Sequence
# author: Kat
# date: 03/11/2022

fibonacci_cache = {}

def fibonacci(n):
    
# If we have cached the value, then return it
  if n in fibonacci_cache:
      return fibonacci_cache[n]

# Compute the Nth term

  if n == 1:
    return 1
 elif n == 2:
     return 1
 elif n > 2:
     value = fibonacci(n-1) + fibonacci(n-2)

# Cache the value and return it

 fibonacci_cache[n] = value
 return value
for n in range (1, 101):
    print(n, ":", fibonacci(n))
