def getFibonacciNumbers(n):
    """Returns a list of Fibonacci numbers less than or equal to n."""
    if n < 0:
        return []  # No Fibonacci numbers for negative inputs
    
    fib_numbers = [0, 1]  # Initial two Fibonacci numbers
    while True:
        next_fib = fib_numbers[-1] + fib_numbers[-2]
        if next_fib > n:
            break
        fib_numbers.append(next_fib)
    
    return fib_numbers if n >= 1 else [0]

# Example usage
print(getFibonacciNumbers(10))  # Output: [0, 1, 1, 2, 3, 5, 8]
