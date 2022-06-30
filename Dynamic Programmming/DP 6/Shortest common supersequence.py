"""Shortest common supersequence


Given two strings A and B, find the shortest string that has both A and B as subsequences.
If multiple answers exist, you may return any of them.

Note: A string S is a subsequence of string T if deleting some number of characters from T (possibly 0, and the characters are chosen anywhere from T) results in the string S.

Input Format:

First line contains a single integer T denoting the number of test cases.
T lines follow each containing two space separated strings A B

Output Format:

Print T lines each containing a single string.
Note: The string should only contain lower case english alphabets.

Constraints:

1 ≤ T ≤ 10000
1 ≤ |A|,|B| ≤ 1000
sum of |A| * |B| over all test cases does not exceed 10^7

For Example:

Input 1:
    2
    abcd bcde
    xyz abc
Output 1:
    abcde
    axbyzc
Explanation:
    string abcde has both abcd and bcde as subsequence and also has minimum length. For second test case you can also print abcxyz or any other string that follow all condition.
"""

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    def util(a,b):
        # print(a, b)
        dp = [ [ 0 for i in range(len(b) + 1) ] for j in range(len(a) + 1) ]
    
        for i in range(1, len(a)+1):
            for j in range(1, len(b)+1):
                if a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1] +1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        matchArr = []
        
        currx = len(a)
        curry = len(b)

        while currx > 0 and curry > 0:
            if a[currx-1] == b[curry-1]:
                matchArr.append( (currx-1, curry-1) )
                currx -= 1
                curry -= 1
                
            elif dp[currx-1][curry] >= dp[currx][curry-1]:
                currx -= 1
            else:
                curry -= 1
        
        if len(matchArr) == 0:
            return a+b
        
        
        matchArr = matchArr[::-1]
        res = ""

        curra = 0
        currb = 0
        temp = 0
        
        while curra < len(a) and currb < len(b) and temp < len(matchArr):
            # print(curra, currb, temp, res)
            # print(matchArr[temp])   
            
            for i in range(curra, matchArr[temp][0]):
                res += a[i]
            
            for i in range(currb , matchArr[temp][1]):
                res += b[i]
            
            # print(res)
            curra = matchArr[temp][0]
            currb = matchArr[temp][1]
            
            res += a[curra]
            
            curra += 1
            currb += 1
            temp += 1
        
        # print(res)
        
        while curra != len(a):
            res += a[curra]
            curra += 1

        while currb != len(b):
            res += b[currb]
            currb += 1

        return res
        
    for i in range(N):
        try: 
            inp = input()
            inpArr = inp.split(" ")
            if len(inpArr) == 1 :
                print(inpArr[0])
            elif  len(inpArr) == 0:
                print("")
            else:
                if len(inpArr[0]) >= len(inpArr[1]):
                    print(util(inpArr[1], inpArr[0]))
                else:
                    print(util(inpArr[0], inpArr[1]))
        except:
            continue
    return 0

if __name__ == '__main__':
    main()
    