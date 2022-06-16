"""Smallest Multiple With 0 and 1


Problem Description

You are given an integer A. You have to find smallest multiple of A which consists of digits 0 and 1 only.

Since this multiple could be large, return it in form of a string.

NOTE: Returned string should not contain leading zeroes.



Problem Constraints

1 <= A <= 105


Input Format

First and only argument is an integer A.


Output Format

Return a string denoting the above answer.


Example Input

Input 1:

 A = 55 

Input 2:

 A = 2



Example Output

Output 1:

 110

Output 2:

 10



Example Explanation

Explanation 1:

 110 is the smallest multiple of 55 which consist of only 0 and 1.

Explanation 2:

 10 is the smallest multiple of 2 which consist of only 0 and 1."""

"""
Hint 1

Naive approach: We multiply N with positive numbers and then check it consists of only ones and zeros.

What could be a faster approach? A recursive solution where we build all possible numbers consists of digits ones and zeroes only.
For example, something like:

        1
       / \
      /   \ 
     /     \ 
    /       \ 
   10       11   
  /  \     /  \
 /    \   /    \  
100  101  110  111

and so on.

How can we merge nodes in this based on values with modulo N in such a way that we don’t visit all possible states.

"""
"""
Solution Approach

Let’s represent our numbers as strings here. Now, consider there are N states, where i’th state stores the smallest string which when take modulo with N gives i. Our aim is to reach state 0. Now, we start from state “1” and at each step we have two options, either to append “0” or “1” to current state. We try to explore both the options, but note that if I have already visited a state, why would I visit it again? It already stores the smallest string which achieves that state and if I visit it again with a new string it will surely have more characters than already stored string.

So, this is basically a BFS on the states. We’ll visit a state atmost once, hence overall complexity is O(N). Interesting thing is that I need not store the whole string for each state, I can just store the value modulo N and I can easily see which two new states I am going to.

But, how do we build the solution?
If I reach a state x, I store two values

    From which node I arrived at node x from. Say this is node y.
    What(0 or 1) did I append at string at node y to reach node x

Using this information, I can build my solution by repeatedly going to parents starting from node 0.

"""

class Solution:
    # @param A : integer
    # @return a strings
    def multiple(self, A):
        # from collections import deque
        
        # def mod(s, a):
        #     r = 0
        #     for i in range(len(s)):
        #         r = r*10 + int(s[i])
        #         r %= a
        #     return r
        
        # def util(A):
        #     de = deque()
        #     de.append('1')
            
        #     while de:
        #         t = de.popleft()
                
        #         if mod(t, A) == 0:
        #             return t
                
        #         else:
        #             de.append(t+'0')
        #             de.append(t+'1')

        # return util(A)
        
        # ------------- gave TLE -----------------------
        from collections import deque 
        if A == 1:
            return 1
            
        parent = [-1]*A
        val = [0]*A
        
        de = deque()

        
        # temp  = 1%A
        val[1] = '1'
        parent[1] = 0
        de.append(1)
        
        ret = ""
        
        while 1:
            p  = de.popleft()
            
            if p == 0:
                ret += val[p]
                p = parent[p]
                
                while p!=0:
                    ret += val[p]
                    p = parent[p]
                
                return ret[::-1]
                
            
            q = (10*p)%A 
            
            # if q > A:
                # q %= A
            
            # print(parent,val,q)
            if parent[q] == -1:
                val[q] = '0'
                parent[q] = p5
                de.append(q)
            
            q += 1
            if q >= A:
                q = q%A
                
            # print(parent,val,q)    
            if parent[q] == -1:
                val[q] = '1'
                parent[q] = p
                de.append(q)
        