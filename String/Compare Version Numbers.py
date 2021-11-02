"""Compare Version Numbers


Compare two version numbers version1 and version2.

        If version1 > version2 return 1,
        If version1 < version2 return -1,
        otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character. The . character does not represent a decimal point and is used to separate number sequences. For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 1.13 < 1.13.4
"""
"""
Solution Approach

Can you split two versions on ‘.’? How can it help you?
"""
# @param A : string
# @param B : string
# @return an integer
def compareVersion( A, B):
    v1 = A.split('.')
    v2 = B.split('.')
    
    l1 = len(v1)
    l2 = len(v2)
    
    # flag = 0
    
    for i in range( min(l1,l2) ):
        if int(v1[i]) > int(v2[i]):
            # flag = 1
            return 1
        
        elif int(v1[i]) < int(v2[i]):
            # flag = 1
            return -1
    
    
        
    
    
    if l1 > l2:
        for i in range(l1 - l2):
            if int(v1[l2 + i ]) > 0:
                return 1
                
    elif l1 < l2:
        for i in range(l2 - l1):
            if int(v2[l1 + i ]) > 0:
                return -1
        
    
    return 0