"""
Maximum Frequency stack

Problem Description

You are given a matrix A which represent operations of size N x 2. Assume initially you have a stack-like data structure you have to perform operations on it.

Operations are of two types:

1 x: push an integer x onto the stack and return -1

2 0: remove and return the most frequent element in the stack.

If there is a tie for the most frequent element, the element closest to the top of the stack is removed and returned.

A[i][0] describes the type of operation to be performed. A[i][1] describe the element x or 0 corresponding to the operation performed.


**Problem Constraints**

1 <= N <= 100000

1 <= A[i][0] <= 2

0 <= A[i][1] <= 109


**Input Format**

The only argument given is the integer array A.


**Output Format**

Return the array of integers denoting answer to each operation.


**Example Input**

Input 1:

A = [
            [1, 5]
            [1, 7]
            [1, 5]
            [1, 7]
            [1, 4]
            [1, 5]
            [2, 0]
            [2, 0]
            [2, 0]
            [2, 0]  ]

Input 2:

 A =  [   
        [1, 5]
        [2 0]
        [1 4]   ]



**Example Output**

Output 1:

 [-1, -1, -1, -1, -1, -1, 5, 7, 5, 4]

Output 2:

 [-1, 5, -1]



**Example Explanation**

Explanation 1:

 Just simulate given operations

Explanation 2:

 Just simulate given operations
"""
"""
Hint 1
Can you maintain a number of stacks to retrieve the
required information to get the answer??
"""
"""
Solution Approach

ushing into a stack looks like:
void push(int x)
{
freq[x]++;
if(freq[x] > max_freq) max_freq = freq[x];

if(stacks.count(freq[x]))
{
    stacks[freq[x]].push(x);    
}
else
{
    stack<int> st;
    st.push(x);
    stacks[freq[x]] = st;
} } This helps in maintaining the required answer and getting the answer to each of the  parts that need to be done such as oush and pop of the elements
"""
# @param A : list of list of integers
# @return a list of integers

    
def solve( A):
    from collections import OrderedDict
    ans = []
    stk = OrderedDict()
    count = {}
    
    def poper(stk, count):
        max_value = len(stk)
        
        temp_num = stk[max_value].pop()
        
        if len( stk[max_value] ) == 0:
            del stk[max_value]
            
        count[temp_num] -= 1
        
        return temp_num

        
    for i in A:
        if i[0] == 1:
            ans.append(-1)
            num = i[1]
            
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            
            if count[num] in stk:
                stk[count[num]].append(num)
            else:
                stk[ count[num]  ] = [num]   # problem is here
        elif i[0] == 2:
            
            ans.append( poper(stk, count) )
            
    

    return ans
