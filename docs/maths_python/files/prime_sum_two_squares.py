# Import math library
import math


def is_one_mod_four(n):
    # Define a function to check if a number is 1 mod 4
    return n % 4 == 1


def is_sum_of_squares(n):
    # Define a function to check if a number is a sum of two squares
    # Iterate over the possible square roots from 1 to sqrt(n)
    for i in range(1, int(math.sqrt(n)) + 1):
        # Check if the difference between n and i^2 is also a perfect square
        j = math.sqrt(n - i**2)
        if j == int(j):
            # Return the two square roots as a tuple
            return (i, int(j))
    # Return None if no such pair exists
    return None


def sieve_of_eratosthenes(n):
    # Define a function to generate primes using the Sieve of Eratosthenes algorithm
    # Create a boolean array of size n+1, initialized to True
    is_prime = [True] * (n + 1)
    # Mark 0 and 1 as not prime
    is_prime[0] = is_prime[1] = False
    # Iterate over the numbers from 2 to the square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        # If i is prime, mark all its multiples as not prime
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    # Return a list of primes by filtering the array
    return [i for i in range(2, n + 1) if is_prime[i]]


# Define the upper limit of the range
n = 100

# Generate the primes using the sieve function
primes = sieve_of_eratosthenes(n)

# Iterate over the primes and check if they are 1 mod 4 and sum of squares
for p in primes:
    if is_one_mod_four(p):
        result = is_sum_of_squares(p)
        if result:
            # Print the prime and the two squares
            print(f"{p} = {result[0]}^2 + {result[1]}^2 = {result[0]**2} + {result[1]**2}")
