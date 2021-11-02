"""
Check two bracket expressions

Problem Description

Given two strings A and B. Each string represents an expression consisting of lowercase english alphabets, '+', '-', '(' and ')'.

The task is to compare them and check if they are similar. If they are similar return 1 else return 0.

NOTE: It may be assumed that there are at most 26 operands from ‘a’ to ‘z’ and every operand appears only once.


Problem Constraints

1 <= length of the each String <= 100


Input Format

The arguments given are string A and String B.


Output Format

Return 1 if they represent the same expression else return 0.


Example Input

Input 1:

 A = "-(a+b+c)"
 B = "-a-b-c"

Input 2:

 A = "a-b-(c-d)"
 B = "a-b-c-d"



Example Output

Output 1:

 1

Output 2:

 0



Example Explanation

Explanation 1:

 The expression "-(a+b+c)" can be written as "-a-b-c" which is equal as B. 

Explanation 2:

 Both the expression are different.

"""
"""
Hint 1


Since the each operand appear atmost once. In both strings A and B, there should be equal sign on each operand.

Can you use stack for simplify the expression A and B?

"""
"""
Solution Approach

We will evaluate each expression one by one.

Calculate the sign on each operand present from ‘a’ to ‘z’ for first string A.

Now, repeat the same process again on string B but with opposite sign.

If the total sign on each operand is 0, return 1.

Else return 0.
"""
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def sanitize(self, str_):
        
        i = 0
        prevSign = "+"
        stk = ["+"]
        
        sanitized = ""
        while i < len(str_):
            if str_[i] == '-' or str_[i] == "+":
                # if stk[-1] == '-':
                #     if str_[i] == '-':
                #         sanitized += '+'
                #     else:
                #         sanitized += '-'
                    
                # else:
                #     sanitized += str_[i]
                
                prevSign = str_[i]
                
            elif str_[i] == '(' or str_[i] == ')':
                if str_[i] == '(':
                    if stk[-1] == '-':
                        if prevSign == '-':
                            stk.append('+')
                        else:
                            stk.append('-')
                    else:
                        stk.append(prevSign)
                        
                elif str_[i] == ')':
                    stk.pop()
            else:
                if stk[-1] == '-':
                    if prevSign == '-':
                        sanitized += '+' + str_[i]
                    else:
                        sanitized += '-' + str_[i]
                else:
                    sanitized +=  prevSign + str_[i]
            
            i+=1
            
        return sanitized   
                
                
        
    def solve(self, A, B):
        A = self.sanitize(A)
        B = self.sanitize(B)
        
        print(A)
        print(B)
        
        if A == B:
            return 1
        else:
            return 0