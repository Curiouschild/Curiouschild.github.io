---
title:  "877. Stone Game"
date:   2019-05-31 19:48:00 +0930
categories: Leetcode
tags: Medium Knapsack DynamicProgramming
---

[{{page.title}}](https://leetcode.com/problems/stone-game/){:target="_blank"}

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


* expand window
  - dp[i][j] : the difference of substracting Lee's stone from Alex's in range [i,j].
  - dp[0][arr.length-1] is positive when Alex has more stone than Lee in the end.

```java

public boolean stoneGame(int[] nums) {
    int[][] dp = new int[nums.length][nums.length];
    int flag = (nums.length - 1) & 1; // Alex's turn
    int sum = 0;
    for(int i = 0; i < nums.length; i++) {
        sum += nums[i];
        dp[i][i] = -nums[i]; // Lee is always to pick the last stone because the # of arr is even
    }
    for(int w = 2; w <= nums.length; w++) {
        for(int i = 0; i+w <= nums.length; i++) {
            int j = i+w-1;
            if(((j-i) & 1) == flag) // Alex's turn
                dp[i][j] = Math.max(nums[i]+dp[i+1][j], nums[j]+dp[i][j-1]);
            else // Lee's turn
                dp[i][j] = Math.max(-nums[i]+dp[i+1][j], -nums[j]+dp[i][j-1]);
        }
    }
    return dp[0][nums.length-1] > 0;
}
```
