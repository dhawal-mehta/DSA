"""
Printing Shortest Common Supersequence

Given two strings X and Y, print the shortest string that has both X and Y as subsequences. If multiple shortest supersequence exists, print any one of them.
Examples: 
 

Input: X = "AGGTAB",  Y = "GXTXAYB"
Output: "AGXGTXAYB" OR "AGGXTXAYB" 
OR Any string that represents shortest
supersequence of X and Y

Input: X = "HELLO",  Y = "GEEK"
Output: "GEHEKLLO" OR "GHEEKLLO"
OR Any string that represents shortest 
supersequence of X and Y

"""
#code
def print_scs(s1,s2,n,m):
    t = [ [0]*(m+1) for i in range(n+1) ]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                t[i][j] = t[i-1][j-1] + 1
            else:
                t[i][j] = max(t[i-1][j] ,t[i][j-1] )
                
    # print(t[-1][-1])
    
    str_ = ""
    
    i = n 
    j = m
    
    while i>0 and j>0:
        if s1[i-1] == s2[j-1]:
            str_ += s1[i-1]
            i -= 1
            j -= 1
        else:
            if t[i-1][j] > t[i][j-1]:
                str_ += s1[i-1]
                i -= 1
            else:
                str_ += s2[j-1]
                j -= 1
    
    while i>0:
        str_ += s1[i-1]
        i-=1
    
    while j>0:
        str_ += s2[j-1]
        j-=1
        
    return str_[::-1]
    
X = "AGGTAB"
Y = "GXTXAYB"

res = print_scs(X,Y, len(X), len(Y))
print(res)
