---
title:  "992. Subarrays with K Different Integers"
date:   2019-06-27 15:15:00 +0930
categories: Leetcode
tags: Hard DFS Tree
---

[{{page.title}}](https://leetcode.com/problems/subarrays-with-k-different-integers/){:target="_blank"}

    Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the
    number of different integers in that subarray is exactly K.

    (For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

    Return the number of good subarrays of A.

    Example 1:

    Input: A = [1,2,1,2,3], K = 2
    Output: 7
    Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].

    Example 2:

    Input: A = [1,2,1,3,4], K = 3
    Output: 3
    Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

    Note:

        1 <= A.length <= 20000
        1 <= A[i] <= A.length
        1 <= K <= A.length

* SlidingWindow

```java

public int subarraysWithKDistinct(int[] A, int K) {
    return atMostK(A, K) - atMostK(A, K - 1);
}
public int atMostK(int[] A, int K) {
    int i = 0, res = 0;
    Map<Integer, Integer> count = new HashMap<>();
    for (int j = 0; j < A.length; j++) {
        if (!count.containsKey(A[j]) || count.get(A[j]) == 0) K--;
        count.put(A[j], count.getOrDefault(A[j], 0) + 1);
        while (K < 0) {
            count.put(A[i], count.get(A[i]) - 1);
            if (count.get(A[i]) == 0) K++;
            i++;
        }
        res += j - i + 1;
    }
    return res;
}
```
