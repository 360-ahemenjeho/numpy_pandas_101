from numpy import arange

feature = arange(6, 21)
label = (feature * 3) + 4
print(f"Dataset Features {feature}")
print(f"Labels {label}")
