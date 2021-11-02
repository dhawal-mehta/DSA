"""
Roman To Integer


Given a string A representing a roman numeral. Convert A into integer.

A is guaranteed to be within the range from 1 to 3999.

NOTE: Read more details about roman numerals at Roman Numeric System


Input Format

The only argument given is string A.

Output Format

Return an integer which is the integer verison of roman numeral string.

For Example

Input 1:
    A = "XIV"
Output 1:
    14

Input 2:
    A = "XX"
Output 2:
    20
"""
"""
Hint 1
Note how the number XVI(10+5+1) and XIV(10-1+5) differs.

In one case we are adding the numeric value of a letter and in other case we are subtracting it. How can you simulate this?
"""
"""
Solution Approach

The key is to notice that in a valid Roman numeral representation the letter with the most value always occurs at the start of the string.

Whenever a letter with lesser value precedes a letter of higher value, it means its value has to be added as negative of that letter’s value.

In all other cases, the values get added.

"""

# @param A : string
# @return an integer
def romanToInt( A):
    
    i = 0
    num ={"M":1000, "CM":900, "D":500,"CD":400  , "C":100,"XC":90  ,"L":50, "XL":40, "X":10,"IX":9,"V":5,"IV":4 ,"I":1}
    
    res = 0
    while i < len(A):
        if i<len(A)-1 and num[A[i]] < num[A[i+1]]:
            temp = A[i] + A[i+1]
            res += num[temp]
            i+=2
        else:
            res += num[A[i]]
            i+=1
    
    return res