"""Day of the week

Given three integers A, B and C, find and return the day of the week for the given date A/B/C where A represents the date, B represents the month and C represents the year. Assume that Jan 1st 1 AD is a Monday in Gregorian calendar. February has 28 days(excluding leap years when it has 29 days). Leap year is a year that is either (divisible by 400) or (divisible by 4 and not divisible by 100).


Input Format

The 3 arguments given are the integers A, B and C.

Output Format

Return the day of the year as a string of lower case english alphabets.
Answer will be one of the following {sunday, monday, tuesday, wednesday, thursday, friday, saturday}.

Constraints

1 <= A <= 31
1 <= B <= 12
1990 <= C <= 2100

For Example

Input 1:
    A = 19
    B = 4
    C = 2019
Output 1:
    friday

Input 2:
    A = 7
    B = 10
    C = 1996
Output 2:
    monday
"""
# @param A : integer
# @param B : integer
# @param C : integer
# @return a strings
    
def solve(A, B, C):

    def isLeap(year):
        if year%4 == 0:
            if (year%100==0 and year%400==0) or year%100 != 0:
                return True
                
        return False
        
    arr = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    m = [0,3,3,6,1,4,6,2,5,0,3,5]
    y = C-1
    days = y + y//4 - y//100 + y//400 + m[B-1] + A
    
    if isLeap(C) and B>2:
        days += 1
    # print(days)
    return arr[days%7]