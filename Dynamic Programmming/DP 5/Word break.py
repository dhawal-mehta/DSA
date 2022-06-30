"""
Word Break

Given a string A and a dictionary of words B, determine if A can be segmented into a space-separated sequence of one or more dictionary words.

Input Format:

The first argument is a string, A.
The second argument is an array of strings, B.

Output Format:

Return 0 / 1 ( 0 for false, 1 for true ) for this problem.

Constraints:

1 <= len(A) <= 6500
1 <= len(B) <= 10000
1 <= len(B[i]) <= 20

Examples:

Input 1:
    A = "myinterviewtrainer",
    B = ["trainer", "my", "interview"]

Output 1:
    1

Explanation 1:
    Return 1 ( corresponding to true ) because "myinterviewtrainer" can be segmented as "my interview trainer".

Input 2:
    A = "a"
    B = ["aaa"]

Output 2:
    0

Explanation 2:
    Return 0 ( corresponding to false ) because "a" cannot be segmented as "aaa".
"""
"""
Hint 1

Can you calculate the answer if you know which all substring of the given string are there in the dictionary?

Think of DP.

"""
"""
Solution Approach

Lets again look at the bruteforce solution.
You start exploring every substring from the start of the string, and check if its in the dictionary. If it is, then you check if it is possible to form rest of the string using the dictionary words. If yes, my answer is true. If none of the substrings qualify, then our answer is false.

So something like this :

    bool wordBreak(int index, string &s, unordered_set<string> &dict) {
                    // BASE CASES
        
        bool result = false;
        // try to construct all substrings.
        for (int i = index; i < s.length(); i++) {
            substring = *the substring s[index..i] with i inclusive*
            if (dict contains substring) {
                result |= wordBreak(i + 1, s, dict); // If this is true, we are done. 
            }
        }
        return result;
    }

This solution itself is exponential. However, do note that we are doing a lot of repetitive work.
Do note, that index in the wordBreak function call can only take s.length() number of values [0, s.length]. What if we stored the result of the function somehow and did not process it everytime the function is called ?

"""
class TrieNode():
    def __init__(self):
        self.children = {}
        self.isLeaf = False
    
    def insert(self, root , key):
        key = str(key)
        
        curr = root
        
        for i in key:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            
            curr = curr.children[i]
            
            
        curr.isLeaf = True
        
            
    def checkWordBreak(self, root, A, tart):
        # print("new", A[tart])
        # A = str(A)
        if tart >= len(A):
            return True
        
        curr = root
        
        for i in range(tart, len(A)):
            # print(A[i], curr.isLeaf)
            
            if A[i] in curr.children and curr.children[A[i]].isLeaf :
                if self.checkWordBreak(root, A, i+1):
                    return True
            
            
            if A[i] not in curr.children:
                return False
            
            curr = curr.children[A[i]]
        
        if curr.isLeaf:
            return True
            
        return False
        

        
        # return False

class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        
        # dp = [ [ 0 for i in range(len(A)) ] for j  in range(len(A))]
        # B = set(B)
        # for size in range(1, len(A)+1):
        #     for j in range(size-1, len(A)):
        #         i = j - size + 1
        #         if A[i:j+1] in B:
        #             dp[i][j] = 1
        #         else:
        #             for k in range(j-1,-1,-1):
        #                 # if i == 0:
        #                 #     print(i,j,k , A[i:k+1], " ",A[k+1:j+1])
        #                 if dp[i][k] == 1 and dp[k+1][j] == 1:
        #                     dp[i][j] = 1
        # return dp[0][-1]
        
        #----------------- slow ------------
        
        # def getKmpArr(word):
        #     kmp = [0]*len(word)
            
        #     start = 0
        #     end = 1
        #     while end < len(word):
        #         if word[start] == word[end]:
        #             start += 1
        #             kmp[end] = start
        #             end += 1
                    
        #         else:
        #             if start == 0:
        #                 kmp[end] = 0
        #                 end += 1
        #             else:
        #                 start = kmp[start-1]

        #     return kmp
            
        # def getAllPos(bigStr, smallStr):
        #     kmp = getKmpArr(smallStr)
        #     # print(kmp)
            
        #     res = []
            
        #     bigPos = 0
        #     smallPos = 0
        #     while(bigPos < len(bigStr)):
                
        #         if smallPos == len(smallStr):
        #             res.append(bigPos - len(smallStr))
        #             smallPos = kmp[-1]
                    
                
        #         if bigStr[bigPos] == smallStr[smallPos]:
        #             bigPos += 1
        #             smallPos += 1
        #         else:
        #             if smallPos == 0:
        #                 bigPos += 1
        #             else:
        #                 smallPos = kmp[smallPos-1]
                        
        #     if smallPos == len(smallStr):
        #         res.append(bigPos - len(smallStr))
            
        #     return res
        
        # def isPresent(Arr, num, L):
        #     if num == L:
        #         return 1
                
        #     if num not in Arr:
        #         return 0
            
        #     for i in Arr[num]:
        #         if isPresent(Arr, i+1, L) == 1:
        #             return 1
            
        #     return 0
        
        # posArr = {}
        # for i in B:
            
        #     temp = getAllPos(A, i)
            
        #     for start in temp:
        #         try:
        #             posArr[start].append(start + len(i) -1)
        #         except:
        #             posArr[start] = [start + len(i) - 1]    
        
        # temp = isPresent(posArr, 0 , len(A))
        
        # return temp
        
        # ------------- TLE -------------------
        
        root = TrieNode()
        for i in B:
            root.insert(root, i)
        

        return 1 if root.checkWordBreak(root, A, 0) else 0 
        
