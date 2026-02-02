from numpy import random

noise = random.random(size=15)
label = (noise * 3) + 4
print(f"Noise Dataset {noise}")
