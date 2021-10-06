"""
Distribute Candy

Problem Description

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.

What is the minimum candies you must give?



Problem Constraints

1 <= N <= 105
-109 <= A[i] <= 109


Input Format

First and only argument is an integer array A representing the rating of children.


Output Format

Return an integer, representing the minimum candies to be given.


Example Input

Input 1:

 A = [1, 2]

Input 2:

 A = [1, 5, 2, 1]



Example Output

Output 1:

 3

Output 2:

 7



Example Explanation

Explanation 1:

 The candidate with 1 rating gets 1 candy and candidate with rating 2 cannot get 1 candy as 1 is its neighbor. 
 So rating 2 candidate gets 2 candies. In total, 2 + 1 = 3 candies need to be given out.

Explanation 2:

 Candies given = [1, 3, 2, 1]
"""
"""
Hint 1

Would greedily assigning the candy work here ?
Where should you start from ?

Should you start assigning the candies from the least rating guy to the guy with most rating or vice versa ?
"""
"""
Solution Approach

Greedy works here ( Think of a supportive proof as as assignment ).

Start with the guy with the least rating. Obviously he will receive 1 candy.

If he did recieve more than one candy, we could lower it to 1 as none of the neighbor have higher rating.
Now lets move to the one which is second least. If the least element is its neighbor, then it receives 2 candies, else we can get away with assigning it just one candy.

We keep repeating the same process to arrive at optimal solution.
"""
# @param A : list of integers
# @return an integer
def candy(A):
    if len(A) ==1:
        return 1
        
    candy = [1]

    for i in range(1, len(A)):
        if A[i] > A[i-1]:
            candy.append(candy[i-1]+1)
        else:
            candy.append(1)
    
    for i in range(len(A)-2, -1, -1):
        if A[i] > A[i+1] and candy[i] <= candy[i+1]:
            candy[i] += candy[i+1] - candy[i] + 1
    
    return sum(candy)


