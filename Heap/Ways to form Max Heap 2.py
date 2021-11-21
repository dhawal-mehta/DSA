"""
Ways to form Max Heap 2


Problem Description

Max heap is a special kind of complete binary tree in which for every node the value present in that node is greater than the value present in it’s children nodes.

Given an array A of size N consisting of N - 1 distinct elements. In other words there is exactly one element that is repeated.
It is given that the element that would repeat would be either the maximum element or the minimum element.

Find the number of structurally different Max heaps possible using all the N elements of the array i.e. Max heap of size N.

As final answer can be very large return your answer modulo 109 + 7.



Problem Constraints

1 <= N <= 1000


Input Format

First and only argument is an integer array A.



Output Format

Return an integer denoting the number of structurally different Max heaps possible modulo 109 + 7.


Example Input

Input 1:

 A = [1, 5, 5]

Input 2:

 A = [2, 2, 7]



Example Output

Output 1:

 2

Output 2:

 1



Example Explanation

Explanation 1:

 The possible max heaps using the given elements are:- First: 5 on the root. 1 as the left child of root and 5 as the right child of the root.   
                5
              /   \
            1       5
 Second: 5 on the root. 5 as the left child of root and 1 as the right child of the root.
                5
              /   \
            5       1            

Explanation 2:

 There is only one possible max heaps: 7 on the root. 2 as the left child of root and 2 as the right child of the root.   
                7
              /   \
            2       2
"""
"""
Hint 1

First consider what would be the number of max heaps if all the elements of the array of distinct.

Next consider what would be the case when both repeating elements are maximum and what would be the case when both would be minimum.
"""
"""
Solution Approach

If both repeating elements are maximum than one maximum element has to be fixed at the root and the other maximum element can go either in the left sub tree or the right subtree so the number of max heaps are equal to when there where no repeating elements.

Now if minimum elements are repeating than there would be two cases:-
1) Both repeating elements go in same subtree
2) Both repeating elements go in different subtree.

If both repeating elements go in different subtree than now the problem is back to when there where no repeating elements but with a smaller problem size.
If both repeating elements go in same subtree than for one subtree(left or right) it would be the case with no repeating elements while for the other subtree call the same function recursively.
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        maxFlag = False

        currMax = max(A)
        count = 0
        for i in A:
            # print(i, currMax, count)
            if i == currMax: 
                if count == 1:
                    maxFlag = True
                else:
                    count += 1

        maxN = 1002
        
        nclArr = [ [-1 for i in range(maxN) ] for j in range(maxN) ]
        log2 = [-1]*maxN
        
        curr = -1
        next = 1
        for i in range(1, maxN):
            if i == next:
                curr += 1
                next *= 2
            log2[i] = curr
        
        getAnsArr = [ [-1,-1] for i in range(maxN) ]
        
        
        def ncl(n ,l):
            if l > n :
                return 0
            if l == 0:
                return 1
            if n <= 1:
                return 1
            
            if nclArr[n][l] != -1 or nclArr[n][n-l] != -1:
                return nclArr[n][l]
            
            ans = 1
            for i in range(1, min(l,n-l) +1):
    
                ans = ((n-i+1)*ans)//i
                # print(i, ans)


            # ans = ncl(n-1,l-1) + ncl(n-1,l)
            nclArr[n][l] = ans
            nclArr[n][n-l] = ans
            # print("ans", ans)
            return ans
            

        def getL(n):
            if n <= 1:
                return 0
            
            h = log2[n]
            numh = 1<<h
            last = n - ( 2**h -  1 ) #in last

            
            if last >= numh//2:
                return 2**h - 1
            else:
                return 2**h -1 - (numh//2 - last)
            
        
        def getAns(n, dupFlag):
            
            if n <= 1 and dupFlag == 1:
                return 0
            if n<=1 and dupFlag == 0:
                return 1
            if n == 2 :
                return 1
            
            if getAnsArr[n][dupFlag] != -1:
                return getAnsArr[n][dupFlag]
                
            l = getL(n)
            # print("l", l)
            if dupFlag == 0:
                ans =  ncl(n-1, l)*getAns(l, 0)*getAns(n-l-1, 0)
                
            else:
                one = ncl(n-3, l-2)*getAns(l, 1)*getAns(n-l-1, 0)
                two = ncl(n-3, l-1)*getAns(l, 0)*getAns(n-l-1, 0)
                three = ncl(n-3, l)*getAns(l,0)*getAns(n-l-1, 1)
                ans =  one+two+three
                
                
            
            getAnsArr[n][dupFlag] = ans%1000000007
            return ans%1000000007

        # print(ncl(5,2))
        # return 0  
        if maxFlag == True:
            return getAns(len(A), 0)
        else:
            return getAns(len(A),1)