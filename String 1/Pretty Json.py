"""
Pretty Json

Given a string A representating json object. Return an array of string denoting json object with proper indentaion.

Rules for proper indentaion:

    Every inner brace should increase one indentation to the following lines.
    Every close brace should decrease one indentation to the same line and the following lines.
    The indents can be increased with an additional '\t'

Note:

    [] and {} are only acceptable braces in this case.

    Assume for this problem that space characters can be done away with.


Input Format

The only argument given is the integer array A.

Output Format

Return a list of strings, where each entry corresponds to a single line. The strings should not have "\n" character in them.

For Example

Input 1:
    A = "{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}"
Output 1:
    { 
        A:"B",
        C: 
        { 
            D:"E",
            F: 
            { 
                G:"H",
                I:"J"
            } 
        } 
    }

Input 2:
    A = ["foo", {"bar":["baz",null,1.0,2]}]
Output 2:
   [
        "foo", 
        {
            "bar":
            [
                "baz", 
                null, 
                1.0, 
                2
            ]
        }
    ]
"""
"""
Hint 1
This is more of a parsing/simulation problem. Think about the corner cases wisely.
"""
"""
Solution Approach

This is more of a parsing problem.

Make sure you take a lot of time thinking about the corner cases and structure of the code before you start coding.

Fixing corner cases on the fly can make your code really ugly.

Note the following:

1) ‘{‘, ‘[’ have the same effect on the printing

2) ‘}’, ‘]’ have the same effect as well

3) ‘:’ and ‘,’ are the only other 2 characters that matter.

Think about the behavior when you encounter the following characters.

Also think about the behavior based on the following character.

"""
# @param A : string
# @return a list of strings
def prettyJSON( A):
    
    num_tabs = 0
    i = 0
    ans = []
    while i < len(A):
        # print("*** ",i,A[i])
        # if A[i] == " ":
        #     i+=1
        #     continue
        
        str_= ""
        
        if A[i] == '{' or A[i]=='[':                
            str_ += "\t"*num_tabs + A[i]                    
            num_tabs += 1
            i+=1
        
        elif A[i] == '}' or A[i]==']':
            num_tabs -= 1
            str_ += "\t"*num_tabs + A[i]
            i+=1                    
        else:
            str_ += "\t"*num_tabs
            # print("+++*", i, A[i])
            while A[i] != ',' and A[i] != '}' and A[i]!= ']' and A[i] != '{' and A[i] != '[':
                str_ += A[i]
                i+=1
                # print("**", i,A[i])
                
        if i< len(A) and A[i] == ",":
            str_ += A[i]
            i+=1
        
        ans.append(str_)
    
    return ans