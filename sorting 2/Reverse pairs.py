"""
Reverse pairs


Problem Description
Given an array of integers A, we call (i, j) an important reverse pair if i < j and A[i] > 2A[j].

Return the number of important reverse pairs in the given array A.



Problem Constraints

1 <= length of the array <= 105

-2 * 109 <= A[i] <= 2 * 109



Input Format

The only argument given is the integer array A.


Output Format

Return the number of important reverse pairs in the given array A.


Example Input

Input 1:

 A = [1, 3, 2, 3, 1]

Input 2:

 A = [4, 1, 2]



Example Output

Output 1:

 2

Output 2:

 1



Example Explanation*

Explanation 1:

 There are two pairs which are important reverse i.e (3, 1) and (3, 1).

Explanation 2:

 There is only one pair i.e (4, 1)."""
"""
Hint 1

Can you use Merge Sort to count the number of important reverse pair?
"""
"""
Solution Approach

We can use two loops and calculate the number of pairs that satisfies the condition but the time complexity for this will be O(N^2) and this will not work in worst case.

So we can think of better solution i.e using merge sort.
We will do a usual merge sort but before calling the merge function we will calculate the number of pairs by using two pointers considering that the two array are sorted individually.

Likewise we will do this till the our mergesort ends i.e the array becomes sorted.
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def util(self, A, start, end):
        if start >= end:
            return 0
        
        mid = start + (end -start)//2
        
        left = self.util(A, start, mid)
        right = self.util(A, mid+1, end)
        
        ans = 0
        
        temp = []
        ptr1 = start
        ptr2 = mid + 1
        # print("for", A[start:end+1])
        
        while ptr1<=mid and ptr2 <= end:
            if A[ptr1] <= 2*A[ptr2]:
                ptr1 += 1
            else:
                ans +=  mid+1 - ptr1
                # print(A, A[start:mid+1], A[mid+1:end+1], start, end)
                ptr2+=1

        
        ptr1 = start
        ptr2 = mid + 1
        
        while ptr1<=mid and ptr2 <= end:
            if A[ptr1] <= A[ptr2]:
                temp.append(A[ptr1])
                ptr1 += 1
            
            else:

                temp.append(A[ptr2])
                ptr2+=1
        
        while ptr1<=mid:
            temp.append(A[ptr1])
            ptr1+=1
        
        while ptr2 <= end:
            temp.append(A[ptr2])
            ptr2+=1
        
        A[start:end+1] = temp
        
        return left+right + ans
        
        
    def solve(self, A):
        temp = self.util(A, 0, len(A)-1)
        return temp 
