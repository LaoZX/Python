def linear_congruential_generator(seed, a, c, m, num_randoms):
    random_numbers = []
    xn = seed

    for _ in range(num_randoms):
        xn = (a * xn + c) % m
        random_numbers.append(xn / float(m))

    return random_numbers

# Constants for the LCG (these are commonly used values)
seed = 42
a = 1664525
c = 1013904223
m = 2**32

# Generate 10 random numbers in the interval (0.0, 1.0)
random_numbers = linear_congruential_generator(seed, a, c, m, 10)
print(random_numbers)
