"""
Smallest Good Base


Given an integer A, we call k >= 2 a good base of A, if all digits of A base k are 1. Now given a string representing A, you should return the smallest good base of A in string format.


Input Format

The only argument given is the string representing A.

Output Format

Return the smallest good base of A in string format.

Constraints

3 <= A <= 10^18

For Example

Input 1:
    A = "13"
Output 1:
    "3"     (13 in base 3 is 111)

Input 2:
    A = "4681"
Output 2:
    "8"     (4681 in base 8 is 11111).
"""
# @param A : string
# @return a strings
def solve(self, A):
    
    for k in range(60, 2, -1):
        start = 2
        end = int(A)
        
        while start < end:
            mid = (start+end)//2

            calc = mid**k
            calc -= 1
            calc //= mid-1
                
            if calc == int(A):
                return mid
            
            elif calc < int(A):
                start = mid+1
            else:
                end = mid 
    
    return str(int(A)-1)
