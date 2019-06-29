---
title:  "9. Palindrome Number"
date:   2019-3-18 15:58:22 +0930
categories: Leetcode
tags: Math
---

[{{page.title}}](https://leetcode.com/problems/palindrome-number/){:target="_blank"}

    Determine whether an integer is a palindrome. An integer is a palindrome when
    it reads the same backward as forward.

    Example 1:

    Input: 121
    Output: true

    Example 2:

    Input: -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
    Therefore it is not a palindrome.

* Compare Half

```java

public boolean isPalindrome(int x) {
    if(x < 0 || x > 0 && x % 10 == 0) return false;
    int re = 0;
    while(x > re) {
        re = re * 10 + x % 10;
        x /= 10;
    }
    return re == x || re / 10 == x;
}
```
