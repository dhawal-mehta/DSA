"""
Efficient program to print all prime factors of a given number


Given a number n, write an efficient function to print all prime factors of n. 
For example, if the input number is 12, then output should be “2 2 3”. And if the input number is 315, then output should be “3 3 5 7”.

"""
"""
Solution Approach 

Following are the steps to find all prime factors. 
1) While n is divisible by 2, print 2 and divide n by 2. 
2) After step 1, n must be odd. Now start a loop from i = 3 to square root of n. While i divides n, print i and divide n by i. After i fails to divide n, increment i by 2 and continue. 
3) If n is a prime number and is greater than 2, then n will not become 1 by above two steps. So print n if it is greater than 2. 
"""
import math

def primeFactors(n):    
    while n % 2 == 0:
        print (2),
        n = n / 2
         
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            print (i),
            n = n / i    
    if n > 2:
        print (n)