"""
Integer To Roman

Another question which belongs to the category of questions which are intentionally stated vaguely.
Expectation is that you will ask for correct clarification or you will state your assumptions before you start coding.

Given an integer A, convert it to a roman numeral, and return a string corresponding to its roman numeral version

    Note : This question has a lot of scope of clarification from the interviewer. Please take a moment to think of all the needed clarifications and see the expected response using "See Expected Output"

    For the purpose of this question, https://projecteuler.net/about=roman_numerals has very detailed explanations.


Input Format

The only argument given is integer A.

Output Format

Return a string denoting roman numeral version of A.

Constraints

1 <= A <= 3999

For Example

Input 1:
    A = 5
Output 1:
    "V"

Input 2:
    A = 14
Output 2:
    "XIV"
"""
"""
Hint 1
Think of some essential numbers whose roman numeral representations can be used to construct other numbers. Its really similar to constructing numbers in different bases after that.
"""
"""
Solution Approach

It is very much like learning our own number system.

All you need to know is how to write 0-9, 10, 20, 30, 40, .. 90, 100, 200, 300,… 900, 1000, 2000, 3000.

You can derive rest of the numbers using the above.
"""
# @param A : integer
# @return a strings
def intToRoman( A):
    res = ""
    
    curr = A
    while curr >= 1000:
        res += "M"
        curr -= 1000
    if curr>=900:
        res += "CM"
        curr -= 900
    
    if curr>=500:
        res += "D"
        curr -= 500
    
    if curr>=400:
        res += "CD"
        curr -= 400
    
    while curr>=100:
        res += "C"
        curr -= 100
    if curr>=90:
        res += "XC"
        curr -= 90
    
    if curr >= 50:
        res += "L"
        curr -= 50
        
    if curr >= 40:
        res+="XL"
        curr -= 40
    
    while curr>=10:
        res += "X"
        curr -= 10
    
    if curr >= 9:
        res+= "IX"
        curr -= 9
    
    if curr >=5:
        res += "V"
        curr -= 5
        
    if curr >= 4:
        res += "IV"
        curr -= 4
        
    while curr > 0:
        res += "I"
        curr -= 1
        
    return res
