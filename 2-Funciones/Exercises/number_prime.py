
number_prime = lambda n: all([n % i for i in range (2,n)])

for i in range(2,100):
    n_prime = number_prime(i)
    if n_prime:
        print(i)
    