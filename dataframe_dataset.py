from numpy import random
from pandas import DataFrame

rows = random.randint(low=1, high=99, size=(5, 2))
features = ["Wins", "Losses"]
dataset = DataFrame(data=rows, columns=features)

# Print the dataset
# print(dataset)

# Assign a new column and set the value to the sum of Losses column and 5.
dataset["Net"] = dataset["Losses"] + 5

# Print the new dataset
# print(dataset)

# Print the first n rows
# print(dataset.head(3))

# Print a specific row
# print(dataset.iloc[1])

# Print specified rows
# print(dataset[1 : len(dataset)])

# Print a specified column
print(dataset["Losses"])
