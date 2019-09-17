---
title:  "247. Strobogrammatic Number II"
date:   2019-05-25 10:49:00 +0930
categories: Leetcode
tags: Medium Recursive Math
---

[{{page.title}}](https://leetcode.com/problems/strobogrammatic-number-ii/){:target="_blank"}

    A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

    Find all strobogrammatic numbers that are of length = n.

    Example:

    Input:  n = 2
    Output: ["11","69","88","96"]



* Easy


```java

int[] self = {0,1,8};
int[] nums = {0,1,6,9,8};
int[] map =  {0,1,0,0,0,0,9,0,8,6};
public List<String> findStrobogrammatic(int n) {
    ArrayList<String> result = new ArrayList<>();
    build(result, n, "", "");
    return result;
}

public void build(ArrayList<String> result, int n, String prefix, String suffix) {
    if(n == 0) {
        result.add(prefix + suffix);
    } else if(n == 1) {
        for(int i : self) {
            result.add(prefix + i + suffix);
        }
    } else {
        for(int i : nums) {
            if(prefix.length() == 0 && i == 0) continue;
            build(result, n-2, prefix+i, map[i]+suffix);
        }
    }
}
```
