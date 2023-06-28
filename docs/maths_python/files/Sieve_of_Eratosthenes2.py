"""implement the Sieve of Eratosthenes algorithm to find all prime numbers below 100
"""

n = 100
prime = [True for i in range(n + 1)]
p = 2
while p * p <= n:
    if prime[p]:
        for i in range(p * p, n + 1, p):
            prime[i] = False
    p += 1
    while not prime[p]:
        p += 1

primes = []
for p in range(2, n):
    if prime[p]:
        primes.append(p)

print(primes)
