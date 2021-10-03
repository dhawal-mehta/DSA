"""
Size three subsequences divisible by B


Given an array of integers A and an integer B.
Find and return the number of subsequences of length 3 whose sum is divisible by B.

Since the total number of subsequences may be very large.

Return the total number of subsequences of length 3 whose sum is divisible by B modulo (109+7).



Input Format

The only argument given is the integer array A.

Output Format

Return the number of subsequences of length 3 whose sum is divisible by B modulo (10^9+7). 

Constraints

1 <= length of the array <= 100000
1 <= A[i] <= 10^9 
1 <= B <= 10^3

For Example

Input 1:
    A = [6, 1, 1, 4, 1, 5, 3]
    B = 2
Output 1:
    20

Input 2:
    A = [4, 10, 9]
    B = 5
Output 2:
    0
                                                         
"""
"""
Hint 1

Store each value modulo M in a frequency array.

We use a frequency array to store the number of occurrence of each elements using index mapping techniques.

Now look for the cases.

"""
"""
Solution Approach

Three cases may occur:

1.Thrice of a number is divisible by B then we will add ncr(N,3) to answer where N is frequency of that number.

2.Twice of some number A added with sum number B is divisible by B
then we will add ncr(Freq[A],2) * Freq[B] to the answer.

3.If all the number A, B, C(A,B,C are pairwise disticnt)
that sum up to S which is divisible by B then we will add Freq[A] * Freq[B] * Freq[C] to the answer.

Time Complexity : O(B^2)

"""
def solve( A, B):
    freq = {}
    
    for i in A:
        mod = i%B
        if mod in freq:
            freq[mod] += 1
        else:
            freq[mod] = 1
        
    ans = 0
    for i in freq:
        for j in freq:
            
            k = (B-i-j)%B
            if  k>=j and j >= i and k in freq :
                
                if i==j and j==k:
                    ans = ans + ( freq[i] * (freq[i] - 1) * (freq[i] - 2)) // 6
                elif i==j :
                    ans = ans + ((freq[i] * (freq[i] - 1))//2) * freq[k]
                elif i==k:
                    ans = ans + ((freq[i] * (freq[i] - 1))//2) * freq[j]
                elif j==k:
                    ans = ans + ((freq[j] * (freq[j] - 1))//2) * freq[i]
                else:
                    ans = ans + freq[i] * freq[j] * freq[k]
                
                ans = ans%(1000000007)
    return ans