"""
Simplify Directory Path


Given a string A representing an absolute path for a file (Unix-style).

Return the string A after simplifying the absolute path.

Note:

    Absolute path always begin with ’/’ ( root directory ).

    Path will not have whitespace characters.



Input Format

The only argument given is string A.

Output Format

Return a string denoting the simplified absolue path for a file (Unix-style).

For Example

Input 1:
    A = "/home/"
Output 1:
    "/home"

Input 2:
    A = "/a/./b/../../c/"
Output 2:
    "/c"

"""
"""
Hint 1

You need to simulate whatever is stated. Stack can be useful here.
"""
"""
Solution Approach

More of a simulation problem.
Break the string along ‘/’ and process the substrings in order one by one. ‘..’ indicates popping an entry unless there is nothing to pop.
"""
# @param A : string
# @return a strings
def simplifyPath( A):
    
    arr = A.split('/')
    # print(arr)
    stk = []
    for i in range(0 , len(arr)):
        if arr[i] == '.':
            continue;

        elif arr[i] == '..':
            if len(stk) > 0: 
                stk.pop()

        elif arr[i] != '/' and len(arr[i]) > 0:
            stk.append(arr[i])
    
    # print()
    
    return '/'+'/'.join(stk) 