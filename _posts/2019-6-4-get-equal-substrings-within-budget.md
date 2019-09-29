---
title:  "1208. Get Equal Substrings Within Budget"
date:   2019-06-04 22:21:00 +0930
categories: Leetcode
tags: Medium SlidingWindow
---

[{{page.title}}](https://leetcode.com/problems/get-equal-substrings-within-budget/){:target="_blank"}

    You are given two strings s and t of the same length. You want to change s to t. Changing the i-th
    character of s to i-th character of t costs |s[i] - t[i]| that is, the absolute difference between the
    ASCII values of the characters.

    You are also given an integer maxCost.

    Return the maximum length of a substring of s that can be changed to be the same as the corresponding
    substring of twith a cost less than or equal to maxCost.

    If there is no substring from s that can be changed to its corresponding substring from t, return 0.

    Example 1:

    Input: s = "abcd", t = "bcdf", cost = 3
    Output: 3
    Explanation: "abc" of s can change to "bcd". That costs 3, so the maximum length is 3.

    Example 2:

    Input: s = "abcd", t = "cdef", cost = 3
    Output: 1
    Explanation: Each charactor in s costs 2 to change to charactor in t, so the maximum length is 1.

    Example 3:

    Input: s = "abcd", t = "acde", cost = 0
    Output: 1
    Explanation: You can't make any change, so the maximum length is 1.



    Constraints:

        1 <= s.length, t.length <= 10^5
        0 <= maxCost <= 10^6
        s and t only contain lower case English letters.


* sliding window

```java

class Solution {
    public int equalSubstring(String s, String t, int maxCost) {
        int result = 0;
        int[] arr = new int[s.length()];
        for(int i = 0; i < s.length(); i++)
            arr[i] = Math.abs(s.charAt(i)-t.charAt(i));
        int sum = 0, l = 0, r = 0;
        while(r < arr.length) {
            if(sum <= maxCost) {
                result = Math.max(result, r-l);
                sum += arr[r];
                r++;
            } else {
                sum -= arr[l];
                l++;
            }
        }
        if(sum <= maxCost) result = Math.max(result, r-l);
        return result;
    }
}

```
