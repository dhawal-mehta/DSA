"""
Same Format String


Problem Description
Given two strings A and B. Check if B contains same characters as that of given string A and in the same order.



Problem Constraints

1: A and B contain only UPPERCASE Letters.
2: No two consecutive characters are same in A.
3: You can only use constant amount of extra memory.


Input Format

The first argument given is string A.
The second argument given is string B.


Output Format

Return 1 if B contains same characters as that of given string A and in the same order else return 0.


Example Input

Input 1:

    A = "HIRED" 
    B = "HHHIIIRRRRREEEEEDDDDD"

Input 2:

    A = "HIRED"
    B = "DDHHHHIIIIRRRRREEEEDDD"



Example Output

Output 1:

    1

Output 2:

    0



Example Explanation

Explanation 1:

    B has same characters and appear in same order.

Explanation 2:

    B has extra character "D"
"""
"""
Hint 1
We can not use extra memory.
Try not to compress string B into another temporary string.
"""
"""
Solution Approach

We can easily observe that both the strings are matched if compressed version of string B is same as string A.
Here compressed means if there are two or more than two consecutive characters are same replace them with a single character.
Example : Compressed version of “ABBCCCSSS” will be “ABCS”
It is very easy to compress string B into some other temporary string C.
Now if A is same as C then strings A and B are of same format otherwise not.
As we can only take constant extra space so we can not take another temporary string C.
For coping this problem we can simply make a comparision of compressed segment of B corresponding to that character in A.
(A simple iterations can do this)

i = 0,j = 0,n = size of A,m = size of B;
while( i < n && j < m)
{
    count = 0;
    //count how many times the current character is available in string B
    while(j < m && B[j] == A[i])
    {
        count++;
        j++;
    }
    // if count does not greater than one, return unmatched
    if(count == 0)
    unmatched;
    i++;
}
here check if both the strings have been completely used up then other strings are matched, 
if there are still characters left in A or B string are unmatched.

"""
# @param A : string
# @param B : string
# @return an integer
def solve( A, B):
    j = 0
    count_ = 0
    
    if len(A) == 0 and len(B) != 0:
        return 0
        
    if len(A) == 0 and len(B) == 0:
        return 1
        
    for i in A:
        if j == len(B):
            break
        
        if B[j] != i:
            return 0
        
        while(j < len(B) and B[j] == i):
            j+=1
            
        count_ += 1
            
    if count_ != len(A) or j != len(B):
        return 0
        
    return 1