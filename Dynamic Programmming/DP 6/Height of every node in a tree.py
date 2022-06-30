"""Height of every node in a tree


Given a tree of A nodes. Find the height of tree for each node taken as a root.

Input Format:

First argument of input contains an integer A denoting number of Nodes
Second argument of input contains a (A-1) x 2 matrix denoting edges of tree.

Output Format:

Return an integer array of size A denoting height of each node as a root.

Constraints:

1 ≤ N ≤ 100000

Example Input:

Input 1:
    A = 4 , B = [[1,2],[2,3],[2,4]]
Output 1:
    [2,1,2,2]
Explanation 1:
    For node 1 deepest node is 3(or 4) at height 2, for node 3,4 node 1 is deepest node at height 2 and for node 2 all node are at height 1.
"""
"""
Solution Approach

Precalculate two things for each node in 1 dfs using tree dp.

    Maximum depth below this node
    Maximum height above this node
    answer is max of both.

"""
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        
        graph = [ [] for i in range(A)]
        
        for m,n in B:
            graph[m-1].append(n-1)
            graph[n-1].append(m-1)
        
        
        def getIn(currNode, prevNode):
            global inArr
            
            res = 0
            for i in graph[currNode]:
                if i != prevNode:
                   res = max(res, getIn(i, currNode) + 1) 
            
            inArr[currNode] = res
            return res
        
            
        global inArr 
        inArr = [0 for i in range(A) ]
        getIn(0, -1)
        
        
        def getOut(currNode, prevNode, prevPrevNode):
            # print(currNode, prevNode)
            global inArr
            global outArr
            global dp
            
            if dp[prevNode][0] == -1:
                firstMax = -1
                firstMaxNode = -1
                secMax = -1
                
                for i in graph[prevNode]:
                    if i != prevPrevNode:
                        if inArr[i] > firstMax:
                            temp = firstMax
                            firstMax = inArr[i]
                            firstMaxNode = i
                            secMax = temp
                        
                        elif inArr[i] == firstMax or inArr[i] > secMax:
                            secMax = inArr[i]
                    
                dp[prevNode][0] = firstMax
                dp[prevNode][1] = firstMaxNode
                dp[prevNode][2] = secMax
                
            if dp[prevNode][1] == currNode:
                inFromPrev = dp[prevNode][2]
            else:
                inFromPrev = dp[prevNode][0]
                
            outArr[currNode] = max(outArr[prevNode] , 1+inFromPrev) + 1
            
            for i in graph[currNode]:
                if i != prevNode:
                    getOut( i, currNode, prevNode)
        
        global outArr
        global dp
        
        # what is  dp storing
            # for  each node Dp[i] stores first max , first max node and 2nd max
            
        dp = [ [-1,-1,-1] for i in range(A)]
        outArr = [ 0 for i in range(A) ] 
        for i in graph[0]:
            getOut( i, 0,-1)


        # res = []
        for i in range(A):
            inArr[i] = max(inArr[i], outArr[i])
        
        return inArr