"""Rotated Sorted Array Search

Problem Description

Given a sorted array of integers A of size N and an integer B.

array A is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).

You are given a target value B to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

NOTE: Users are expected to solve this in O(log(N)) time.



Problem Constraints

1 <= N <= 1000000

1 <= A[i] <= 10^9

all elements in A are disitinct.



Input Format

The first argument given is the integer array A.

The second argument given is the integer B.


Output Format

Return index of B in array A, otherwise return -1


Example Input

Input 1:

A = [4, 5, 6, 7, 0, 1, 2, 3]
B = 4

Input 2:

A = [1]
B = 1



Example Output

Output 1:

 0

Output 2:

 0



Example Explanation

Explanation 1:

 
Target 4 is found at index 0 in A.

Explanation 2:

 
Target 1 is found at index 0 in A.
"""
"""
Hint 1

Think a modified version of the binary search.
If the pivot is known, the binary search becomes trivial as the array to the either side of the pivot is sorted.
Can you somehow search for the pivot in your binary search?
"""
"""
Solution Approach

A naive solution is the linear search.

To improve, let us break our approach into 2 steps. First, we find the pivot (the index of minimum in the array).

Once we know the pivot, to search for x, we can do a conventional binary search in the left and right part of the pivot in the array.

Now, let us look at how binary search can be applied in this scenario to find the minimum.

There are 2 cases:

1)


          mid
   
           |
    
   6 7 8 9 1 2 3 4 5  

arr[mid] > arr[end]

The min lies in (mid, end]

Mid is excluded from the range because arr[mid] > arr[end]

2)

        
         mid
         
          | 
          
  6 7 8 9 1 2 3 4 5

arr[mid] < arr[end]

The min lies in [start, mid]

3) Note: If there are duplicates, making either decision might be difficult and hence linear search might be required.

               mid
               
                |
                
1 1 1 1 2 0 1 1 1 1 1 1 1 1 1 1 1 

arr[mid] = arr[end]

Indecisive. We would need to explore the whole array.

"""
# @param A : tuple of integers
# @param B : integer
# @return an integer
def search( A, B):
    N = -1
    
    l = 0
    r = len(A)-1

    if B == A[0]:
        return 0
    elif B == A[-1]:
        return len(A)-1

    while l<=r:
        mid = l + (r-l)//2
        
        if A[mid] == B:
            return mid

        if A[mid] > A[N]:
            if A[mid] > B and B>A[N]:
                r = mid - 1
            else:
                l = mid + 1            
        else:
            if A[mid] < B and B<=A[-1]:
                l = mid + 1
            else:
                r = mid - 1
    
    return -1
