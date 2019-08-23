---
title:  "440. K-th Smallest in Lexicographical Order"
date:   2019-4-30 21:44:00 +0930
categories: Leetcode
tags: Hard DenaryTree TwoPointers
---

[{{page.title}}](https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/){:target="_blank"}

    Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.

    Note: 1 ≤ k ≤ n ≤ 109.

    Example:

    Input:
    n: 13   k: 2

    Output:
    10

    Explanation:
    The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is
    10.


* My brutal force solution fail to pass. TLE 40/69

The solution below is damn brilliant:
    Count the number of elements in a sub tree --> cnt.

    if cnt > target:

      // the target is in current subtree

      dive into this tree by: num *= 10

    else

      // the target is in the neighbors subtrees

      move to the next subtree by: num++


Note elements on the same level are consecutive increasing!!

https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/discuss/92242/ConciseEasy-to-understand-Java-5ms-solution-with-Explaination

```java

public int findKthNumber(int n, int k) {
    int curr = 1;
    k = k - 1;
    while (k > 0) {
        int steps = calSteps(n, curr, curr + 1);
        if (steps <= k) {
            curr += 1;
            k -= steps;
        } else {
            curr *= 10;
            k -= 1;
        }
    }
    return curr;
}
//use long in case of overflow
public int calSteps(int n, long n1, long n2) {
    int steps = 0;
    while (n1 <= n) {
        steps += Math.min(n + 1, n2) - n1;
        n1 *= 10;
        n2 *= 10;
    }
    return steps;
}
```
