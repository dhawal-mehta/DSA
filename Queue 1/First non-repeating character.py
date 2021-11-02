"""
First non-repeating character


Problem Description

Given a string A denoting a stream of lowercase alphabets.

You have to make new string B. B is formed such that we have to find first non-repeating character each time a character is inserted to the stream and append it at the end to B. if no non-repeating character is found then append '#' at the end of B.



Problem Constraints

1 <= |A| <= 100000


Input Format

The only argument given is string A.


Output Format

Return a string B after processing the stream of lowercase alphabets A.


Example Input

Input 1:

 A = "abadbc"

Input 2:

 A = "abcabc"



Example Output

Output 1:

"aabbdd"

Output 2:

"aaabc#"



Example Explanation

Explanation 1:

"a"      -   first non repeating character 'a'
"ab"     -   first non repeating character 'a'
"aba"    -   first non repeating character 'b'
"abad"   -   first non repeating character 'b'
"abadb"  -   first non repeating character 'd'
"abadbc" -   first non repeating character 'd'

Explanation 2:

"a"      -   first non repeating character 'a'
"ab"     -   first non repeating character 'a'
"abc"    -   first non repeating character 'a'
"abca"   -   first non repeating character 'b'
"abcab"  -   first non repeating character 'c'
"abcabc" -   no non repeating character so '#'
"""
"""
Hint 1

Think of how you can maintain information for this stream
to get required answer.
"""
"""
Solution Approach

You need to maintain map for each character of the stream.
After that you can also maintain a queue for extraction of information.
Each character is inserted and removed from queue atmost 1 time
hence time complexity is O(n).
Code looks something like
for (auto c : A)
{
    mp[c]++;
    q.push(c);
    while (!q.empty() && mp[q.front()] > 1) 
        q.pop();

    if (!q.empty()) 
        ans.push_back(q.front());
    else 
        ans.push_back(‘#’);
}
"""
def solve(self, A):
    # s = {}
    # stk = []
    # ans = ""
    # for i in A:

    #     if len(stk)==0:
    #         stk.append(i)
    #         s[i] = 1
    #     else:
    #         if i in s:
    #             s[i] -= 1
    #         else:
    #             s[i] = 1
    #             stk.append(i)
                
    #     if s[ stk[0] ] != 1:
    #         while stk and s[stk[0]] != 1:
    #             stk.pop(0)
        
    #     if stk:
    #         ans += stk[0]
    
    #     else:
    #         ans += "#"
        
    
    # return ans
    
    from collections import deque
    s = {}
    
    q = deque()
    ans = ""
    for i in A:
        q.append(i)
        if i in s:
            s[i] += 1
        else:
            s[i] = 1
            
        while len(q) > 0 :
            if s[q[0]] == 1:
                ans += q[0]
                break
            else:
                q.popleft()
        
        if len(q) == 0 and i in s:
            ans += '#'


    return ans