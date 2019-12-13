#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) o(n^3)
  since we multiply n * n * n for each iteration, which is n^3, each time the input increases we perform n^3 operations. There's also another operation taking place, but n^3 is the dominant answer.


b)O(n*j)
  we go through n number of ops for the first loop and j number of ops for the nested loops - nested loops are multiplied. If we knew if n or j was clearly dominant, we could get rid of the other variable in favor of just the worst case answer.

c)linear - O(n)
  we are going through "bunnies" amount of times - as n increases the number of ops we perform increases at the same rate

## Exercise II

Since the building floors are already sorted I would split the list of floors in half and check if the halfway floor breaks the egg (binary search). If yes, I would split the LHS in half and check again, if not, I would check the RHS, etc. 

runtime complexity of binary search is log(n)

