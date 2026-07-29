Explanation for my solution:

# Brute force approach

Pick one element in the array from index 0 and the add, check with other elements.
Similarly then take next element ie index 1 and compare it with its succeeding elements. 

> **Note:** We donot need to compare with previous element cause we already checked in previous step
             eg-> arr = 2,4,1,5 ,target = 5, then 2,4 is not possible also 4,2 is not possible.
     
Thus we use nested for loop, making time complexity Big O of n^2.
