---
title:  "402. Remove K Digits"
date:   2019-06-06 17:05:00 +0930
categories: Leetcode
tags: Medium Greedy Stack
---

[{{page.title}}](https://leetcode.com/problems/remove-k-digits/){:target="_blank"}

    Given a non-negative integer num represented as a string, remove k digits from the number so that the new
    number is the smallest possible.

    Note:

        The length of num is less than 10002 and will be ≥ k.
        The given num does not contain any leading zero.

    Example 1:

    Input: num = "1432219", k = 3
    Output: "1219"
    Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

    Example 2:

    Input: num = "10200", k = 1
    Output: "200"
    Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading
    zeroes.

    Example 3:

    Input: num = "10", k = 2
    Output: "0"
    Explanation: Remove all the digits from the number and it is left with nothing which is 0.


* Stack

```java

public String removeKdigits(String num, int k) {
        if(k == num.length()) return "0";
        LinkedList<Character> stack = new LinkedList<>();
        int cnt = 0;
        for(int i = 0; i < num.length(); i++) {
            char c = num.charAt(i);
            while(cnt < k && !stack.isEmpty() && stack.peek() > c) {
                stack.pop();
                cnt++;
            }
            stack.push(c);
        }
        while(cnt < k) {
            stack.removeFirst();
            cnt++;
        }
        StringBuilder result = new StringBuilder();
        for(char c : stack) result.insert(0, c);
        int j = 0;
        while(j < result.length() && result.charAt(j) == '0') j++;
        if(j == result.length()) return "0";
        return result.toString().substring(j);
    }
```
