"""
Seats


Problem Description

There is a row of seats represented by string A. Assume that it contains N seats adjacent to each other. There is a group of people who are already seated in that row randomly. i.e. some are sitting together & some are scattered.

An occupied seat is marked with a character 'x' and an unoccupied seat is marked with a dot ('.')

Now your target is to make the whole group sit together i.e. next to each other, without having any vacant seat between them in such a way that the total number of hops or jumps to move them should be minimum.

In one jump a person can move to the adjacent seat (if available).

NOTE: 1. Return your answer modulo 107 + 3.



Problem Constraints

1 <= N <= 1000000
A[i] = 'x' or '.'


Input Format

First and only argument is a string A of size N.


Output Format

Return an integer denoting the minimum number of jumps required.


Example Input

Input 1:

 A = "....x..xx...x.."

Input 2:

 A = "....xxx"



Example Output

Output 1:

 5

Output 2:

 0



Example Explanation

Explanation 1:

 Here is the row having 15 seats represented by the String (0, 1, 2, 3, ......... , 14) 
                 . . . . x . . x x . . . x . . 
 Now to make them sit together one of approaches is -
                 . . . . . . x x x x . . . . .
 Steps To achieve this:
 1) Move the person sitting at 4th index to 6th index: Number of jumps by him =   (6 - 4) = 2
 2) Bring the person sitting at 12th index to 9th index: Number of jumps by him = (12 - 9) = 3
 So, total number of jumps made: 2 + 3 = 5 which is the minimum possible.

 If we other ways to make them sit together but the number of jumps will exceed 5 and that will not be minimum.
 

Explanation 2:

 They are already together. So, the cost is zero.
"""
"""
Hint 1

Hint : Is it possible to use the median position somehow ?

Are you getting “Wrong Answer” on time complexity check ? Did you miss taking mod from MOD = 10000003
"""
"""
Solution Approach

Lets take an exmaple:

string :  .x..x..x.
positions where x are present {1, 4, 7}
Median is 4. So we will move all x near our median. 1st person would need to jump 2 steps and 3rd person would also need to jump 2 steps. Total answer = 4. 

Can you prove why this approach works ?

Happy Coding
"""
class Solution:
	# @param A : string
	# @return an integer
	def seats(self, A):        
        MOD = 10000003
        seat = []
        
        for i in range(len(A)):
            if A[i] == "x":
                seat.append(i)
        if len(seat) == 0:
            return 0
        mid = len(seat)//2
        median = seat[mid] if len(seat)%2 == 1 else (seat[mid] + seat[mid-1])//2 
        empty = median if A[median] == "." else median - 1
        
        # print(seat,mid, median)
        hops = 0
        
        for i in range(median,-1,-1):
            if A[i] == "x" and empty > i:
                temp = empty - i 
                hops += temp 
                hops %= MOD
                empty -= 1 

        empty = median+1
        
        for j in range(median+1, len(A)):
            
            if A[j] == "x":
                temp = j-empty
                hops += temp
                hops %= MOD
                empty += 1 
                
        return hops