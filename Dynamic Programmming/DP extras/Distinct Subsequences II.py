"""
Distinct Subsequences II


Given a string s, return the number of distinct non-empty subsequences of s. Since the answer may be very large, return it modulo 109 + 7.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not.

 

Example 1:

Input: s = "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".

Example 2:

Input: s = "aba"
Output: 6
Explanation: The 6 distinct subsequences are "a", "b", "ab", "aa", "ba", and "aba".

Example 3:

Input: s = "aaa"
Output: 3
Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".

 

Constraints:

    1 <= s.length <= 2000
    s consists of lowercase English letters.
"""

""" Hint
Intuition and Algorithm

Even though the final code for this problem is very short, it is not very intuitive to find the answer. In the solution below, we'll focus on finding all subsequences (including empty ones), and subtract the empty subsequence at the end.

Let's try for a dynamic programming solution. In order to not repeat work, our goal is to phrase the current problem in terms of the answer to previous problems. A typical idea will be to try to count the number of states dp[k] (distinct subsequences) that use letters S[0], S[1], ..., S[k].

Naively, for say, S = "abcx", we have dp[k] = dp[k-1] * 2. This is because for dp[2] which counts ("", "a", "b", "c", "ab", "ac", "bc", "abc"), dp[3] counts all of those, plus all of those with the x ending, like ("x", "ax", "bx", "cx", "abx", "acx", "bcx", "abcx"). Here's a visualization for this string.

However, for something like S = "abab", let's play around with it. We have:

    dp[0] = 2, as it counts ("", "a")
    dp[1] = 4, as it counts ("", "a", "b", "ab");
    dp[2] = 7 as it counts ("", "a", "b", "aa", "ab", "ba", "aba");
    dp[3] = 12, as it counts ("", "a", "b", "aa", "ab", "ba", "bb", "aab", "aba", "abb", "bab", "abab").

We have that dp[3]countsdp[2], plus("b", "aa", "ab", "ba", "aba")with"b"added to it. Notice that("", "a")are missing from this list, as they get double counted. In general, the sequences that resulted from putting"b"the last time (ie."b", "ab"`) will get double counted. Here's a visualization for a string with repeated letters.

This insight leads to the recurrence:

dp[k] = 2 * dp[k-1] - dp[last[S[k]] - 1]

The number of distinct subsequences ending at S[k], is twice the distinct subsequences counted by dp[k-1] (all of them, plus all of them with S[k] appended), minus the amount we double counted, which is dp[last[S[k]] - 1].
"""


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        t = [1]
        prev = {}
        for i in range(0, len(s)):
            t.append( 2*t[-1] )
            if s[i] in prev:
                t[i] -= t[ prev[s[i]] ] 
                
            prev[s[i]] = i
        
        return t[-1]%(10**9 +7)


