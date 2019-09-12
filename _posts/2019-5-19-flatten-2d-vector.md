---
title:  "251. Flatten 2D Vector"
date:   2019-05-19 19:28:00 +0930
categories: Leetcode
tags: Medium TwoPointer
---

[{{page.title}}](https://leetcode.com/problems/flatten-2d-vector/){:target="_blank"}

    Design and implement an iterator to flatten a 2d vector. It should support the following operations: next
    and hasNext.

    Example:

    Vector2D iterator = new Vector2D([[1,2],[3],[4]]);

    iterator.next(); // return 1
    iterator.next(); // return 2
    iterator.next(); // return 3
    iterator.hasNext(); // return true
    iterator.hasNext(); // return true
    iterator.next(); // return 4
    iterator.hasNext(); // return false



    Notes:

        Please remember to RESET your class variables declared in Vector2D, as static/class variables are
        persisted across multiple test cases. Please see here for more details.
        You may assume that next() call will always be valid, that is, there will be at least a next element in
        the 2d vector when next() is called.



    Follow up:

    As an added challenge, try to code it using only iterators in C++ or iterators in Java.




```java

class Vector2D {
    int i = 0, j = 0;
    int[][] nums;
    public Vector2D(int[][] v) {
        nums = v;
    }

    public int next() {
        hasNext();
        int v = nums[i][j];
        if(j == nums[i].length-1) {
            j = 0;
            i++;
        } else {
            j++;
        }
        return v;
    }

    public boolean hasNext() {
        while(i < nums.length && nums[i].length == 0) i++;
        if(i == nums.length) return false;
        return true;
    }
}
```
