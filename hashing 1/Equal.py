"""
Equal


Problem Description

Given an array A of N integers, find the index of values that satisfy P + Q = R + S, where P,Q,R & S are integers values in the array

Expected time complexity O(N2)

NOTE:



1) Return the indices A1 B1 C1 D1, so that A[A1] + A[B1] = A[C1] + A[D1] A1 < B1, C1 < D1 A1 < C1, B1 != D1, B1 != C1


2) If there are more than one solutions, then return the tuple of values which are lexicographical smallest.


Assume we have two solutions S1 : A1 B1 C1 D1 ( these are values of indices in the array )
S2 : A2 B2 C2 D2


S1 is lexicographically smaller than S2 if: A1 < A2 OR A1 = A2 AND B1 < B2 OR A1 = A2 AND B1 = B2 AND C1 < C2 OR A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2

If no solution is possible, return an empty list.



**Problem Constraints**

1 <= N <= 1000

0 <= A[i] <= 1000



**Input Format**

Single argument which is an integer array A of size N.


**Output Format**

Return an array of size 4 which indexes of values P,Q,R and S.


**Example Input**

Input 1:

 A = [3, 4, 7, 1, 2, 9, 8]

Input 2:

 A = [2, 5, 1, 6]



**Example Output**

Output 1:

 [0, 2, 3, 5]

Output 2:

 [0, 1, 2, 3]



**Example Explanation**

Explanation 1:

 A[0] + A[2] = A[3] + A[5]
 Note: indexes returned should be 0-based.

Explanation 2:

 A[0] + A[1] = A[2] + A[3]"""

"""
Hint 1

Brute Force:

Loop i = 1 to N :
  Loop J = I+1 to N :
    Loop K = J+1 to N:
        Loop L = K+1 to N:
               if condition is true then update ans
         endLoop;
     endLoop;
   endLoop;
endLoop;

But this solution is too slow.
Can we optimize somehow ? Use hashing perhaps ?
"""
"""
Hint 2
Continuing from the first hint,

Hashing can provide one more level of optimization.

Lets look at our bruteforce solution once more :

Loop I = 1 to N :
  Loop J = I+1 to N :
    Loop K = J+1 to N:
        Loop L = K+1 to N:
               if condition is true then update ans
         endLoop;
     endLoop;
   endLoop;
endLoop;

Do we need a loop for L if we have hashed out the values ?

We know that A[I] + A[J] = A[K] + A[L].
If we know, I, J and K, then we can determine what A[L] should be.
We can lookup the value A[L] = A[I] + A[J] - A[K] in a hashmap.

The solution then becomes O(N^3) instead of O(N^4).
Do note that we need to take care of duplicate values here.

However, this might be a little slow as well. We are looking for something better.
Can we use more space to optimize the solution ? How about hashing pairwise sums ( A[i] + A[J], A[K] + A[L] ) ?
"""
"""
Solution Approach



Loop i = 1 to N :
    Loop j = i + 1 to N :
        calculate sum
        If in hash table any index already exist for sum then 
            try to find out that it is valid solution or not IF Yes Then update solution
        update hash table
    EndLoop;
EndLoop;


Now can you implement it??
Happy Coding
"""
# @param A : list of integers
# @return a list of integers
def equal(self, A):
    
    sum_ = {}
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            temp = A[i] + A[j]
            
            if temp in sum_:
                prev = sum_[temp][-1]
                if prev[0] != i and prev[0] != j and prev[1] != i and prev[1] != j:
                    sum_[temp].append([i,j])
                
            else:
                sum_[ temp ] = [[i,j]]
    

    curr_num = [10**9]*4
    flag = 0
    for i in sum_:
        # print(i)
        if len( sum_[i] ) > 1:
            arr = sum_[i]
            
            if ((arr[0][0] < curr_num[0]) or
                (arr[0][0] == curr_num[0] and arr[0][1] < curr_num[1]) or
                (arr[0][0] == curr_num[0] and arr[0][1] == curr_num[1] and arr[1][0] < curr_num[2]) or
                (arr[0][0] == curr_num[0] and arr[0][1] == curr_num[1] and arr[1][0] == curr_num[2] and arr[1][1] < curr_num[3]) ): 
                
                curr_num = [ arr[0][0], arr[0][1], arr[1][0], arr[1][1] ]
                flag = 1
                    
        
    if flag == 0:
        return []
    else:
        return curr_num
