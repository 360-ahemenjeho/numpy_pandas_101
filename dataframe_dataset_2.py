from numpy import random
from pandas import DataFrame

rows = random.randint(low=0, high=101, size=(3, 4))
features = ["Eleanor", "Chidi", "Tahani", "Jason"]

dataset = DataFrame(data=rows, columns=features)

# Print the data set
print(dataset)

# Print value at cell #1[Eleanor]
print(dataset.iloc[0]["Eleanor"])

# Create 5th column "Janet" and populate based on columns "Tahani" and "Jason",
dataset["Janet"] = dataset["Tahani"] + dataset["Jason"]
# Print expanded dataset
print(dataset)
