"""Valid Ip Addresses


Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.

Example:

Given “25525511135”,

return [“255.255.11.135”, “255.255.111.35”]. (Make sure the returned strings are sorted in order)
"""
"""
Hint 1

You need to place only 3 dots and every segment should be a valid one.
"""
"""
Solution Approach

Brute force works here.

Essentially you have to place 3 dots in the given string.

Try out all the possible combinations for the 3 dots.

Corner case:

25011255255

    25.011.255.255 is not valid as 011 is not valid.
    25.11.255.255 is not valid either as you are not allowed to change the string.
    250.11.255.255 is valid.
"""
# @param A : string
# @return a list of strings
def restoreIpAddresses(A):
    res = []
    if len(A) >12:
        return 

    def check(n1,n2,n3,n4):
        # print(n1,n2,n3,n4)
        if n1[0] == '0' and len(n1) != 1:
            return False

        if n2[0] == '0' and len(n2) != 1:
            return False

        if n3[0] == '0' and len(n3) != 1:
            return False

        if n4[0] == '0' and len(n4) != 1:
            return False

        if int(n1) <= 255 and int(n2) <= 255 and int(n3)<=255 and int(n4)<=255:
            return True
        
        return False

    for i in range(1,4):
        for j in range(i+1, i+4):
            for k in range(j+1,j+4):
                if  k<len(A) and check(A[:i], A[i:j], A[j:k], A[k:]) :
                    res.append( A[:i] + "." + A[i:j] +  "." + A[j:k] + "." + A[k:])
    
    return res