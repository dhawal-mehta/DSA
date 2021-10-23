"""
Parity Queries


Problem Description

Given an empty multiset of integers initially and N queries to perform on it.

+ X — add non-negative integer X to the multiset. Note that there may be many occurrences of the same integer.

- X — delete a single occurrence of non-negative integer X from the multiset. It's guaranteed that there is at least one X in the multiset.

? S — count the number of integers in the multiset (with repetitions) that match some pattern S consisting of 0 and 1.

In the pattern, 0 stands for the even digits, while 1 stands for the odd. Integer X matches the pattern S if the parity of the ith from the right digit in decimal notation matches the ith from the right digit of the pattern.

If the pattern is shorter than this integer, it's supplemented with 0's from the left. Similarly, if the integer is shorter than the pattern, its decimal notation is supplemented with the 0's from the left.

For example, if the pattern is S = 010, then integers 92, 2212, 50, and 414 matches the pattern, while integers 3, 110, 25, and 1030 do not.

Given an array of characters A and an array of Strings B (representing the value of X for each query) of size N each, perform the queries and return the result for every third query in the form of an array of integers.


Problem Constraints

1 <= N <= 105

A[i] = {'+', '-', '?'}

0 <= B[i] <= 1018 (given in the form of string)


Input Format

The first argument given is the character array A.

The second argument given is the String array B.


Output Format

Return the answer for every third query in the form of an array of integers.


Example Input

Input 1:

 A = ['+', '+', '-', '?']
 B = [200, 200, 200, 0]

Input 2:

 A = ['+', '+', '?', '+', '-', '?']
 B = [1, 241, 1, 361, 241, 101]



Example Output

Output 1:

 [1]

Output 2:

 [2, 1]



Example Explanation

Explanation 1:

 Multiset after operation 1 : {200}
 Multiset after operation 2 : {200, 200}
 Multiset after operation 3 : {200}
 As only 1 element i.e. 200 in the multiset matches the pattern 0, thus answer is 1.

Explanation 2:

 Multiset after operation 1 : {1}
 Multiset after operation 2 : {1, 241}
 As both the elements i.e. 1 and 241 in the multiset match the pattern 1, thus answer is 2.
 Multiset after operation 3 : {1, 241, 361}
 Multiset after operation 1 : {1, 361}
 As only 1 element i.e. 361 in the multiset matches the pattern 101, thus answer is 1.
"""
"""
Hint 1

In order to solve this problem, try converting every digit of the given number into 0 (if it is even) and 1 (if it is odd).
Now, the pattern and the numbers are quite related.

Now, try thinking of a data structure to store these numbers and increment and decrement their count efficiently in maybe O(1) or O(logN).
"""
"""
Solution Approach

Try converting every digit of the number into 0 (if it is even) and 1 (if it is odd).
Then the number will appear to be in base 2 representation.
Pattern is also given in base 2 representation.

Use this to store / increment / decrement the count of every number and display when required.
"""
# @param A : list of characters
# @param B : list of strings
# @return a list of integers
def solve( A, B):
    # print(A, B)
    
    store = {}
    ans = []
    
    def binValue(num):
        if num ==0 :
            return 0
            
        ans = 0
        pow_ = 1
        while num!=0:
            temp = num%10 
            if temp & 1 == 1:
                
                ans +=  + pow_
                
            pow_ *= 2
            num = num//10
            
        return  ans
    
    def binValue2(patt):
        
        ans = 0
        for i in range(len(patt)):
            ans = ans*2 + int(patt[i])
        return ans

    for i in range(len(A)):
        if A[i] == '+':
            binVal = binValue(int(B[i]))
            
            if binVal in store:
                store[binVal] += 1
            else:
                store[binVal] = 1
                
        elif A[i] == '-':
            binVal = binValue(int(B[i]))
            
            store[binVal] -= 1
            if store[binVal] == 0:
                store.pop(binVal)
            
        else:
            
            pattBinValue = binValue2(B[i])
            temp = 0
            
            if pattBinValue in store:
                temp += store[pattBinValue]
            
            ans.append(temp)
                    
    
    return ans
