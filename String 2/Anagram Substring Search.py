"""Anagram Substring Search


Given a string A and a string B.

Find and return the starting indices of the substrings of A which matches any of the anagrams of B.

Note: An anagram is a play on words created by rearranging the letters of the original word to make a new word or phrase


Input Format

The arguments given are string A and string B.

Output Format

Return the starting indices of the substrings of A which matches any of the anagrams of B.

Constraints

1 <= length of the string A,B <= 100000
length of string A > length of string B
'a' < = A[i] ,B[i] < ='z'

For Example

Input 1:
    A = "BACDGABCDA"
    B = "ABCD"
Output 1:
    [0, 5, 6]

Input 2:
    A = "AAABABAA"
    B = "AABA"
Output 2:
    [0, 1, 4]
"""
# @param A : string
# @param B : string
# @return a list of integers
def solve( A, B):
    Bhash = {}
    
    for i in B:
        if i in Bhash:
            Bhash[i] += 1
        else:
            Bhash[i] = 1
            
    
    tempHash = {}
    count = 0
    ans = []
    
    start=0
    end = len(B)
    for i in range(len(B)):
        if A[i] in Bhash:
            if A[i] in tempHash:
                tempHash[A[i]] += 1
            else:
                tempHash[A[i]] = 1
            count += 1

    # print(Bhash, tempHash)
    
    # tempHash["A"] +=1
    # print(Bhash == tempHash)
    
    for i in range(len(B), len(A)):
        if tempHash == Bhash:
            ans.append(start)
        
        if A[start] in tempHash:
            tempHash[ A[start] ] -= 1
            
        start +=1
        
        if A[i] in Bhash:
            if A[i] in tempHash:
                tempHash[A[i]] += 1
            else:
                tempHash[A[i]] = 1
                
    # 'print(ans)
    # if count == len(B):
            
    
    return [0]