# This code generates a Fibonacci sequence using recursion, which can be inefficient for large inputs
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

# Call the function for n = 40, which can take a while to complete
print(fibonacci(40))
