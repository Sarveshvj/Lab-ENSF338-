import timeit
import matplotlib.pyplot as plt

def func(n):
   if n == 0 or n == 1:
      return n
   else:
      return func(n-1) + func(n-2)
    
'''
1. Essentially, this code returns the value of the fibonacci sequence at the
   (n)th element using recursion.

2. This is NOT an example of a divide-and-conquer algorithm. While divide-and-conquer algorithms
   split larger problems into smaller independent subproblems, this program breaks the problem
   into subproblems whose results overlap and are computed multiple times, making it
   very inefficient.

3. Expression:
   t(n) = t(n-1) + t(n-2) + O(1) = O(2^n)
'''
# 4. Optimized code implementation using array memoization
memo = {}      # <---- already computed results stored here

def func2(n, memo):
   if n in memo:
      return memo[n]
   if n <= 1:
      memo[n] = n
   else:
      memo[n] = func2(n-1, memo) + func2(n-2, memo)
   return memo[n]

'''
5. Expression:
   t(n) = (n+1) * O(1) = O(n)
'''

# 6
origin = []
optim = []

for n in range(0, 36):
   t1 = timeit.timeit(stmt=lambda: func(n), number=1)
   origin.append(t1)
   t2 = timeit.timeit(stmt=lambda: func2(n, {}), number=1)
   optim.append(t2)


# PLOTTING:
n_values = list(range(36))

# PLOT FUNC

plt.figure()
plt.plot(n_values, origin)
plt.xlabel("n")
plt.ylabel("Time(seconds)")
plt.title("Original Recursive Fibonacci Runtime")
plt.grid(True)
plt.show()

# PLOT FUNC2
plt.figure()
plt.plot(n_values, optim)
plt.xlabel("n")
plt.ylabel("Time(seconds)")
plt.title("Memoized Fibonacci Runtime")
plt.grid(True)
plt.show()
