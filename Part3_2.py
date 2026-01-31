import time
import random
import numpy as np
import matplotlib.pyplot as plt

# Linear search function
def linear_search(arr, target):
    for x in arr:
        if x == target:
            return True
    return False

sizes = [1000, 2000, 5000, 10000]
averages = []

# Benchmarking
for n in sizes:
    times = []
    data = list(range(n))

    for _ in range(100):
        target = random.choice(data)
        start = time.perf_counter()
        linear_search(data, target)
        end = time.perf_counter()
        times.append(end - start)

    avg_time = sum(times) / len(times)
    averages.append(avg_time)

# Linear regression
coeffs = np.polyfit(sizes, averages, 1)
poly = np.poly1d(coeffs)

x_line = np.linspace(min(sizes), max(sizes), 100)
y_line = poly(x_line)

# Plot
plt.figure()
plt.plot(sizes, averages, marker='o', label="Average Time")
plt.plot(x_line, y_line, label="Regression Line")
plt.xlabel("Number of Records")
plt.ylabel("Average Processing Time (seconds)")
plt.title("Linear Search Performance")
plt.legend()
plt.savefig("output.3.2.png")
plt.show()
