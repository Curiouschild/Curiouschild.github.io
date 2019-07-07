---
title:  "829. Consecutive Numbers Sum"
date:   2019-3-25 23:54:00 +0930
categories: Leetcode
tags: Math
---

[{{page.title}}](https://leetcode.com/problems/consecutive-numbers-sum/){:target="_blank"}

    Given a positive integer N, how many ways can we write it as a sum of consecutive
    positive integers?

    Example 1:

    Input: 5
    Output: 2
    Explanation: 5 = 5 = 2 + 3

```java
public int consecutiveNumbersSum(int N) {
    int result = 0;
    for (int k = 1; k * (k + 1) <= 2 * N; k++) {
        if ((2* N - k * (k + 1)) % (2*k) == 0) result++;
    }
    return result;
}
```
