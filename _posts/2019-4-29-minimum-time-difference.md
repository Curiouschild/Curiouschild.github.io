---
title:  "539. Minimum Time Difference"
date:   2019-4-29 21:09:00 +0930
categories: Leetcode
tags: Medium Array
---

[{{page.title}}](https://leetcode.com/problems/minimum-time-difference/){:target="_blank"}

    Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference
    between any two time points in the list.

    Example 1:

    Input: ["23:59","00:00"]
    Output: 1

    Note:

        The number of time points in the given list is at least 2 and won't exceed 20000.
        The input time is legal and ranges from 00:00 to 23:59.


* Build an array to store times

```java
public int findMinDifference(List<String> timePoints) {
    boolean[] seconds = new boolean[60 * 24];
    for(String s : timePoints) {
        int index = Integer.valueOf(s.substring(0,2))*60 + Integer.valueOf(s.substring(3,5));
        if(seconds[index]) return 0;
        seconds[index] = true;
    }
    int result = 60 * 24;
    int first = -1, prev = -1;
    for(int i = 0; i < seconds.length; i++) {
        if(!seconds[i]) continue;
        if(first == -1) first = i;
        if(prev != -1) result = Math.min(result, i-prev);
        prev = i;
    }
    result = Math.min(result, first + 60*24 - prev);
    return result;
}
```
