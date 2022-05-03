"""Mask Updates

Bitmasks are cool. A bitmask is a string of binary bits (0s and 1s). For example: "01010" is a bitmask.

Kuldeep is a naughty but brilliant computer scientist. In his free time, he writes some random programs to play with bitmasks. He has a PhD student under him and to test him (and entertain himself), he has given him the following task:

Given a number N, write a bitmask of length N containing all 0s. Now, you are given Q operations. Each operation contains two numbers (l, r) as input. An operation can be one of the following:

    Update operation: Take the XOR of all the bits in the bitmask from index l to r (both inclusive) with 1.
    Query operation: Count the number of set bits in the bitmask between index l to r (both inclusive).

You need to find the sum of all the queries.

Note:

1. In case there are no queries, return 0.
2. As the answer can be large, output the answer mod 1000000007
3. Consider 0 based indexing

Constraints:

1 <= N <= 100000
1 <= Q <= 100000
0 <= l, r < N

Input format:

int A: Number N as described above
vector<vector<int> > B: Q operations as described above. 
Each row contains three numbers (type, l, r). If type is 0, its an update operation else a query operation.

Example:

Input:
N = 5
Operations: [[0, 1, 3], [1, 1, 2], [0, 0, 4], [1, 3, 4]]

Output:
3

Explanation:
Initial mask: 00000
Operation 1: Update (1,3) , Resulting mask = 01110
Operation 2: Query (1,2), Answer to query = 2
Operation 3: Update (0, 4), Resulting mask = 00001
Operation 4: Query (3,4), Answer to query = 1

Sum of all the queries = 2+1 = 3
Answer = 3%1000000007 = 3
"""
"""
Hint 1

A naive algorithm will be one where both update and query are O(N). Using a naive algorithm, complexity of the solution would be O(N*Q).

Can you think of the algorithm where:
1. Updates are O(N) and Queries are O(1)
2. Updates are O(1) and Queries are O(N)
3. Both updates and queries are O(logN)

"""
"""
Solution Approach

If you were to use the Naive approach, complexity of the algorithm would be O(N*Q). However, it can be improved.

Improvement:
In case there are large no. of updates and lesser queries, you can store how many times each of the index has been updated. Now, if the bit at an index i has been updated odd number of times, it would be 1 else 0.

We can store the updates in O(1) time by maintaining an array UPD[N] where UPD[i] = No. of times the bit i has been updated.
Now, for an update (l, r), add 1 to UPD[l] and -1 to UPD[r+1]. This ways updates are O(1)

For query, first calculate a new array CUMUPD[N] where CUMUPD[i] = UPD[0] + … + UPD[i] (Cumulative Sum). Now, CUMUPD[i] will tell you the number of times an index has been updated. Queries are thus O(N).

Similarly, we can make update O(N) and queries O(1) in case there are more queries.

Algorithm for our need:
The improvement above is better than Naive algorithm but is not enough for our problem (which is obvious through constraints).
The problem above is that of range-update and range-query. We can use a special data structure named Segment Tree to solve this problem. Just make sure that we have both update and query working in O(logN) time.

Come on, this is an important data structure. Read about it on the web and code it out.

"""
class SegmentTree:
    def __init__(self, A):
        self.st =  [0]*(A*4)
        self.lazy = [0]*(4*A)
        
    def update(self, l, r, currL, currR, indx):
        if indx > len(self.st):
            return 0
            
        if self.lazy[indx] == 1:
            self.st[indx] = (currR - currL + 1) - self.st[indx]
            
            if 2*indx + 1 < len(self.st) and 2*indx+2 < len(self.st):
                self.lazy[2*indx + 1] = 1 - self.lazy[2*indx + 1]
                # print(indx, 2*indx+2)
                self.lazy[2*indx + 2] = 1 - self.lazy[2*indx + 2]
        
            self.lazy[indx] = 0
        
        # no overlap 
        if currL > r or currR < l:
            return  self.st[indx]     
            
        # total overlap
        if currL >= l and currR <= r:
            self.st[indx] = (currR - currL + 1) - self.st[indx]
            
            if 2*indx + 1 < len(self.st) and 2*indx+2 < len(self.st):
                self.lazy[2*indx + 1] = 1 - self.lazy[2*indx + 1]
                self.lazy[2*indx + 2] = 1 - self.lazy[2*indx + 2]
   
            return self.st[indx]
        
        mid= (currL + currR)//2
        
        self.st[indx] =   self.update(l,r, currL, mid, 2*indx +1) + self.update(l, r, mid+1, currR, 2*indx + 2) 
        
        return self.st[indx]


    
    def query(self, l, r, currL, currR, indx):
        
        if currL > r or currR < l:
            return 0        
        
        if self.lazy[indx] == 1:
            self.st[indx] =  (currR - currL + 1) - self.st[indx] 
            
            if 2*indx + 1 < len(self.lazy) and 2*indx+2 < len(self.st):
                self.lazy[2*indx +1] = 1 - self.lazy[2*indx + 1]
                # print(indx, 2*indx+2)
                
                self.lazy[2*indx +2] = 1 - self.lazy[2*indx + 2]
            
            self.lazy[indx] = 0

        if currL >= l and currR <= r:
            return self.st[indx]
        
        mid = (currL + currR )//2
        
        return  self.query(l, r, currL, mid, 2*indx +1) + self.query(l,r, mid+1, currR, 2*indx+2)


class Solution:
    def solve(self, A, B):
        st = SegmentTree(A)
        
        
        ans = 0
        for q, l, r  in B:
            if q == 0:
                st.update(l,r, 0, A-1, 0)
            else:
                ans = (ans +  st.query(l,r, 0, A-1, 0) )%1000000007
            
            # print(st.seg, st.lazy)
        return ans
        