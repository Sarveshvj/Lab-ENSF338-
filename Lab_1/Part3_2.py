import json
import timeit
from matplotlib import pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = [10, 5]


with open("large-file.json", "r", encoding="utf-8") as f:
    data = json.load(f)


avgtimes = []
sizes = [1000, 2000, 5000, 10000]

for size in sizes:
    subset = data[:size]
    rez = []

    def change_size():
        for record in subset:
            record["size"] = 42

    for i in range(100):
        tm = timeit.timeit(change_size, number=1)
        rez.append(tm)

    avg = sum(rez) / len(rez)
    avgtimes.append(avg)

    print("Average time for %d records: %f" % (size, avg))


# ----- Linear Regression -----
slope, intercept = np.polyfit(sizes, avgtimes, 1)

plt.scatter(sizes, avgtimes)
linevalues = [slope * x + intercept for x in sizes]
plt.plot(sizes, linevalues)

plt.xlabel("Number of Records")
plt.ylabel("Average Processing Time (seconds)")
plt.title("Processing Time vs Number of Records")

plt.savefig("output.3.2.png")
plt.close()


print("The linear model is: t = %.2e * n + %.2e" % (slope, intercept))
print("Plot saved as output.3.2.png")
