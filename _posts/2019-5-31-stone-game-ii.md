---
title:  "877. Stone Game"
date:   2019-05-31 21:38:00 +0930
categories: Leetcode
tags: Medium DynamicProgramming Backtrack
---

[{{page.title}}](https://leetcode.com/problems/stone-game-ii/){:target="_blank"}

    Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and
    each pile has a positive integer number of stones piles[i].

    The objective of the game is to end with the most stones.  The total number of stones is odd, so there are
    no ties.

    Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones
    from either the beginning or the end of the row.  This continues until there are no more piles left, at
    which point the person with the most stones wins.

    Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

    Example 1:

    Input: [5,3,4,5]
    Output: true
    Explanation:
    Alex starts first, and can only take the first 5 or the last 5.
    Say he takes the first 5, so that the row becomes [3, 4, 5].
    If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
    If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
    This demonstrated that taking the first 5 was a winning move for Alex, so we return true.

    Note:

        2 <= piles.length <= 500
        piles.length is even.
        1 <= piles[i] <= 500
        sum(piles) is odd.


* dp top down
  - total sum minus the amount that the other person has to take when following the optimal rule
  - the # the other person can take changes when the current person takes differnt # of piles
  - for loop try all possibilities, and find a min value
  - the result is Total sum - min value
```java

class Solution {
    int[][] dp;
    int[] suffix;
    public int stoneGameII(int[] piles) {
        dp = new int[piles.length][32];
        suffix = new int[piles.length];
        suffix[suffix.length-1] = piles[suffix.length-1];
        for(int i = suffix.length-2; i >= 0; i--)
            suffix[i] = piles[i] + suffix[i+1];
        return backtrack(piles, 1, 0);
    }

    public int backtrack(int[] piles, int m, int j) {
        if(piles.length-j <= 2 * m) return suffix[j]; // take all
        if(dp[j][m] != 0) return dp[j][m]; // cached
        int result = Integer.MAX_VALUE;
        for(int x = 1; x <= 2 * m && x+j-1 < piles.length; x++)
            result = Math.min(result, backtrack(piles, Math.max(x,m), j+x));
        dp[j][m] = suffix[j] - result; // total sum of [j:] subtract the min value the other
                                       // person must take when following the optimal rule
        return dp[j][m];
    }
  }
```
