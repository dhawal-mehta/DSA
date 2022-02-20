"""
Inversion count in an array


Problem Description

Given an array of integers A. If i < j and A[i] > A[j] then the pair (i, j) is called an inversion of A. Find the total number of inversions of A modulo (109 + 7).


Problem Constraints

1 <= length of the array <= 100000

1 <= A[i] <= 10^9



Input Format

The only argument given is the integer array A.


Output Format

Return the number of inversions of A modulo (109 + 7).


Example Input

Input 1:

A = [3, 2, 1]

Input 2:

A = [1, 2, 3]



Example Output

Output 1:

3

Output 2:

0



Example Explanation

Explanation 1:

 All pairs are inversions.

Explanation 2:

 No inversions.
"""
"""
Hint 1

Traverse through the array and for every index find the number of smaller elements on its right side of the array.
This can be done using a nested loop. Sum up the counts for all index in the array and print the sum.
"""
"""
Solution Approach

Algorithm :
Traverse through the array from start to end
For every element find the count of elements smaller than the current number upto that index using another loop.
Sum up the count of inversion for every index.
Print the count of inversions.
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def merge(self, A, start, mid, end):
        temp = []
        ptr1=start
        ptr2 = mid+1
        count = 0
        while ptr1<=mid and ptr2<=end:
            # print(A,temp, ptr1, A[ptr1], ptr2, A[ptr2])
            if A[ptr1] <= A[ptr2]:
                temp.append( A[ptr1] )
                ptr1+=1
            else:    
                # print("here")
                # print(temp, ptr2, A[ptr2])
                temp.append( A[ptr2] )
                count += mid - ptr1 + 1
                ptr2 += 1
        
        # print(temp)        
        while ptr1<mid+1:
            temp.append(A[ptr1])
            ptr1+=1
            
        while ptr2<end+1:
            temp.append(A[ptr2])
            ptr2+=1
        
        # j = 0
        for i in range(len(temp)):
            A[start+i] = temp[i]
        
        # print(start, end, temp, count)
        return count 
    
    def mergeRoutine(self, A, start, end):
        if start>=end:
            return 0
        mid = start + (end - start)//2
        return self.mergeRoutine(A,start,mid) + self.mergeRoutine(A,mid+1,end) + self.merge(A, start, mid, end)
        
    def solve(self, A):
        return self.mergeRoutine(A,0,len(A)-1)