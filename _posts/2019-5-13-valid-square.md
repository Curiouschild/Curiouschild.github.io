---
title:  "593. Valid Square"
date:   2019-05-13 14:41:00 +0930
categories: Leetcode
tags: Medium Math
---

[{{page.title}}](https://leetcode.com/problems/valid-square/){:target="_blank"}

    Given the coordinates of four points in 2D space, return whether the four points could construct a square.

    The coordinate (x,y) of a point is represented by an integer array with two integers.

    Example:

    Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
    Output: True



    Note:

        All the input integers are in the range [-10000, 10000].
        A valid square has four equal sides with positive length and four equal angles (90-degree angles).
        Input points have no order.


* Check diagonals.

p1       p3


p2       p4


```java

public boolean validSquare(int[] p1, int[] p2, int[] p3, int[] p4) {
    return check(p1, p2, p3, p4) || check(p1, p3, p2, p4) || check(p1, p4, p2, p3);
}

public boolean check(int[] p1, int[] p2, int[] p3, int[] p4) {
    if(p1[0] == p2[0] && p1[1] == p2[1]) return false;
    if(!(p1[0]+p2[0] == p3[0]+p4[0] && p1[1]+p2[1] == p3[1]+p4[1])) return false;
    if(!(d(p1, p3) == d(p1, p4))) return false;
    if(!(d(p1, p2) == d(p3, p4))) return false;
    return true;
}
public int d(int[] x, int[] y) {
    return (x[0]-y[0]) * (x[0]-y[0]) + (x[1]-y[1]) * (x[1]-y[1]);
}
```
