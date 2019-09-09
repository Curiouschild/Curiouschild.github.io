---
title:  "179. Largest Number"
date:   2019-05-13 11:24:00 +0930
categories: Leetcode
tags: Medium String
---

[{{page.title}}](https://leetcode.com/problems/largest-number/){:target="_blank"}

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"

Example 2:

Input: [3,30,34,5,9]
Output: "9534330"

Note: The result may be very large, so you need to return a string instead of an integer.


```java

public String largestNumber(int[] nums) {
    PriorityQueue<String> q = new PriorityQueue<String>((a,b)->{
        String s1 = a+b, s2 = b+a;
        return s2.compareTo(s1);
    });
    for(int i : nums) {
        q.offer("" + i);
    }
    String r = "";
    while(!q.isEmpty()) {
        r += q.poll();
    }
    if(r.charAt(0) == '0') return "0";
    return r;
}
```
