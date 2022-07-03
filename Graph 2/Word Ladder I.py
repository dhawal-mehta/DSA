"""
Word Ladder I


Problem Description

Given two words A and B, and a dictionary C, find the length of shortest transformation sequence from A to B, such that:

    You must change exactly one character in every transformation.
    Each intermediate word must exist in the dictionary.

NOTE:

    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.



Problem Constraints

1 <= length(A), length(B), length(C[i]) <= 25
1 <= length(C) <= 5000


Input Format

The first argument of input contains a string, A.

The second argument of input contains a string, B.

The third argument of input contains an array of strings, C.



Output Format

Return an integer representing the minimum number of steps required to change string A to string B.


Example Input

Input 1:

 A = "hit"
 B = "cog"
 C = ["hot", "dot", "dog", "lot", "log"]

Input 2:

 A = "cat"
 B = "bat"
 C = ["rat"]

Input 3:

 A = "bait"
 B = "pant"
 C = ["a","b"]



Example Output

Output 1:

 5

Output 2:

 2

Output 3:

 0



Example Explanation

Explanation 1:

 "hit" -> "hot" -> "dot" -> "dog" -> "cog"

Explanation 2:

 "cat" -> "bat"

Explanation 3:

 No intermediate words are present in the given dictionary so transformation is not possible. We will return 0 for this case.
"""
"""
Hint 1

Think in terms of a graph.

When can you do the transition from one word to another ? Does it mean it can indicate a graph edge between those 2 words ? How can this graph help you to achieve the purpose?

"""
"""
Solution Approach

This is a classic shortest path problem.

Think in terms of a graph. You basically need to add an edge between two words which can be converted into one another. Resulting graph will be unweighted and undirected.

Which graph traversal algorithm can now help you in computing the shortest path in undirected, unweighted graph?

"""
class Solution:
    # @param A : string
    # @param B : string
    # @param C : list of strings
    # @return an integer
    def solve(self, A, B, C):
        
        C.append(A)
        C.append(B)
        graph = [ [] for i in range(len(C)) ]
        
        
        def getNumChar(i, j):
            if len(C[i]) != len(C[j]):
                return 1
                
            count = 0
            
            for curr in range(len(C[i])):
                if C[i][curr] != C[j][curr]:
                    count += 1
                    if count == 2:
                        return 2
            
            return 1
        
        for  i in range(len(C)-1):
            for j in range(i+1, len(C)):
                if getNumChar(i, j) == 1:
                    graph[i].append(j)
                    graph[j].append(i)
        

        from collections import deque
        
        def bfs(graph):
            res = float('inf')
            de = deque()
            
            visited = [0]*len(C)            
            visited[len(C)-2] = 1
            de.append([len(C)-2, -1,1])
            
            while de:
                curr, prev , wt = de.popleft()
                visited[curr] += 1
                
                if curr == len(C)-1:
                    res = min(res, wt)
                else:
                    for i in graph[curr]:
                        if i!= prev and visited[i] == 0:
                            visited[i] = 1
                            de.append([i, curr, wt+1])                            
            
            return res if res != float('inf') else 0

        return bfs(graph)
        
        
        