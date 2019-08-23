---
title:  "96. Unique Binary Search Trees"
date:   2019-05-01 10:22:00 +0930
categories: Leetcode
tags: Medium DynamicProgramming Math
---

[{{page.title}}](https://leetcode.com/problems/unique-binary-search-trees/){:target="_blank"}

    Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

    Example:

    Input: 3
    Output: 5
    Explanation:
    Given n = 3, there are a total of 5 unique BST's:

       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3



```java
class Solution {

    public int numTrees(int n) {
        return build(n, new int[n+1]);
    }
    public int build(int n, int[] dp) {
        if(n <= 1) return 1;
        if(dp[n] > 0) return dp[n];
        int result = 0;
        for(int i = 1; i <= n; i++) {
            result += build(i-1, dp) * build(n-i, dp);
        }
        dp[n] = result;
        return result;
    }
}
```
