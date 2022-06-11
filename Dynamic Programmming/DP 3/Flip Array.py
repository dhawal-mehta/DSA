"""
Flip Array

Problem Description

Given an array A of positive elements, you have to flip the sign of some of its elements such that the resultant sum of the elements of array should be minimum non-negative(as close to zero as possible).

Return the minimum number of elements whose sign needs to be flipped such that the resultant sum is minimum non-negative.



Problem Constraints

1 <= length of(A) <= 100

Sum of all the elements will not exceed 10,000.



Input Format

First and only argument is an integer array A.


Output Format

Return an integer denoting the minimum number of elements whose sign needs to be flipped.


Example Input

Input 1:

 A = [15, 10, 6]

Input 2:

 A = [14, 10, 4]



Example Output

Output 1:

 1

Output 2:

 1



Example Explanation

Explanation 1:

 Here, we will flip the sign of 15 and the resultant sum will be 1.

Explanation 2:

 Here, we will flip the sign of 14 and the resultant sum will be 0.
 Note that flipping the sign of 10 and 4 also gives the resultant sum 0 but flippings there sign are not minimum.
"""
"""
Hint 1

Given that we have to negate some of the elements such that total resultant sum should be minimum non-negative, can this problem be reduced to a knapsack problem? Here, the elements of the knapsack would correspond to the elements negated. Come on, think dynamic!
"""
"""
Solution Approach

Let the sum of all the given elements be S. This problem can be reduced to a Knapsack problem where we have to fill a Knapsack of capacity (S/2) as fully as possible and using the minimum no. of elements. We will fill the Knapsack with the given elements. Sign of all the elements which come into the knapsack will be flipped. As sum of all the elements in the Knapsack will be as close to S/2 as possible, we are indirectly calculating minimum non-negative sum of all the elements after flipping the sign. Give it a thought and code your way out!

"""