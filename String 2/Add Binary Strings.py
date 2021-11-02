"""
Add Binary Strings


Problem Description
Given two binary strings, return their sum (also a binary string).

Example:

a = "100"

b = "11"
Return a + b = "111".
"""
"""
Hint 1
This is exactly like adding 2 numbers.

    Note 1: It might be easier if you construct the reverse of the answer, reversing the strings that we have to add.
    Note 2: Make sure you don’t stop before carry is 0. (Cases like 11 + 1.)


"""
"""
Solution Approach

Since sizes of two strings may be different, we first make the size of smaller string equal to that of bigger string by adding leading 0s for simplicity
Note that you can handle the addition without adding zeroes as well by adding a few if statements.
After making sizes same, one by one, we add bits from rightmost bit to leftmost bit.
In every iteration, we need to sum 3 bits: 2 bits of 2 given strings and carry.

The sum bit will be 1 if, either all of the 3 bits are set or one of them is set.
So we can add all the bits and then take remainder with 2 to get the current bit in the answer.

How to find carry?

Carry will be 1 if any of the two bits is set. So we can find carry by adding the bits and dividing the result by 2.

Following is a step by step algorithm:

    Make them equal sized by adding 0s at the begining of smaller string.

    Perform bit addition

Boolean expression for adding 3 bits a, b, c

Sum = (a + b + c) % 2
Carry = (a + b + c ) / 2


"""
# @param A : string
# @param B : string
# @return a strings
def addBinary( A, B):
    A = A[::-1]
    B = B[::-1]
    rem = 0
    ans = ""
    for i in range(min(len(A),len(B))):
        temp = int(A[i]) + int(B[i]) + rem
        if temp%2 == 0:
            ans += '0'
        else:
            ans += '1'
        if temp > 1:
            rem = 1            
        else:
            rem = 0
        # print(ans,A[-i-1],B[-i-1])
    
    
    if len(A) > len(B):
        C = A
    else:
        C = B
    
    # print(ans)
    
    for i in range(min(len(A),len(B)), max(len(A),len(B))):
        temp = int(C[i]) + rem
        if temp % 2 == 0:
            ans += '0'
        else:
            ans += '1'
        
        if temp == 2:
            rem=1
        else:
            rem = 0
    
    if rem == 1:
        ans += '1'
    
    # print(ans)
    
    return ans[::-1]     