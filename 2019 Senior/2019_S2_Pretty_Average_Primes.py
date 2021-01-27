
def get_primes(max_num):
    # True -> is prime, False -> is not prime
    isPrime = [True for _ in range(2, max_num)]
    # isPrime[0] -> 2

    for i in range(2, int(max_num ** 0.5) + 1):

        if (isPrime[i - 2]):

            # Update all multiples of i
            for multiple in range(i * 2, max_num, i):
                isPrime[multiple - 2] = False

    primes = [i for i in range(2, max_num) if isPrime[i - 2]]

    return primes


def a_b(n):

    if n in all_primes:
        return n, n

    for i, a in enumerate(all_primes):
        b = (n * 2 - a)
        if b in all_primes:
            return a, b


t = int(input())
all_n = [int(input()) for n in range(t)]
all_primes = get_primes(max(all_n) * 2)

for n in all_n:
    print(*a_b(n))
