"""
Gcd Ordering

Given an array of integers A, find and return the lexicographically greatest arrangement of A
which follows the below rules:

    If the size of A is less than 3 it is always possible to rearrange A.

    A[i] = A[i-1] + GCD(A[i-1], A[i-2]) for all i > 2, where GCD(x, y) is
    greatest common factor of x and y.

Return the lexicographically greatest arrangement of A which follows the above rules,
if it is not possible to rearrange A according to the above rules return -1.

Note: Lexicographically means in dictionary order, i.e. if two arrangemnets are compared based
on dictionary position the arrangements which comes afterwards is said to be Lexicographically greater.



Input Format

The only argument given is the integer array A.

Output Format

Return the lexicographically greatest arrangement of A  which follows the above rules, 
if it is not possible to rearrange A according to the given rules return -1.

Constraints

1 <= length of the array <= 100000
0 <= A[i] <= 10^5

For Example

Input 1:
    A = [4, 6, 2, 5, 3]
Output 1:
     [2, 3, 4, 5, 6]

Input 2:
    A = [3, 8, 5]
Output 2:
    -1

"""
"""
Hint 1
You would have guessed of a solution that would involve sorting of the array and then checking if the gcd condition holds. You are partly right, the numbers have to be in increasing sequence but except for one case where there could be a number that could appear at the start of the permutation. For Example, in 2 4 6 8 8, you could have had 8 at the starting and have got the permutation 8 2 4 6 8. There were many corner cases to this
Check for the corner cases.

Few other things to note were -
1) you couldn’t have more than two elements whose freq was more than 1.
2) if you had two zeros in the array, the only possible permutation possible was all 0’s
3) you had to use gcd of(0,x) = x wisely.

Time Complexity - nlogn
"""
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def merge(self, A, start, mid, end):
        # print(start, mid, end)
        temp= []
        # print(temp1, temp2)
        ptr1 = start
        ptr2 = mid+1


        while ptr1 <= mid and ptr2<=end:
            
            if A[ptr1] <= A[ptr2]:
                temp.append(A[ptr1])
                ptr1 +=1
            else:
                temp.append( A[ptr2] )
                ptr2 += 1
        
        
        while ptr1 <= mid:
            temp.append(A[ptr1])
            ptr1+=1
            
        while ptr2<=end:
            temp.append(A[ptr2])
            ptr2+=1
        
        A[start:end+1] = temp
        
            
    def mergeSort(self, A, start, end):
        # print(start,end)
        if start >= end:
            return
        
        mid = start + (end-start)//2
        
        self.mergeSort(A,start, mid)
        self.mergeSort(A, mid+1, end)
        self.merge(A, start, mid, end)
    
    def GCD(self, a, b):
        if b==0:
            return a
        if a%b == 0:
            return b
        
        return self.GCD(b, a%b)
    
    def solve(self, A):
        if len(A) <= 1:
            return A
        if len(A) == 2:
            return [max(A[0], A[1]), min(A[1], A[0])]
            
        self.mergeSort(A,0,len(A)-1)
        
        
        if len(A) >=2 and A[0] == A[1] and A[1] == 0:
            for i in range(2, len(A)):
                if A[i] != 0:
                    return -1

       
        
        flag = 0
        for i in range(2,len(A)):
            # print(A[i], A[i-1], A[i-1] + self.GCD(A[i-1], A[i-2]) )
            
            if A[i] == A[i-1] + self.GCD( A[i-1], A[i-2] ):
                continue
            
            else:
                if flag == 1:
                    return [-1]
                else:
                    if A[1] == A[0] + self.GCD(A[i], A[0]):
                        flag = 1
                        
                        for j in range(i,0,-1):
                            A[j]=A[j-1]
                        
                        A[0]=A[i]
                
                
        return A