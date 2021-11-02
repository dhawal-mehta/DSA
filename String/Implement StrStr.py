"""
 Implement StrStr


Another question which belongs to the category of questions which are intentionally stated vaguely.
Expectation is that you will ask for correct clarification or you will state your assumptions before you start coding.

Implement strStr().

    strstr - locate a substring ( needle ) in a string ( haystack ).

Try not to use standard library string functions for this question.

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

    NOTE:

    Good clarification questions:

        What should be the return value if the needle is empty?

        What if both haystack and needle are empty?

    For the purpose of this problem, assume that the return value should be -1 in both cases.
"""
"""
Hint 1

Lets say M is length of haystack and N is length of needle. Then expected complexity here is O(N*M).
"""
# @param A : string
# @param B : string
# @return an integer
def strStr( A, B):
    if len(A) == 0 or len(B) == 0 or len(A) < len(B):
        return -1


    needle = B
    haystk = A
    
    lps = [0]*len(needle)
    
    start= 0
    end= 1
    
    while end < len(needle):
        if needle[start] == needle[end]:
            lps[end] = start + 1
            start+=1
            end += 1
        else:
            if start == 0:
                lps[end] = 0
                end += 1
            else:
                start = lps[start-1]

    j = 0
    i = 0
    
    while i < len(haystk):
        if j == len(needle):
            return i-len(needle)
        
        if needle[j] == haystk[i]:
            i+=1
            j+=1
        else:
            if j==0:
                i+=1
            else:
                j= lps[j-1]
    
    if j == len(needle):
        return i-len(needle)
    
    return -1