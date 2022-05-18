"""
Longest Common Subsequence

Given two sequences, find the length of longest subsequence present in both of them. 
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. 
For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. 

Examples: 
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3. 
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4. 

"""
def lcs(X , Y):
    m = len(X)
    n = len(Y)
 
    L = [[0]*(n+1) for i in range(m+1)]
 
    for i in range(1,m+1):
        for j in range(1, n+1):

            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
    return L[m][n]

X = "AGGTAB"
Y = "GXTXAYB"
print ("Length of LCS is ", lcs(X, Y) )