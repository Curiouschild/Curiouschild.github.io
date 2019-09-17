---
title:  "246. Strobogrammatic Number"
date:   2019-05-25 10:53:00 +0930
categories: Leetcode
tags: Easy
---

[{{page.title}}](https://leetcode.com/problems/strobogrammatic-number/){:target="_blank"}

    A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

    Write a function to determine if a number is strobogrammatic. The number is represented as a string.

    Example 1:

    Input:  "69"
    Output: true

    Example 2:

    Input:  "88"
    Output: true

    Example 3:

    Input:  "962"
    Output: false

* Easy


```java

public boolean isStrobogrammatic(String num) {
    HashMap<Character, Character> map = new HashMap<>();
    map.put('6','9');
    map.put('9','6');
    map.put('0','0');
    map.put('1','1');
    map.put('8','8');
    int l = 0, r = num.length()-1;
    while(l <= r) {
        if(!map.containsKey(num.charAt(l)) ||map.get(num.charAt(l)) != num.charAt(r))
            return false;
        l++;
        r--;
    }
    return true;
}
```
