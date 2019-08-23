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

The key is the sequence N1,N2,N3,N4,...,NM has the same number of tree combination with the sequences
1,2,3,4,...,M. So we can break this problem down to smaller problems.

Also mathematically this problem is to calculate a Catalan number.
C = C * 2 * (2 * i + 1) / (i + 2)

* Top Down

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

* Bottom Up

```java
public int numTrees(int n) {
    int[] dp = new int[n+1];
    dp[0] = 1;
    dp[1] = 1;
    for(int i = 2; i <= n; i++) {
        for(int j = 1; j <= i; j++) {
            dp[i] += dp[j-1] * dp[i-j];
        }
    }
    return dp[n];
}
```
