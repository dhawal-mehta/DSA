"""
Largest Rectangle in Histogram


Problem Description

Given an array of integers A .

A represents a histogram i.e A[i] denotes height of the ith histogram's bar. Width of each bar is 1.

Find the area of the largest rectangle formed by the histogram.



Problem Constraints

1 <= |A| <= 100000

1 <= A[i] <= 1000000000



Input Format

The only argument given is the integer array A.


Output Format

Return the area of largest rectangle in the histogram.


Example Input

Input 1:

 A = [2, 1, 5, 6, 2, 3]

Input 2:

 A = [2]



Example Output

Output 1:

 10

Output 2:

 2



Example Explanation

Explanation 1:

The largest rectangle has area = 10 unit. Formed by A[3] to A[4].

Explanation 2:

Largest rectangle has area 2.
"""
"""
Hint 1
Whats the brute force approach here?

We know that the height of the largest rectange will be one of the heights of the histogram bars (Think about why?)
If that is the case, we can iterate on all the histogram bars, and for each histogram bar H, we try to create the maximum rectange with H as the height.
To do that, we keep going left L and right R till we encounter a histogram bar with height less than H.
Now, (R - L - 1) * H is one of the possibilities for the largest rectangle.

Doing this for all the histogram bars will give us the right solution.

Following is a rough pseudocode for the approach mentioned above :


max_rectangle = 0 

for index = 0 to all_histograms.length
  H = all_histograms[index]
  L = index, R = index
  while L >= 0 AND all_histograms[L] >= H
    L = L - 1
  while R < all_histograms.length AND all_histograms[R] >= H
    R = R + 1
  max_rectangle = MAX(max_rectangle, (R - L - 1) * H)

return max_rectangle


This approach is however O(N^2) time complexity in the worst case. How can we do better than this approach?

Hint : Think in terms of using a stack ?
"""
"""
Hint 2
As discussed in the previous hint, height of the maximum rectangle will be height of one of the histogram bars. For each histogram H, we need to know index of the first smaller (smaller than H) bar on left of H (lets call it L) and index of first smaller bar on right of H.
We already tried the brute force approach. How can we do better?

Important observation:

Lets consider 2 consecutive histogram bars H[i] and H[i+1]. Lets assume H[i+1] < H[i]
In such a case, for all histogram bars X with index > i + 1 when traversing left for L, there is no point looking at H[i] after looking at H[i+1]. If H[i+1] > X, obviously H[i] > X as we already know H[i] > H[i+1]

Then, whats the next entry we would want to look at? We would want to look at the first histogram bar left of H[i+1] with height less than H[i+1].

Can you think of a stack based approach based on the above observation?
"""
"""
Solution Approach

From our previous observation, we already know that when I traverse left, I only need entries in decreasing order.

We traverse all histograms from left to right, maintain a stack of histograms. Every histogram is pushed to stack once. A histogram is popped from stack when a histogram of smaller height is seen. When a histogram is popped, we calculate the area with the popped histogram as smallest histogram. How do we get left and right indexes of the popped histogram – the current index tells us the ‘right index’ R and index of previous item in stack is the ‘left index’ L. Following is a rough pseudocode.

max_rectangle = 0
stack = an instance of empty stack
for index = 0 to all_histograms.length
    if stack.empty OR H[index] > H[stack.top]
        Push index to the stack
    if H[index] < H[stack.top]
        while !stack.empty && H[stack.top] > H[index]
            h = H[stack.pop]
            # Calculate the area with h as the smallest height. 
            R = index
            L = stack.top
            max_rectangle = MAX(max_rectangle, (R - L - 1) * h)
        Push index to the stack
if stack is not empty
    Repeat the process of removing entries one by one from stack and calculating the max_rectangle as done earlier.     
     
"""
# @param A : list of integers
# @return an integer
def largestRectangleArea(A):
    stk = []
    index = 0
    max_area = 0
    while index < len(A):
        if not stk or A[stk[-1]] <= A[index]:
            
            stk.append(index)
            index += 1
            # print(stk)
        
        else:
            temp = stk.pop()
            area = A[temp]*( index -stk[-1] -1 if stk else index)
            # print(area)
            max_area = max(area, max_area)
    
    while stk:
        temp = stk.pop()
        area = A[temp]*( index -stk[-1] -1 if stk else index)
        max_area = max(area, max_area)
    
    return max_area 