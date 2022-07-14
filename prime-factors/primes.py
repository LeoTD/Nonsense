def primes(n):
    p = 2
    print("factors of " + str(n) + ":")
    while n > 1:
        while n % p == 0:
            print(p)
            n /= p
        p += 1

primes(3)
primes(10)
primes(20)
primes(27)
