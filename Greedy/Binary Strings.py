"""
Binary Strings


Problem Description

You are given a string A consisting of 1's and 0's. Now the task is to make the string consisting of only 1's. But you are allowed to perform only the following operation:
Take exactly B consecutive elements of string and change 1 to 0 and 0 to 1.

Each operation takes 1 unit time so you have to determine the minimum time required to make the string of 1's only. If not possible return -1.



Problem Constraints

2 ≤ length of A ≤ 105
2 ≤ B ≤ (length of A)


Input Format

First argument is a string A consisting if 1's and 0's.
Second argument is an integer B which represents the number of consecutive elements which can be changed.


Output Format

Return an integer which is the minimum time to make the string of 1's only or -1 if not possible.


Example Input

Input 1:

 A = "00010110"
 B = 3

Input 2:

 A = "011"
 B = 3



Example Output

Output 1:

 3

Output 2:

 -1



Example Explanation

Explanation 1:

 You can get 1 by first changing the leftmost 3 elements, getting to 11110110, then the rightmost 3, getting to 11110001, 
 and finally the 3 left out 0's to 11111111; In 3 unit time.

Explanation 2:

It's not possible to convert the string into string of all 1's.
"""
"""
Hint 1

Think of a greedy approach to solve this problem.

"""
"""
Solution Approach

Let us follow a greedy strategy.

Maintain an answer = 0.
Also maintain a variable and an auxillary array, let’s say xr and temp respectively.
Initially both are 0.

Start from the leftmost index of the string and iterate till the index ((string length)-B).
Now consider the curr index is i.
Firstly, xr = xr ^ temp[i]
If ( A[i] == ‘1’ && xr == 1) || (A[i] == ‘0’ && xr == 0) then incrememt the answer.
Also mark temp[i+B] as 1 and xr = 1 - xr.

Now check for the remaining elenents and if there is any 0 return -1.
Else,
Return ans

Time Complexity : O(N)
Space Complexity: O(N)
"""
class Solution:
    def solve(self, A, B):
        status = True
        
        def util(bin, start, k):
            ans = 0

            while start < len(bin)-k:
                if bin[start] == "1":
                    start+=1
                    continue
                
                else:
                    ans += 1
                    newBin = ""
                    temp = start
                    postK_Bin = bin[start+k:]
                    for i in range(temp ,start+k):
                        if bin[temp] == "1":
                            newBin += '0'
                        else:
                            newBin+='1'
                            
                        temp += 1

                    bin = bin[:start] + newBin + postK_Bin

            while start < len(bin)-1:
                if bin[start] == bin[start+1]:
                    start += 1
                    continue
                else:
                    return -1
            
            if bin[-1] == '1':
                return ans
            else:
                return ans+1
                
        ans = util(A,0,B)
        
        return ans