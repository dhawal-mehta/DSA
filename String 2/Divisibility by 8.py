"""
Divisibility by 8

Given a number A in the form of string. Check if the number is divisible by 8 or not.

Return 1 if it is divisible by 8 else return 0.


Input Format

The only argument given is string A.

Output Format

Return 1 if it is divisible by 8 else return 0.

Constraints

1 <= length of the String <= 100000
'0' <= A[i] <= '9'

For Example

Input 1:
    A = "16"
Output 1:
    1

Input 2:
    A = "123"
Output 2:
    0
"""
"""
Hint 1

Since input number may be very large, we cannot use n % 8 to check if a number is divisible by 8 or not, especially in languages like C/C++. The idea is based on following fact.

A number is divisible by 8 if number formed by last three digits of it is divisible by 8.
"""
# @param A : string
# @return an integer
def solve(A):
    if len(A) == 0:
        return 0
        
    if len(A) == 1 or len(A) == 2 or len(A) == 3 :
        num_ =int(A)
    
    else:
        num_ = ( int(A[-1]) + int(A[-2])*10 + int(A[-3])*100 )
    
    if num_%8 ==0:
        return 1
    else:
        return 0