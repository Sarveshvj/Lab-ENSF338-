import timeit
import profile

def sub_function(n):
#sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)
    
def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
# third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]


# Q1: What is a profiler, and what does it do?
# A profile is a set of statistics that describes how often and 
# for how long various parts of the program executed.
# It shows you exactly where the time goes in the program.

# Q2: How does profiling differs from benchmarking?
# Benchmarking just tells you how a piece of code is excuted under specific condition.
# Whereas, Profiling shows exactly where and why it is slow.

# Q3: Use a profiler to measure execution time of the program (skip function definitions)
def main():    
    test_function()
    third_function()

profile.run("main()")

# Q4: Discuss a sample output. Where does execution time go?
# The profiler reports that the program executes in 8.109 seconds with 72 function calls.
# The output shows that most of the execution time spent in third_function().It consumes about
# 7.203 seconds of total runtime.
