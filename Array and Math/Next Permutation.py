"""Next Permutation

Problem Description

Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers for a given array A of size N.

If such arrangement is not possible, it must be rearranged as the lowest possible order i.e., sorted in an ascending order.

NOTE:

The replacement must be in-place, do not allocate extra memory.
DO NOT USE LIBRARY FUNCTION FOR NEXT PERMUTATION. Use of Library functions will disqualify your submission retroactively and will give you penalty points.


Problem Constraints

1 <= N <= 5 * 105

1 <= A[i] <= 109



Input Format

The first and the only argument of input has an array of integers, A.


Output Format

Return an array of integers, representing the next permutation of the given array.


Example Input

Input 1:

 A = [1, 2, 3]

Input 2:

 A = [3, 2, 1]



Example Output

Output 1:

 [1, 3, 2]

Output 2:

 [1, 2, 3]



Example Explanation

Explanation 1:

 Next permutaion of [1, 2, 3] will be [1, 3, 2].

Explanation 2:

 No arrangement is possible such that the number are arranged into the numerically next greater permutation of numbers.
 So will rearranges it in the lowest possible order.
 """

"""
Hint 1
You can try out few test cases to see what the pattern is or what exactly is the flow of numbers from initial sequence to final sequence.

""" 
"""
Solution Approach
It might help to write down the next permutation on paper to see how and when the sequence changes.

You’ll realize the following pattern :

The suffix which gets affected is in a descending order before the change.

A swap with the smaller element happens and then we reverse the affected suffix.

    1 2 3 -> 1 3 2   // Suffix being just the 3. 

    1 2 3 6 5 4  -> 1 2 4 3 5 6 // Suffix being 6 5 4 in this case. 

"""
""" accepted solution """
def swapSort(A,i):

    num = A[i-1]
    minPos = i
    
    for j in range(i+1,len(A)):
        if A[j] >= num:
            minPos+=1
        else:
            break
    
    A[i-1],A[minPos] = A[minPos], A[i-1]
    A[i:len(A)] = sorted(A[i:len(A)])
            
            
    
def nextPermutation( A):
    flag = 0
    for  i in range(len(A)-1,0,-1):
            if A[i] > A[i-1]:
                swapSort(A, i)
                flag = 1
                break

    if flag == 0:
        A = A[::-1]

    return A
