---
title:  "1011. Capacity To Ship Packages Within D Days"
date:   2019-05-09 08:32:00 +0930
categories: Leetcode
tags: Hard DynamicProgramming BinarySearch
---

[{{page.title}}](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/){:target="_blank"}

    A conveyor belt has packages that must be shipped from one port to another within D days.

    The i-th package on the conveyor belt has a weight of weights[i].  Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

    Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.



    Example 1:

    Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
    Output: 15
    Explanation:
    A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
    1st day: 1, 2, 3, 4, 5
    2nd day: 6, 7
    3rd day: 8
    4th day: 9
    5th day: 10

    Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

    Example 2:

    Input: weights = [3,2,2,4,1,4], D = 3
    Output: 6
    Explanation:
    A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
    1st day: 3, 2
    2nd day: 2, 4
    3rd day: 1, 4

    Example 3:

    Input: weights = [1,2,3,1,1], D = 4
    Output: 3
    Explanation:
    1st day: 1
    2nd day: 2
    3rd day: 3
    4th day: 1, 1



    Note:

        1 <= D <= weights.length <= 50000
        1 <= weights[i] <= 500


* Totally the same with split array largest sum, why one is a medium and another is hard?

```java
public int shipWithinDaysDP(int[] weights, int D) {
    if(weights.length == 0 || D == 0) return 0;
    int[] pre = new int[weights.length];
    pre[0] = weights[0];
    for(int i = 1; i < weights.length; i++)
        pre[i] = pre[i-1] + weights[i];
    int[][] dp = new int[D][weights.length];
    for(int i = 1; i < dp.length; i++)
        Arrays.fill(dp[i], Integer.MAX_VALUE);

    System.arraycopy(pre, 0, dp[0], 0, pre.length);
    for(int i = 1; i < dp.length; i++) {
        for(int j = i; j < dp[0].length; j++) {
            for(int k = i-1; k < j; k++) {
                dp[i][j] = Math.min(dp[i][j], Math.max(dp[i-1][k], pre[j]-pre[k]));
            }
        }
    }
    return dp[dp.length-1][dp[0].length-1];
}
```

* Binary Search

```java
public int shipWithinDays(int[] weights, int D) {
    int l = 0, r = 0;
    for(int n : weights) {
        l = Math.max(l, n);
        r += n;
    }
    while(l < r) {
        int mid = l + (r-l) / 2;
        if(canSplit(weights, D, mid)) {
            r = mid;
        } else
            l = mid + 1;
    }
    return r;
}
public boolean canSplit(int[] arr, int d, int target) {
    int sum = 0;
    int cnt = 0;
    for(int n : arr) {
        if(n > target) return false;
        if(n + sum > target) {
            cnt++;
            sum = n;
        } else {
            sum += n;
        }
    }
    return cnt+1 <= d;
}
```
