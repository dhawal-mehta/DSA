""" 
N/3 Repeat Number

Problem Description
You're given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.

If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.

Example:

Input: [1 2 3 1 1]
Output: 1 
1 occurs 3 times which is more than 5/3 times.

"""
"""
Hint 1
It works to simply pick all elements one by one. For every picked element, count its occurrences by traversing the array.
If count becomes more than n/3, then print the element. Time Complexity of this method would be O(n^2).

A better solution is to use sorting.

First, sort all elements using a O(nLogn) algorithm. All required elements in a linear scan of array can be found once the array is sorted.

So overall, time complexity of this method is O(nLogn) + O(n) which is O(nLogn).

However, a linear solution is needed here.

Note: if at any instance, you have three distinct elements from the array, if you remove them from the array, your answer does not change.

Try to base your solution idea on the above fact.

Would it help to maintain two elements from array with their count as you traversed the array ?

"""

"""
solution approach

It is important to note that if at a given time, you have 3 distinct element from the array, if you remove them from the array, your answer does not change.

Assume that we maintain 2 elements with their counts as we traverse along the array.

When we encounter a new element, there are 3 cases possible :

    We don’t have 2 elements yet. So add this to the list with count as 1.

    This element is different from the existing 2 elements. As we said before, we have 3 distinct numbers now. Removing them does not change the answer. So decrement 1 from count of 2 existing elements. If their count falls to 0, obviously its not a part of 2 elements anymore.

    The new element is same as one of the 2 elements. Increment the count of that element.

Consequently, the answer will be one of the 2 elements left behind. If they are not the answer, then there is no element with count > N / 3.

"""

""" accepted solution """

# @param A : tuple of integers
# @return an integer
def repeatedNumber( A):
    n=len(A)
    first_major=0
    second_major=0
    first_count=0
    second_count=0
    
    for i in range(n):
        
        if A[first_major] == A[i]:
            first_count+=1
        elif A[second_major] == A[i]:
            second_count+=1
        elif first_count == 0:
            first_major = i
            first_count+=1
        elif second_count == 0:
            second_major = i
            second_count += 1
        else:
            first_count-=1
            second_count-=1
    first_count = 0
    second_count = 0
    for i in range(n):
        if A[i] == A[first_major]:
            first_count+=1
        elif A[i] == A[second_major]:
            second_count+=1
    if first_count > n//3:
        return A[first_major]
    elif second_count > n//3:
        return A[second_major]
    else:
        return -1
            