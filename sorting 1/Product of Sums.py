"""
Product of Sums


Consider a 3-tuple of integers (A,B,C) under the constraints that A<=B and C<=B.

A function on the tuple is defined as:

F(A,B,C)=0 if A>B or C>B (or both).
F(A,B,C)=(A+B)*(B+C) if A<=B and C<=B.

Given 3 arrays of size P,Q,R respectively.

Find the sum of all F(A,B,C) over all the 3-tuples (A,B,C) where A,B,C belong to the arrays P,Q,R respectively.

Since the sum can be very large, find the sum modulo 10^9+7.

Constraints:

1.   1<=P,Q,R<=100000
2.   1<= every array element <=10^9

Input:

3 integers denoting the size of the 3 arrays and 3 arrays.

Output:
Sum of all F(A,B,C) over all the 3-tuples (A,B,C) where A,B,C belong to the arrays P,Q,R respectively modlulo 10^9+7

Example:

Input:

size of array1: 2
size of array2: 2
size of array3: 4
array1:[1 2]
array2:[4 4]
array3:[2 3 4 5]

Output:

462

"""
"""
Hint 1
For any 3 tuple (A,B,C) , since we need A and C to be less than or equal to B and since we need to consider
all the 3 tuples, we sort all the 3 arrays.
Now try to think how binary search would fit in this problem.
"""
"""
Hint 2
For every value of B, we binary search in array A and C the just greater value of B and use prefix sums to find the intended sum.
"""
"""
Solution Approach

For a particular B, we need to find the sum of all A’s and C’s less than B.
That can be done efficiently using prefix sum arrays over first and third array.
Now that value of B will be added as many times as the number of A’s and C’s less than B
"""
# @param A : integer
# @param B : integer
# @param C : integer
# @param D : list of integers
# @param E : list of integers
# @param F : list of integers

# @return an integer

def getNext(self, arr, curr, B):
    # print(arr, curr, B)
    if curr>= len(arr):
        return 0, 0, False
    
    tempSum = 0
    tempCurr = curr
    flag =False

    
    while tempCurr < len(arr):
        if arr[tempCurr] <= B:
            flag = True
            tempSum += arr[tempCurr]
            tempCurr+=1
        else:
            return tempCurr, tempSum, flag
    return tempCurr, tempSum, flag
    
    
def getSum(self, a, b, c, A, B, C):
    
    sumA = 0
    currA = 0
    
    sumC = 0
    currC = 0
    
    A = sorted(A)
    B = sorted(B)
    C = sorted(C)
    
    ans = 0

    flagA = False
    flagC = False

    for i in B:
        (tempCurrA,tempSumA,flagA) = self.getNext(A, currA, i)
        (tempCurrC,tempSumC,flagC) = self.getNext(C, currC, i)   
        
        if flagA:
            currA = tempCurrA
            sumA += tempSumA
        
        if flagC:
            currC = tempCurrC
            sumC += tempSumC
        
        ans  = (ans + (currA*i + sumA)*(currC*i + sumC) )%(10**9 + 7)
    
    return ans
