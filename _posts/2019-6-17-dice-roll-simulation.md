---
title:  "1223. Dice Roll Simulation"
date:   2019-06-17 14:54:00 +0930
categories: Leetcode
tags: Medium DynamicProgramming
---

[{{page.title}}](https://leetcode.com/problems/dice-roll-simulation/){:target="_blank"}

    A die simulator generates a random number from 1 to 6 for each roll. You introduced a constraint to the
    generator such that it cannot roll the number i more than rollMax[i] (1-indexed) consecutive times.

    Given an array of integers rollMax and an integer n, return the number of distinct sequences that can be
    obtained with exact n rolls.

    Two sequences are considered different if at least one element differs from each other. Since the answer
    may be too large, return it modulo 10^9 + 7.

    Example 1:

    Input: n = 2, rollMax = [1,1,2,2,2,3]
    Output: 34
    Explanation: There will be 2 rolls of die, if there are no constraints on the die, there are 6 * 6 = 36
    possible combinations. In this case, looking at rollMax array, the numbers 1 and 2 appear at most once
    consecutively, therefore sequences (1,1) and (2,2) cannot occur, so the final answer is 36-2 = 34.

    Example 2:

    Input: n = 2, rollMax = [1,1,1,1,1,1]
    Output: 30

    Example 3:

    Input: n = 3, rollMax = [1,1,1,2,2,3]
    Output: 181



    Constraints:

        1 <= n <= 5000
        rollMax.length == 6
        1 <= rollMax[i] <= 15

* DynamicProgramming
  - state:
    - n: n rolls remaining
    - index: the value of the last index of the rolled numbers
    - k: the number of consecutive index in the rolled numbers including the last one

```java

class Solution {
    int[][][] memo;
    int[] rollMax;
    int MOD = 1000000007;
    public int dieSimulator(int n, int[] rollMax) {
        this.memo = new int[n+1][7][16];
        this.rollMax = rollMax;
        int result = 0;
        for(int i = 0; i < 6; i++) {
            result += dfs(n-1, i, 1);
            result %= MOD;
        }
        return result % MOD;
    }

    public int dfs(int n, int index, int k) {
        if(n == 0) return 1;
        if(memo[n][index][k] != 0) return memo[n][index][k];
        int result = 0;
        for(int i = 0; i < 6; i++) {
            if(i == index) {
                if(rollMax[i] > k) {
                    result += dfs(n-1, i, k+1);
                    result %= MOD;
                }
            } else {
                result += dfs(n-1, i, 1);
                result %= MOD;
            }
        }
        memo[n][index][k] = result % MOD;
        return memo[n][index][k];
    }
}
```
