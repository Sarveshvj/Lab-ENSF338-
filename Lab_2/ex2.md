Exercise 2 /1

1. Mention at least two aspects that make interpolation search better than binary search 

	    •	Interpolation search can be faster than binary search when the data is evenly distributed, because it tries to guess where the value might be.
	    •	It may need fewer comparisons than binary search in some cases.

2. Interpolation search assumes that data is uniformly distributed. What happens this data follows a different distribution? Will the performance be affected? Why?

        • If the data distribution is uneven, the interpolation search may guess the wrong location.
        • This will slow down the search and require more steps.
        • Therefore, performance will indeed be affected because the algorithm relies on a uniform distribution of data.

3. If we wanted to modify interpolation search to follow a different distribution,
which part of the code would be affected?

        • The part that changes is thiolation calculation 
        • This line of code estimates the location of the target value, based on the uniform distribution.

Exercise 2 /2

4. When is linear search your only option for searching data as binary and interpolation search may fail.

        • Linear search is the only why when the data is not sorted.
        • Binary search and interpolation search both need sorted data to work correctly.

5. In which case will linear search outperform both binary and interpolation search, and why?

        • Linear search can be faster when the list is very small or when the value is close to the beginning of the list.
        • In these cases, linear search finds the value quickly without extra calculations.

6. Is there a way to improve binary and interpolation search to solve this issue?

        • Yes, one way is to sort the data first so binary and interpolation search can be used.
        • Another what is to choose a different search method depending on the data size and situation.