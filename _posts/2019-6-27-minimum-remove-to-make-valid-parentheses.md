---
title:  "1249. Minimum Remove to Make Valid Parentheses"
date:   2019-06-27 15:15:00 +0930
categories: Leetcode
tags: Medium Parentheses
---

[{{page.title}}](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/){:target="_blank"}

    Given a string s of '(' , ')' and lowercase English characters.

    Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting
    parentheses string is valid and return any valid string.

    Formally, a parentheses string is valid if and only if:

        It is the empty string, contains only lowercase characters, or
        It can be written as AB (A concatenated with B), where A and B are valid strings, or
        It can be written as (A), where A is a valid string.


    Example 1:

    Input: s = "lee(t(c)o)de)"
    Output: "lee(t(c)o)de"
    Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

    Example 2:

    Input: s = "a)b(c)d"
    Output: "ab(c)d"

    Example 3:

    Input: s = "))(("
    Output: ""
    Explanation: An empty string is also valid.

    Example 4:

    Input: s = "(a(b(c)d)"
    Output: "a(b(c)d)"



    Constraints:

        1 <= s.length <= 10^5
        s[i] is one of  '(' , ')' and lowercase English letters.


* O(N)
  - first pass remove invalid ')'
  - second pass remove invalid '('

```java

public String minRemoveToMakeValid(String s) {
    StringBuilder sb = new StringBuilder();
    int cnt = 0;
    for (char c : s.toCharArray()) {
        if (c == '(') {
            cnt++;
        } else if (c == ')') {
            if (cnt == 0) continue;
            cnt--;
        }
        sb.append(c);
    }

    for (int i = sb.length() - 1; i >= 0 && cnt > 0; i--) {
        if (sb.charAt(i) == '(') {
            sb.deleteCharAt(i);
            cnt--;
        }
    }
    return sb.toString();
}
```
