"""
Given a number line from 0 to n and a string denoting a sequence of moves, determine the number of subsequences of those moves that lead from a given point x to end at another point y. Moves will be given as a sequence of l and r instructions. An instruction l = left movement, so from position j the new position is j - 1, and an instruction r = right movement, so from position j the new position would be j + 1.

For example, given a number line from 0 to 6, and a sequence of moves rrlrlr, the number of subsequences that lead from 1 to 4 on the number line is 3, as shown below.

Question image https://drive.google.com/file/d/1JzOP14wkmgIVaAYgJivZH0aE2i4FqMHB/view

"""
"""
Hint
This problem can be solved with the following recurrence: Let dp[i][j] be the number of ways to use the first i letters of s to end up at position j.

    Base case: dp[0][x] = 1. All else is 0.
    Recurrence: Set dp[i][j] = dp[i-1][j] (corresponds to don't use current character). Then, if s[i] (1-indexed) is l, add dp[i-1][j+1] (assuming j+1 <= n). Otherwise, add dp[i-1][j-1] (assuming j-1 >= 0).
    Answer: The answer is dp[s.length][y].

EDIT: accounting for distinctness. See https://leetcode.com/problems/distinct-subsequences-ii/ for this technique of removing duplicates.
"""

static int MOD = 1000000007;
public static int solve(char[] s, int n, int x, int y) {
    int[] prevSame = new int[s.length];
    int idxL = -1;
    int idxR = -1;
    for (int i = 0; i < prevSame.length; i++) {
        if (s[i] == 'l') {
            prevSame[i] = idxL;
            idxL = i;
        } else {
            prevSame[i] = idxR;
            idxR = i;
        }
    }

    // dp[i][j] is number of distinct subsequnces of length i to end up at j
    long[][] dp = new long[s.length+1][n+1];
    dp[0][x] = 1;
    for (int i = 1; i <= s.length; i++) {
        for (int j = 0; j <= n; j++) {
            dp[i][j] = dp[i-1][j];
            if (s[i-1] == 'l') {
                if (j+1 <= n) dp[i][j] += dp[i-1][j+1];
                if (j+1 <= n && prevSame[i-1] >= 0) dp[i][j] -= dp[prevSame[i-1]+1-1][j+1];
            } else {
                if (j-1 >= 0) dp[i][j] += dp[i-1][j-1];
                if (j-1 >= 0 && prevSame[i-1] >= 0) dp[i][j] -= dp[prevSame[i-1]+1-1][j-1];
            }
            dp[i][j] = (dp[i][j] + MOD) % MOD;
        }
    }
    return (int) dp[s.length][y];
}
