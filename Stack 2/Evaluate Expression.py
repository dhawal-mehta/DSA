"""
Evaluate Expression


Problem Description

An arithmetic expression is given by a charater array A of size N. Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each character may be an integer or an operator.



Problem Constraints

1 <= N <= 105


Input Format

The only argument given is character array A.


Output Format

Return the value of arithmetic expression formed using reverse Polish Notation.


Example Input

Input 1:
    A =   ["2", "1", "+", "3", "*"]

Input 2:
    A = ["4", "13", "5", "/", "+"]



Example Output

Output 1:
    9

Output 2:
    6



Example Explanation

Explaination 1:
    starting from backside:
    * : () * ()
    3 : () * (3)
    + : (() + ()) * (3)
    1 : (() + (1)) * (3)
    2 : ((2) + (1)) * (3)
    ((2) + (1)) * (3) = 9

Explaination 2:
    + : () + ()
    / : () + (() / ())
    5 : () + (() / (5))
    1 : () + ((13) / (5))
    4 : (4) + ((13) / (5))
    (4) + ((13) / (5)) = 6
"""
"""
Hint 1
Start processing from start. What happens when you encounter an operand? How elements are affected? Can you simulate it.
"""
"""
Solution Approach

This is pretty much a simulation problem.
Think stack.

When you encounter an operator is when you need the top 2 numbers on the stack, perform the operation on them and put them on the stack.

"""
# @param A : list of strings
# @return an integer
def evalRPN(A):
    stk = []
    for i in A:
        if i =='+' or i='-' or i=='*' or i == '/':
            num2 = stk.pop()
            num1 = stk.pop()
            if i == '+':
                stk.append(num1+num2)
            elif i==-:
                stk.append(num1-num2)
            elif i==*:
                stk.append(num1*num2)
            elif i=='/':
                stk.append(num1//num2)
        else:
            stk.append(int(i))
        
    return stk[-1]