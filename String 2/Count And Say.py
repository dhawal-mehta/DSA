"""Count And Say

Problem Description
The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...

1 is read off as one 1 or 11. 11 is read off as two 1s or 21.

21 is read off as one 2, then one 1 or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Example:

if n = 2, the sequence is 11."""
"""
Hint 1
You need to figure out how the new sequence is constructed from old sequence by counting contiguous same numbers.
"""
"""
Solution Approach

The best way is to simulate.

Try constructing the sequence starting from 1.

For constructing the current sequence, you need to look at the previous sequence and count the size of the contiguous sequences.
"""
# @param A : integer
# @return a strings
def countAndSay( A):
    if A == 1:
        return "1"
    pre = "1"
    ret = ""
    while A > 1:
        ret = ""
        i = 0
        while i < len(pre):
            j = i + 1
            c = 1
            while j < len(pre) and pre[j] == pre[j-1]:
                c += 1
                j += 1
            i = j
            ret += str(c) + pre[j-1]
        pre = ret
        A -= 1
