def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)
    
'''
1. when func(n) is called, if int n equals 0 or 1, function will return value n
   otherwise, function will return the sum of the call results 
   from func(n-1) and func(n-1).
   Essentially, this code returns the value of the fibonacci sequence at the
   (n)th element.

2. This is an example of a divide-and-conquer algorithm. We want to display the
   fibonacci sequence value at a specific index, so we do so by dividing the function
   into function calls of smaller arguments and solving those subcalls to determine
   the result of the larger original call.

3. Formula:
   func(n) = func(n-1) + func(n-2)


'''

print(func(3))