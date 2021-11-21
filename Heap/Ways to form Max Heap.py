"""
Ways to form Max Heap


Problem Description

Max Heap is a special kind of complete binary tree in which for every node the value present in that node is greater than the value present in it’s children nodes.

Find the number of distinct Max Heap can be made from A distinct integers.

In short, you have to ensure the following properties for the max heap :

    Heap has to be a complete binary tree ( A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.)
    Every node is greater than all its children.

NOTE: If you want to know more about Heaps, please visit this link. Return your answer modulo 109 + 7.



Problem Constraints

1 <= A <= 100


Input Format

First and only argument is an inetegr A.


Output Format

Return an integer denoting the number of distinct Max Heap.


Example Input

Input 1:

 A = 4

Input 2:

 A = 10



Example Output

Output 1:

 3

Output 2:

 3360



Example Explanation

Explanation 1:

 Let us take 1, 2, 3, 4 as our 4 distinct integers
 Following are the 3 possible max heaps from these 4 numbers :
      4           4                     4
    /  \         / \                   / \ 
   3    2   ,   2   3      and        3   1
  /            /                     /    
 1            1                     2

Explanation 2:

 Number of distinct heaps possible with 10 distinct integers = 3360.
"""
"""
Hint 1

Verify if the following is true :

    The structure of the heap tree will be fixed.
    Given the numbers in a subtree, the root value is going to be fixed.

Are the numbers in left and right subtree independent of each other?
"""
"""
Solution Approach

    Suppose there are n distinct elements to be used in Max heap. Now it is for sure that the maximum element among this n distinct element will surely be placed on the root of the heap.

    Now there will be remaining (n-1) elements to be arranged.

    Now point to be remembered here is that the structure of the heap will remain the same. That is only the values within the node will change however the overall structure remaining the same.

    As structure of the heap remains the same, the number of elements that are present in the left sub-tree of the root (L) will be fixed. And similarly the number of the elements on the right sub-tree (R) of the root. And also following equality holds .

    L + R = (n-1)

    Now as all the remaining (n-1) elements are less than the element present at the root(The Max Element), whichever L elements among ‘n-1` elements we put in the left sub-tree, it doesn’t matter because it will satisfy the Max Heap property.

    So now there are (n-1)CL ways to pickup L elements from (n-1) elements. And then recurse the solution.

    So final equation will be as follows :

    (n-1)CL * getNumberOfMaxHeaps(L) * getNumberOfMaxHeaps(R)

    So now the question remains only of finding L for given n. It can be found as follows:

    Find the height of the heap h = log2(n)

    Find the max number of elements that can be present in the hth level of any heap . Lets call it m. m = 2h

    Find the number of elements that are actually present in last level(hth level) in heap of size n. Lets call it p. p = n - (2h - 1)

    Now if the last level of the heap is more than or equal to exactly half filled, then L would be 2h - 1

    However if it is half filled then it will reduced by the number of elements in last level left to fill exactly half of the last level.

    So final equation for L will be as follows :

    L = 2h - 1 if p >= m/2
    = 2h - 1 - (m/2 - p) if p<(m/2)

"""
class Solution:
	# @param A : integer
	# @return an integer
	def solve(self, A):
        maxN = 102
        
        getAnsArr = [-1]*maxN
        nclArr = [ [ -1 for i in range(maxN) ]  for j in range(maxN)]
        
        log2 = [0]*maxN
        
        curr = -1
        next = 1
        for i in range(1, maxN):
            if next == i:
                curr += 1
                next *= 2
            log2[i] = curr
        
        # print(log2)
        
        def getL(n):
            if n == 1:
                return 0
                
            h = log2[n]
            numh = (1<<h)
            last = n - (2**h -1)
            
            if last >= (numh)//2:
                return 2**h - 1
            else:
                return 2**h -1 - (numh//2 - last)
        
        def ncl(n,l):
            if l > n:
                return 0
            if l == 0:
                return 1
            if n<=1:
                return 1
            
            if nclArr[n][l] != -1:
                return nclArr[n][l]
            
            ans = ncl(n-1, l-1)+ncl(n-1, l)
            nclArr[n][l] = ans 
            return ans
            
        def getAns(n):
            if n <= 1:
                return 1
            if getAnsArr[n] != -1:
                return getAnsArr[n]
            
                
                
            l = getL(n)
            
            
            answer = ncl(n-1, l)*getAns(l)*getAns(n-l-1)
            getAnsArr[n] = (answer)%1000000007
            return getAnsArr[n]
        
        return getAns(A)