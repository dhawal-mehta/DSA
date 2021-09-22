"""Alternate positive and negative elements

Problem Description

Given an array of integers A, arrange them in an alternate fashion such that every non-negative number is followed by negative and vice-versa, starting from a negative number, maintaining the order of appearance. The number of non-negative and negative numbers need not be equal.

If there are more non-negative numbers they appear at the end of the array. If there are more negative numbers, they too appear at the end of the array.

Note: Try solving with O(1) extra space.



Problem Constraints

1 <= length of the array <= 7000
-109 <= A[i] <= 109


Input Format

The first argument given is the integer array A.


Output Format

Return the modified array.


Example Input

Input 1:

 A = [-1, -2, -3, 4, 5]

Input 2:

 A = [5, -17, -100, -11]



Example Output

Output 1:

 [-1, 4, -2, 5, -3]

Output 2:

 [-17, 5, -100, -11]



Example Explanation

Explanation 1:

A = [-1, -2, -3, 4, 5]
Move 4 in between -1 and -2, A => [-1, 4, -2, -3, 5]
Move 5 in between -2 and -3, A => [-1, 4, -2, 5, -3]
"""
"""
Hint 
If extra memory is allowed, we simply first seperate all the positive and negative numbers.

After that we can merge them by taking elements from both of them alternatively.
"""
"""
Solution approach
The above problem can be easily solved if O(n) extra space is allowed. It becomes interesting due to the limitations that O(1) extra space and order of appearances.

The idea is to process array from left to right. While processing, find the first out of place element in the remaining unprocessed array. An element is out of place if it is negative and at odd index, or it is positive and at even index. Once we find an out of place element, we find the first element after it with opposite sign. We right rotate the subarray between these two elements (including these two).

// Bonus
The idea is to process the array and shift all negative values to the end in O(n) time.

After all negative values are shifted to the end, we can easily rearrange array in alternating positive & negative items.

We basically swap next positive element at even position from next negative element in this step.

"""
# @param A : list of integers
# @return a list of integers
def rotate(self,A, end ,start):
    temp = A[end]
    for i in range(end,start,-1):
        A[i] = A[i-1]
    A[start] = temp
    
def solve(self, A):
    outOfPlace = -1
    for i in range(len(A)):
        
        if outOfPlace >= 0:
                if  (A[i]<0  and A[outOfPlace]>=0) or (A[i]>=0 and A[outOfPlace]<0):
                    # print("test")
                    self.rotate(A,i,outOfPlace)
                    if i - outOfPlace > 1:
                        outOfPlace +=2
                    else:
                        outOfPlace = -1
                        
        else:
            if (A[i] < 0 and i%2 ==1) or (A[i]>=0 and i%2==0):
                outOfPlace = i
        # print(A, outOfPlace)


    return A       