li = []

# Original code
def processdata (li):
    for i in range(len(li)):
        if li[i] > 5:   # if current element i > 5
            for j in range(len(li)):
                li[i] *= 2  # multiply current element in the list by 2 for each element in list

# Modified code
'''
1.  best case: none of elements are greater than 5, inner loop never runs; O(n)
    average case: any of elements are greater than 5; O(n^2) (nxn, loop for each loop)
    worst case: all of elements are greater than 5, inner loop runs for every element; O(n^2)  
2.  The average, best, and worst case complexity are not the same...
'''

#Modified

def processdata_mod(li):
    for i in range(len(li)):
        for j in range(len(li)):
            li[i] *= 2          # runs for every element with no condition

# best, average, and worst case: O(n^2)