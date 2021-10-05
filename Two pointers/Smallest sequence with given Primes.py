"""Smallest sequence with given Primes


Problem Description

Given three prime number(A, B, C) and an integer D. Find the first(smallest) D integers which have only A, B, C or a combination of them as their prime factors.


Problem Constraints

1 <= A, B, C <= 10000

1 <= D <= 100000



Input Format

First argument is an integer A.
Second argument is an integer B.
Third argument is an integer C.
Fourth argument is an integer D.


Output Format

Return an integer array of size D, denoting the first D integers described above.

NOTE: The sequence should be sorted in ascending order



Example Input

Input 1:

 A = 2
 B = 3
 C = 5
 D = 5

Input 2:

 A = 3
 B = 2
 C = 7
 D = 3



Example Output

Output 1:

 [2, 3, 4, 5, 6]

Output 2:

 [2, 3, 4]



Example Explanation

Explanation 1:

 4 = A * A ( 2 * 2 ), 6 = A * B ( 2 * 3 )

Explanation 2:

 2 has only prime factor 2. Similary 3 has only prime factor 3. 4 = A * A ( 2 * 2 )
 """
"""
Hint 1
Naive solution : We are interested in only those numbers whose prime factorization contains no other prime number other than p1, p2 and p3. So we can simply iterate all numbers and can check their prime factorization.

Better solution : Can we incrementally construct new numbers starting from the lowest prime p1 ? Would this become similar to Breadth first search / Dijkstra ?
"""
"""
Solution Approach

The naive solution will be to check prime factorization of every natural number incrementally till k numbers are found. However, that will be too slow.

As mentioned in the previous hint, this problem can be addressed as a modified BFS / Dijkstra. We push p1, p2 and p3 to a min heap.
Every time, we repeat the following process till we find k numbers :

 - M = Pop out the min element in the min heap. 
 - Add M to the final answer. 
 - Push M * p1, M * p2, M * p3 to the min heap if they are not already present in the heap ( We can use a hash map to track this ) 

However, this is O( k * log k ).
Can we do better than this ?

It turns out we can.
We use the fact that there are only 3 possibilities of getting to a new number : Multiply by p1 or p2 or p3.

For each of p1, p2 and p3, we maintain the minimum number in our set which has not been multiplied with the corresponding prime number yet.
So, at a time we will have 3 numbers to compare.
The corresponding approach would look something like the following :


initialSet = [p1, p2, p3] 
indexInFinalSet = [0, 0, 0]

for i = 1 to k 
  M = get min from initialSet. 
  add M to the finalAnswer if last element in finalAnswer != M
  if M corresponds to p1 ( or in other words M = initialSet[0] )
    initialSet[0] = finalAnswer[indexInFinalSet[0]] * p1
    indexInFinalSet[0] += 1
  else if M corresponds to p2 ( or in other words M = initialSet[1] )
    initialSet[1] = finalAnswer[indexInFinalSet[1]] * p1
    indexInFinalSet[1] += 1
  else 
    # Similar steps for p3. 
end
"""
# @param A : integer
# @param B : integer
# @param C : integer
# @param D : integer
# @return a list of integers
def solve(self, A, B, C, D):
    p1  = 0
    p2 = 0
    p3 = 0
    arr = [1]
    curr = 0
    while curr < D:
        num1 = arr[p1]*A
        num2 = arr[p2]*B
        num3 = arr[p3]*C
        temp = min(num1, num2, num3)
        if temp != arr[-1]:
            arr.append(temp)
            
            curr += 1
            
        if temp == num1:
            p1 += 1
        
        elif temp == num2:
            p2 += 1            
        
        else:
            p3 += 1
    
    return arr[1:]