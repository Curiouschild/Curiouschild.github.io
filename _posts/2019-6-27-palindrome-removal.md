---
title:  "1246. Palindrome Removal"
date:   2019-06-27 15:10:00 +0930
categories: Leetcode
tags: Hard DynamicProgramming
---

[{{page.title}}](https://leetcode.com/problems/palindrome-removal/){:target="_blank"}

    Given an integer array arr, in one move you can select a palindromic subarray arr[i], arr[i+1], ..., arr[j] where i
    <= j, and remove that subarray from the given array. Note that after removing a subarray, the elements on the left
    and on the right of that subarray move to fill the gap left by the removal.

    Return the minimum number of moves needed to remove all numbers from the array.

    Example 1:

    Input: arr = [1,2]
    Output: 2

    Example 2:

    Input: arr = [1,3,4,1,5]
    Output: 3
    Explanation: Remove [4] then remove [1,3,1] then remove [5].

    Constraints:

        1 <= arr.length <= 100
        1 <= arr[i] <= 20

* DP

```java

public int minimumMoves(int[] arr) {
    int N = arr.length;
    int[][] dp = new int[N+1][N];
    for(int w = 1; w <= N; w++) { // w: window size
        for(int i = 0; i+w-1 < N; i++) {
            int j = i+w-1;
            if(w == 1) {
                dp[i][j] = 1;
            } else {
                dp[i][j] = 1 + dp[i+1][j]; // remove i
                if(arr[i] == arr[i+1]) {
                    dp[i][j] = Math.min(dp[i][j], 1 + dp[i+2][j]); // remove i and i+1
                }
                for(int k = i+2; k <= j; k++) {
                    if(arr[k] == arr[i]) { // remove i and k alone with substring between them
                        dp[i][j] = Math.min(dp[i][j], dp[i+1][k-1] + dp[k+1][j]);
                    }
                }
            }
        }
    }
    return dp[0][N-1];
}
```
