"""implement the Sieve of Eratosthenes algorithm to find all prime numbers below 100
"""
import math

def sieve_of_eratosthenes(n):
    # Define a function to generate primes using the Sieve of Eratosthenes algorithm
    # Create a boolean array of size n+1, initialized to True
    is_prime = [True] * (n+1)
    # Mark 0 and 1 as not prime
    is_prime[0] = is_prime[1] = False
    # Iterate over the numbers from 2 to the square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        # If i is prime, mark all its multiples as not prime
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    # Return a list of primes by filtering the array
    return [i for i in range(2, n+1) if is_prime[i]]


# Define the upper limit of the range
n = 100
# Generate the primes using the sieve function
primes = sieve_of_eratosthenes(n)
print(primes)