"""
Min Stack


Problem Description

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

NOTE:

    All the operations have to be constant time operations.
    getMin() should return -1 if the stack is empty.
    pop() should return nothing if the stack is empty.
    top() should return -1 if the stack is empty.



Problem Constraints

1 <= Number of Function calls <= 107


Input Format

Functions will be called by the checker code automatically.


Output Format

Each function should return the values as defined by the problem statement.


Example Input

Input 1:

push(1)
push(2)
push(-2)
getMin()
pop()
getMin()
top()

Input 2:

getMin()
pop()
top()



Example Output

Output 1:

 -2 1 2

Output 2:

 -1 -1



Example Explanation

Explanation 1:

Let the initial stack be : []
1) push(1) : [1]
2) push(2) : [1, 2]
3) push(-2) : [1, 2, -2]
4) getMin() : Returns -2 as the minimum element in the stack is -2.
5) pop() : Return -2 as -2 is the topmost element in the stack.
6) getMin() : Returns 1 as the minimum element in stack is 1.
7) top() : Return 2 as 2 is the topmost element in the stack.

Explanation 2:

Let the initial stack be : []
1) getMin() : Returns -1 as the stack is empty.
2) pop() :  Returns nothing as the stack is empty.
3) top() : Returns -1 as the stack is empty.
"""
"""
Hint 1
Lets look at solution number 1.

What if you maintained 2 queues. One which stored the actual stack of element, and the other which stored the minimum of elements.
So when pushing new element,
min = min(top of minimum stack, current value) which is pushed to minimum stack.

However, this uses 2N memory.

Can you think of slight optimizations to this ?
"""
"""
Solution Approach

What if you maintaned the current minimum in a variable and only stored the places where the minimum changes or the element is same as the minimum.

pop() becomes a little trickier in such a case.
You only pop() from the min stack if the top() of min stack is same as the current minimum.

Space complexity : O(N + X) where X = number of places where minimum changes or the element is same as the minimum
"""
class MinStack:
    stack = []
    minimums = []
    # @param x, an integer
    # @return an integer
    def push(self, x):
        if len(self.stack) == 0:
            self.stack.append(x)
            self.minimums.append(x)
        else:
            self.stack.append(x)
            if x < self.minimums[-1]:
                self.minimums.append(x)
            else:
                self.minimums.append(self.minimums[-1])

    # @return nothing
    def pop(self):
        if len(self.stack) != 0:
            self.stack.pop()
            self.minimums.pop()

    # @return an integer
    def top(self):
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack[-1]

    # @return an integer
    def getMin(self):
        if len(self.stack) == 0:
            return -1
        else:
            return self.minimums[-1]
    
    def __init__(self):
        self.stack = []
        self.minimums = []
