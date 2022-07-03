"""
Word Ladder II


Given two words (start and end), and a dictionary, find the shortest transformation sequence from start to end, such that:

        Only one letter can be changed at a time
        Each intermediate word must exist in the dictionary

If there are multiple such sequence of shortest length, return all of them. Refer to the example for more details.

Note:

        All words have the same length.
        All words contain only lowercase alphabetic characters.

Input Format

The first argument is string start.
The second argument is string end.
The third argument is an array of strings dict

Output Format

Return all transformation sequences such that first word of each sequence is start and last word is end, all intermediate words belongs to dictionary(dict) and consecutive words had atmost 1 difference.  

Example :

:

start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]

Return

  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
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

Once you know about the shortest path, how do we construct all shortest paths ?
When will a node x be a parent of node Y ?

"""
class Solution:
    def findLadders(self, start, end, dictV):

        if start==end:
            return [ [start] ]

        # if dictV[-2] == dictV[-1]:
        #     return [[dictV[-1]]]
        
        from collections import deque
        
        # what is use of s?? for pos of word in dict
        s = {}
        for i in range(len(dictV)):
            s[dictV[i]] = i
            
        visited = [0]*len(dictV)
        
        ladders = []
        de = deque()
        de.append([len(dictV)-2, 1, [dictV[-2]]])
        
        minWt= float('inf')
        while de:
            # print(de)
            curr, wt , ladder = de.popleft()
            # print(curr, wt, ladder, ladders)
            visited[curr] = 1
            
            if curr == len(dictV)-1:
                if wt == minWt:
                    # print(ladder)
                    ladders.append(ladder)
                elif wt < minWt:
                    minWt = wt
                    ladders = [ladder]
            
            else:
                for i in range( len(dictV[curr]) ):
                    word = dictV[curr]
                    for alpha in 'abcdefghijklmnopqrstuvwxyz':
                        
                        neword = word[:i] + alpha + word[i+1:]
                        
                        
                        if alpha != word[i] and neword in s and visited[s[neword]] == 0:
                            # print("ghehe")
                            de.append( [s[neword], wt+1, ladder+[neword]] )
            
        return ladders