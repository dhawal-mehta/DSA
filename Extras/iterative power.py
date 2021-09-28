"""
iterative power

iterative O(Log y) function for pow(x, y)

    Difficulty Level : Medium
    Last Updated : 07 Jul, 2021

Given an integer x and a positive number y, write a function that computes xy under following conditions. 
a) Time complexity of the function should be O(Log y) 
b) Extra Space is O(1) 

Examples: 

Input: x = 3, y = 5
Output: 243

Input: x = 2, y = 5
Output: 32
"""
# Iterative Python3 program
# to implement pow(x, n)
# Iterative Function to
# calculate (x^y) in O(logy)

def power(x, y):
    res = 1
    while (y > 0):
        if ((y & 1) == 1) :
            res = res * x

        y = y >> 1
        x = x * x
     
    return res