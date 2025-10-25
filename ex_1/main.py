import time


def caching_fibonacci():
    cache = {}
    

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci


start_time = time.time()  # Record start time
fib = caching_fibonacci()
# print(fib(900))
# print(fib(1800))
# print(fib(2600)) 
# print(fib(3500)) 
# print(fib(4300)) 
# print(fib(5100))
print(fib(10))
print(fib(15)) 
print(fib(35)) 
end_time = time.time()    # Record end time

elapsed_time = end_time - start_time
print(f"Execution time with cache: {elapsed_time:.4f} seconds")








def fibonacci_recursive(n):

    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        return 0  # Base case: 0th Fibonacci number
    elif n == 1:
        return 1  # Base case: 1st Fibonacci number
    else:
        # Recursive step: sum of the previous two Fibonacci numbers
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)





start_time = time.time()  # Record start time
print(fibonacci_recursive(35))           # Execute the function
end_time = time.time()    # Record end time

elapsed_time = end_time - start_time
print(f"Execution time without cache: {elapsed_time:.4f} seconds")