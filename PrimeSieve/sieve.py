
"""	Working with yield and generators to manage infinite data structures.

	Nats: generates the set of all natural numbers.
	Sieve: generates the set of all primes by skipping any number evenly divisible by a previously discovered prime.
"""

def nats(n) :
	yield n
	yield from nats(n + 1)

def sieve(s) :
	n = next(s)
	yield n
	yield from sieve(i for i in s if (i % n != 0))

natural = nats(2)
print(natural)
print(next(natural))
print(next(natural))
print(next(natural))
print(next(natural))
print(next(natural))
print(next(natural))
print(next(natural))
print(next(natural))
print(next(natural))
print(next(natural))

prime = sieve(nats(2))
print(prime)
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
