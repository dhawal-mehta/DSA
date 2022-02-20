"""
Shortest Unique Prefix


Problem Description

Given a list of N words. Find shortest unique prefix to represent each word in the list.

NOTE: Assume that no word is prefix of another. In other words, the representation is always possible



Problem Constraints

1 <= Sum of length of all words <= 106


Input Format

First and only argument is a string array of size N.


Output Format

Return a string array B where B[i] denotes the shortest unique prefix to represent the ith word.


Example Input

Input 1:

 A = ["zebra", "dog", "duck", "dove"]

Input 2:

A = ["apple", "ball", "cat"]



Example Output

Output 1:

 ["z", "dog", "du", "dov"]

Output 2:

 ["a", "b", "c"]



Example Explanation

Explanation 1:

 Shortest unique prefix of each word is:
 For word "zebra", we can only use "z" as "z" is not any prefix of any other word given.
 For word "dog", we have to use "dog" as "d" and "do" are prefixes of "dov".
 For word "du", we have to use "du" as "d" is prefix of "dov" and "dog".
 For word "dov", we have to use "dov" as "d" and do" are prefixes of "dog".  
 

Explanation 2:

 "a", "b" and c" are not prefixes of any other word. So, we can use of first letter of each to represent."""

"""
Hint 1

Use Prefix tree or Trie ( https://www.topcoder.com/community/data-science/data-science-tutorials/using-tries/ )

Assume you have all the prefixes of the word stored in the tree along with their frequencies. Is it possible to arrive at the solution now ?
"""
"""
Solution Approach

Lets take an example:

input: ["zebra", "dog", "duck", "dot"]

Now we will build prefix tree and we will also store count of characters

                root
                /|
         (d, 3)/ |(z, 1)
              /  |
          Node1  Node2
           /|        \
     (o,2)/ |(u,1)    \(e,1)
         /  |          \
   Node1.1  Node1.2     Node2.1
      | \         \            \
(g,1) |  \ (t,1)   \(c,1)       \(b,1)
      |   \         \            \ 
    Leaf Leaf       Node1.2.1     Node2.1.1
    (dog)  (dot)        \                  \
                         \(k, 1)            \(r, 1)
                          \                  \   
                          Leaf               Node2.1.1.1
                          (duck)                       \
                                                        \(a,1)
                                                         \
                                                         Leaf
                                                         (zebra)

Now, for every leaf / word , we find the character nearest to the root with frequency as 1. 
The prefix that the path from root to this character corresponds to, is the representation of the word. 

"""
class Node:
    def __init__(self, d):
        self.data = d
        self.count = 1
        self.children = [None]*26
        self.isTerminal = False

class Trie:
    def __init__(self):
        self.root = self.getNode()
    
    def getNode(self, d=None):
        return Node(d)
    
    def insert(self, key):
        temp = self.root
        for level in range(len(key)):
            index = ord(key[level]) - ord('a')
            
            if not temp.children[index]:
                temp.children[index] = self.getNode(key[level])
            else:
                temp.children[index].count += 1
            
            temp = temp.children[index]
        
        temp.isTerminal = True
    
    def search(self, key):
        temp = self.root
        for level in range(len(key)):
            index = ord(key[level]) - ord('a')
            
            if not temp.children[index] or temp.children[index].count == 1:
                return level
        
            temp = temp.children[index]
        
        return False
            


class Solution:
	# @param A : list of strings
	# @return a list of strings
	def prefix(self, A):
        
        trie = Trie()
        for i in A:
            trie.insert(i)
        
        ans = []
        
        for i in A:
            searchRes = trie.search(i)
            ans.append(i[:searchRes+1])

        
        return ans
