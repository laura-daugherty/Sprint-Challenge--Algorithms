#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Logarithmic Time - O(log n)
  as n increases, the time it takes to do the operation increases just a bit


b)Constant Time - O(1)
  as n increases, the time it takes to do the operation doesn't increase


c)polynomial - O(n^c)

## Exercise II

Since the building floors are already sorted I would split the list of floors in half and check if the halfway floor breaks the egg (binary search). If yes, I would split the LHS in half and check again, if not, I would check the RHS, etc. 

runtime complexity of binary search is log(n)

