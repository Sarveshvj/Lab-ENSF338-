import json
import timeit
from matplotlib import pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = [10, 5]


with open("large-file.json", "r", encoding="utf-8") as f:
    data = json.load(f)


subset = data[:1000]


def change_size():
    for record in subset:
        record["size"] = 42


timer = timeit.Timer(change_size)
results = timer.repeat(repeat=1000, number=1)

average = sum(results) / len(results)
print("Average time for 1000 records:", average)


plt.figure()
plt.hist(results, bins=30)

plt.xlabel("Processing Time (seconds)")
plt.ylabel("Frequency")
plt.title("Distribution of Processing Time for 1000 Records")

plt.savefig("output.3.3.png")
plt.close()

print("Histogram saved as output.3.3.png")
