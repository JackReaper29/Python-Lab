# Q4math_operations.py

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_primes_in_interval(start, end):
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes

def is_armstrong_number(num):
    order = len(str(num))
    sum_of_powers = sum(int(digit) ** order for digit in str(num))
    return num == sum_of_powers

def get_armstrong_numbers_in_interval(start, end):
    armstrong_numbers = [num for num in range(start, end + 1) if is_armstrong_number(num)]
    return armstrong_numbers

def generate_fibonacci_series(n):
    fibonacci_series = [0, 1]
    while len(fibonacci_series) < n:
        fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])
    return fibonacci_series
