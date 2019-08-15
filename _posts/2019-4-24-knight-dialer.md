---
title:  "935. Knight Dialer"
date:   2019-4-24 09:12:00 +0930
categories: Leetcode
tags: DynamicProgramming
---

[{{page.title}}](https://leetcode.com/problems/knight-dialer/){:target="_blank"}


    A chess knight can move as indicated in the chess diagram below:

![img1](/img/posts/knight-dialer-1.png)

![img1](/img/posts/knight-dialer-2.png)


    This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes N-1 hops.  Each hop must be from one key to another numbered key.

    Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing N digits total.

    How many distinct numbers can you dial in this manner?

    Since the answer may be large, output the answer modulo 10^9 + 7.



    Example 1:

    Input: 1
    Output: 10

    Example 2:

    Input: 2
    Output: 20


```java

int MOD = 1000000007;
public int knightDialer(int N) {
    int[][] dict = {{4,6},{6,8},{7,9},{4,8},{0,3,9},{},{0,1,7},{2,6},{1,3},{2,4}};
    int[] cnt = new int[10];
    Arrays.fill(cnt, 1);
    while(N > 1) {
        int[] nextCnt = new int[10];
        for(int i = 0; i <= 9; i++) {
            for(int j : dict[i]) {
                nextCnt[j] += cnt[i];
                nextCnt[j] %= MOD;
            }
        }
        cnt = nextCnt;
        N--;
    }
    int result = 0;
    for(int i = 0; i <= 9; i++) {
        result += cnt[i];
        result %= MOD;
    }
    return result;
}
```
