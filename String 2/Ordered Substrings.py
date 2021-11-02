"""
Ordered Substrings


You are given an array A consisting of strings. You are supposed to order the given strings in such a way that for a particular string, all strings ordered before it exist as its substrings.

Each string is made up of lowercase English letters.

Return an array consisting of the correct order of strings. If it is not possible to do so, return a vector consisting of one element, which is the string "NO".

Input:

A: Array of strings.

Output:

Return an array consisting of the correct order of strings. If it is not possible to do so, return a vector consisting of one element, which is the string "NO".

Constraints:

Strings in A consist of lowercase English letters
1 <= size(A) <= 100
1 <= size of strings in A <= 100
Some strings might be equal

Example:

Input:
A: [abc, abcd, a, abc]

Output:
[a, abc, abc, abcd]

Input:
A: [xyz, xz, xyzzy]

Output:
[NO]
"""
"""
Hint 1
A string would be the substring of it’s parent string only if it’s length is <= the length of it’s parent string.

Hence, if you check strings lengthwise, it will be easier.
"""
"""
Solution Approach

We basically need to sort the strings with respect to it’s length, and then check if the shorter string is a substring of the larger string.

We can sort it with respect to it’s length by making a vector of pairs, where the first element of the pair is the string length, and the second element is the actual string.
Using the sort function will sort with respect to the first element of the pair, which is the length.
"""
class Solution:
    # @param A : list of strings
    # @return a list of strings
    def strstr(self, A, B):
        
        lps = [0]*len(B)
        
        start=0
        end = 1
        
        while end < len(B):
            if B[start] == B[end]:
                lps[end]= start+1
                end += 1
                start += 1
            else:
                if start == 0:
                    lps[end] = 0
                    end += 1
                else:
                    start = lps[start-1]
        
        j = 0
        i = 0
        # print(lps)
        
        while i < len(A):
            if j == len(B):
                return True
                
            if A[i] == B[j]:
                i+=1
                j+=1
            else:
                if j != 0:
                    j=lps[j-1]
                else:
                    i+=1
        if j==len(B):
            return True
            
        return False
        
                
            
        
    def solve(self, A):

        
        for i in range(len(A)-2,-1,-1):
            
            curr = i
            for j in range(i+1,len(A)):

                if self.strstr(A[j], A[curr]):
                    break
                    
                elif self.strstr(A[curr],A[j]):
                    A[curr],A[j] = A[j], A[curr]
                    curr = j
                else:

                    return ["NO"]
                
        
        return A