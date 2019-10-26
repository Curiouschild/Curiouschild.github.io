---
title:  "668. Kth Smallest Number in Multiplication Table"
date:   2019-06-24 16:28:00 +0930
categories: Leetcode
tags: Hard BinarySearch
---

[{{page.title}}](https://leetcode.com/problems/next-greater-element-ii/){:target="_blank"}

    Nearly every one have used the Multiplication Table. But could you find out the k-th smallest number
    quickly from the multiplication table?

    Given the height m and the length n of a m * n Multiplication Table, and a positive integer k, you need to
    return the k-th smallest number in this table.

    Example 1:

    Input: m = 3, n = 3, k = 5
    Output:
    Explanation:
    The Multiplication Table:
    1	2	3
    2	4	6
    3	6	9

    The 5-th smallest number is 3 (1, 2, 2, 3, 3).

    Example 2:

    Input: m = 2, n = 3, k = 6
    Output:
    Explanation:
    The Multiplication Table:
    1	2	3
    2	4	6

    The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).

    Note:

        The m and n will be in the range [1, 30000].
        The k will be in the range [1, m * n]


* Binary Search


```java

public int findKthNumber(int n, int m, int k) {
    int l = 1, r = n * m;
    while(l < r) {
        int mid = l + (r-l) / 2;
        int row = 1, col = n, cnt = 0;
        while(row <= m && col >= 1) {
            if(row * col <= mid) {
                cnt += col;
                row++;
            } else {
                col--;
            }
        }
        // System.out.println(l + " " + r + " m=" + mid  + " cnt=" + cnt);
        if(cnt >= k) {
            r = mid;
        } else {
            l = mid+1;
        }
    }
    return l;
}
```


* TLE PriorityQueue

```java

public int findKthNumber2(int row, int col, int k) {
    int n = Math.max(row, col), m = Math.min(row, col);
    PriorityQueue<int[]> q = new PriorityQueue<>((a,b)->(a[0]*a[1]-b[0]*b[1]));
    for(int i = 1; i <= m; i++) {
        q.offer(new int[]{i,i});
    }
    int cnt = 0;
    while(!q.isEmpty()) {
        int[] p = q.poll();
        cnt++;
        if(p[0] != p[1]) {
            if(p[0] <= n && p[1] <= m) {
                cnt++;
            }
        }
        if(cnt >= k) {
            return p[0] * p[1];
        }
        if(p[1]+1 <= n)
            q.offer(new int[]{p[0], p[1]+1});
    }
    return -1;
}
```
