"""
First Missing Integer

Problem Description

Given an unsorted integer array A of size N. Find the first missing positive integer.

Note: Your algorithm should run in O(n) time and use constant space.



Problem Constraints

    1 <= N <= 1000000

    -109 <= A[i] <= 109



Input Format

First argument is an integer array A.


Output Format

Return an integer denoting the first missing positive integer.


Example Input

    Input 1:

    [1, 2, 0]

    Input 2:

    [3, 4, -1, 1]

    Input 3:

    [-8, -7, -6]



Example Output

    Output 1:

    3

    Output 2:

    2

    Output 3:

    1



Example Explanation

Explanation 1:

    A = [1, 2, 0]
    First positive integer missing from the array is 3.

"""

""" Hint1
To simply solve this problem, search all positive integers, starting from 1 in the given array. We may have to search at most n+1 numbers in the given array. So this solution takes O(n^2) in worst case.

We can use sorting to solve it in lesser time complexity. We can sort the array in O(nLogn) time.

Once the array is sorted, then a linear scan of the array is all that remains to be done.

So this approach takes O(nLogn + n) time which is O(nLogn).

We can also use hashing. We can build a hash table of all positive elements in the given array.

Once the hash table is built, all positive integers, starting from 1 can be searched here. As soon as we find a number which is not there in the hash table, we return it.

Approximately, this approach may take O(n) time, but it requires O(n) extra space.

But what we are really looking for is a O(n) time, O(1) space solution.

Note that ( N being the size of the array ), A[i]<=0 and A[i]>N are not the numbers you are looking for because the missing positive integer will be in the range [1, N+1].

The answer will be N+1 only if all of the elements of the array are exact one occurrence of [1, N].

If using extra space was an option, creating buckets would have been an easy solution.

Creating an array of size N initialized to 0, for every value A[i] which lies in the range [1, N], we would have incremented its count in the array. Consequently, we would traverse the array to find the first array position with value 0, hence finding our answer.

However, since we are not allowed buckets, can we use the existing array as bucket somehow?

"""


""" solution Approach

Note: numbers A[i]<=0 and A[i]>N ( N being the size of the array ) is not important to us since the missing positive integer will be in the range [1, N+1].

The answer will be N+1 only if all of the elements of the array are exact one occurrence of [1, N].

Creating buckets would have been an easy solution if using extra space was allowed.

An array of size N initialized to 0 would have been created.

For every value A[i] which lies in the range [1, N], its count in the array would have been incremented.

Finally, traversing the array would help to find the first array position with value 0 and that will be our answer.
However, usage of buckets is not allowed, can we use the existing array as bucket somehow?

Now, since additional space is not allowed either, the given array itself needs to be used to track it.

It may be helpful to use the fact that the size of the set we are looking to track is [1, N]

which happens to be the same size as the size of the array.

This means we can use the array to track these elements.

We traverse the array and if A[i] is in [1,N] range, we try to put in the index of same value in the array.


"""

""" Accepted solution """
# @param A : list of integers
# @return an integer

def firstMissingPositive( A):
    # partition
    n=len(A)
    end=0
    for i in range(n):
        if A[i] > 0:
            A[i],A[end] = A[end],A[i]
            end+=1
    
    # negative for visit
    for i in range(end):
        if abs(A[i]) <= end:
            A[abs(A[i])-1]*=-1

    for i in range(end):
        if A[i] > 0:
            return i+1
    return end+1

