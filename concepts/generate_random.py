from numpy import random

random_floats = random.random(size=(6, 6))
random_numbers = random.randint(low=1, high=6, size=5)
random_numbers_exp = random_numbers**2
print(f"Untouched {random_numbers}")
print(f"Summed {random_numbers_exp}")
