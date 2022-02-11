"""
Allocate Books


Problem Description

Given an array of integers A of size N and an integer B.

College library has N books,the ith book has A[i] number of pages.

You have to allocate books to B number of students so that maximum number of pages alloted to a student is minimum.

A book will be allocated to exactly one student.
Each student has to be allocated at least one book.
Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.

Calculate and return that minimum possible number.


NOTE: Return -1 if a valid assignment is not possible.



Problem Constraints

1 <= N <= 105
1 <= A[i], B <= 105


Input Format

The first argument given is the integer array A.
The second argument given is the integer B.


Output Format

Return that minimum possible number


Example Input

A = [12, 34, 67, 90]
B = 2



Example Output

113



Example Explanation

There are 2 number of students. Books can be distributed in following fashion : 
        1) [12] and [34, 67, 90]
        Max number of pages is allocated to student 2 with 34 + 67 + 90 = 191 pages
        2) [12, 34] and [67, 90]
        Max number of pages is allocated to student 2 with 67 + 90 = 157 pages 
        3) [12, 34, 67] and [90]
        Max number of pages is allocated to student 1 with 12 + 34 + 67 = 113 pages
        Of the 3 cases, Option 3 has the minimum pages = 113.
"""
"""
Hint 1

Try another assignment :

Can you find how many number of students we need if we fix that one student can read atmost V number of pages ?

"""
"""
Solution Approach

Here we will solve what has been discussed in the previous hint :

Problem statement : Given fixed number of pages (V),  how many number of students we need?
Solution :
   simple simulation approach
   intially Sum := 0
   cnt_of_student = 0
   iterate over all books:
        If Sum + number_of_pages_in_current_book > V :
                  increment cnt_of_student
                  update Sum
        Else:
                  update Sum
   EndLoop;
  


    fix range LOW, HIGH
    Loop until LOW < HIGH:
            find MID_point
            Is number of students required to keep max number of pages below MID < M ? 
            IF Yes:
                update HIGH
            Else
                update LOW
    EndLoop;

"""
# @param A : list of integers
# @param B : integer
# @return an integer
def possible(self, A, B, min_pages):
        
student_count = 1
sum_ = 0

for i in A:
        if i > min_pages :  # as then i'th book will not be able to allocate
        return False
        
        if sum_ + i > min_pages:
        sum_ = i
        student_count += 1
        if student_count > B:
                return False
        
        else:
        sum_ += i

return True
                

def books(self, A, B):

low = min(A) # min possible value
high = sum(A)  # max possible value
# for i in A:
#     high += i
        
ans = 10**9

if len(A) < B:
        return -1
        
while  high - low >= 0:
        mid = low + (high - low)//2
        
        if self.possible(A, B, mid):
        ans = min(ans, mid)
        high  = mid-1
        else:
        low = mid + 1

# print(ans,low)
return ans 

