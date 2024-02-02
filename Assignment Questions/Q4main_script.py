# Q4main_script.py
import Q4math_operations

# Scenario 1: Check prime numbers in the interval
start_interval = 10
end_interval = 30
prime_numbers = Q4math_operations.get_primes_in_interval(start_interval, end_interval)
print(f"Prime numbers between {start_interval} and {end_interval}: {prime_numbers}")

# Scenario 2: Check Armstrong numbers in the interval
start_interval = 100
end_interval = 1000
armstrong_numbers = Q4math_operations.get_armstrong_numbers_in_interval(start_interval, end_interval)
print(f"Armstrong numbers between {start_interval} and {end_interval}: {armstrong_numbers}")

# Scenario 3: Generate Fibonacci series
fibonacci_length = 10
fibonacci_series = Q4math_operations.generate_fibonacci_series(fibonacci_length)
print(f"Fibonacci series of length {fibonacci_length}: {fibonacci_series}")
