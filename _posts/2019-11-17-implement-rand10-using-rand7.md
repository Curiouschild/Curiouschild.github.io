---
title:  "470. Implement Rand10() Using Rand7()"
date:   2019-11-17 18:55:00 +0930
categories: Leetcode
tags: Medium Math Greedy
---

[{{page.title}}](https://leetcode.com/problems/implement-rand10-using-rand7/){:target="_blank"}

    Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which
    generates a uniform random integer in the range 1 to 10.

    Do NOT use system's Math.random().

    Example 1:

    Input: 1
    Output: [7]

    Example 2:

    Input: 2
    Output: [8,4]

    Example 3:

    Input: 3
    Output: [8,1,10]

    Note:

        rand7 is predefined.
        Each testcase has one argument: n, the number of times that rand10 is called.


* Give up illegal data points

```java

class Solution extends SolBase {
    public int rand10() {
        int row = 0, col = 0, index = 41;
        while(index > 40) {
            row = rand7();
            col = rand7();
            index = col + (row - 1) * 7;
        }
        return 1 + (index - 1) % 10;
    }
}
```
