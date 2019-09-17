---
title:  "248. Strobogrammatic Number III"
date:   2019-05-25 11:45:00 +0930
categories: Leetcode
tags: Hard Recursive Math
---

[{{page.title}}](https://leetcode.com/problems/strobogrammatic-number-iii/){:target="_blank"}

    A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

    Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

    Example:

    Input: low = "50", high = "100"
    Output: 3
    Explanation: 69, 88, and 96 are three strobogrammatic numbers.

    Note:
    Because the range might be a large number, the low and high numbers are represented as string.


* Brutal: Use strobogrammatic number ii

This problem reminds me the hard [kth smallest number in lexicographical order](https://curiouschild.github.io/leetcode/2019/04/30/k-th-smallest-in-lexicographical-order.html){:target=_"blank}
But they are different, it is difficult to find a structured growing tree for this problem.

```java

class Solution {
    int[] self = {0,1,8};
    int[] nums = {0,1,6,9,8};
    int[] map =  {0,1,0,0,0,0,9,0,8,6};
    String low, high;
    public int strobogrammaticInRange(String low, String high) {
        this.low = low;
        this.high = high;
        int result = 0;
        for(int i = low.length(); i <= high.length(); i++) {
            result += findStrobogrammatic(i);
        }
        return result;
    }


    public int findStrobogrammatic(int n) {
        int result = build(n, "", "");
        return result;
    }

    public int build(int n, String prefix, String suffix) {
        int result = 0;
        if(n == 0) {
            if(inBound(prefix + suffix)) {
                result++;
            }
        } else if(n == 1) {
            for(int i : self)
                if(inBound(prefix + i + suffix)) {
                    result++;
                }
        } else {
            for(int i : nums) {
                if(prefix.length() == 0 && i == 0) continue;
                result += build(n-2, prefix+i, map[i]+suffix);
            }
        }
        return result;
    }

    public boolean inBound(String s) {
        if(s.length() == low.length() && s.compareTo(low) < 0) return false;
        if(s.length() == high.length() && s.compareTo(high) > 0) return false;
        return true;
    }
```
