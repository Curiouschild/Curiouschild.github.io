---
title:  "1049. Last Stone Weight II"
date:   2019-05-31 14:48:00 +0930
categories: Leetcode
tags: Medium Knapsack DynamicProgramming
---

[{{page.title}}](https://leetcode.com/problems/last-stone-weight-ii/){:target="_blank"}

    We have a collection of rocks, each rock has a positive integer weight.

    Each turn, we choose any two rocks and smash them together.  Suppose the stones have weights x and y with x
    <= y.  The result of this smash is:

        If x == y, both stones are totally destroyed;
        If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

    At the end, there is at most 1 stone left.  Return the smallest possible weight of this stone (the weight
    is 0 if there are no stones left.)



    Example 1:

    Input: [2,7,4,1,8,1]
    Output: 1
    Explanation:
    We can combine 2 and 4 to get 2 so the array converts to [2,7,1,8,1] then,
    we can combine 7 and 8 to get 1 so the array converts to [2,1,1,1] then,
    we can combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
    we can combine 1 and 1 to get 0 so the array converts to [1] then that's the optimal value.



    Note:

        1 <= stones.length <= 30
        1 <= stones[i] <= 100

* 01 Knapsack problem
  - cost array == value array
  - capacity == sum / 2

```java

public int lastStoneWeightII(int[] stones) {
    int sum = 0;
    for(int i : stones) sum += i;
    int V = sum / 2;
    int[] dp = new int[V+1];
    for(int stone : stones)
        for(int j = V; j >= stone; j--)
            dp[j] = Math.max(dp[j], dp[j-stone]+stone);
    return sum - 2 * dp[V];
}
```
