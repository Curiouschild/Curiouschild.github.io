---
title:  "784. Letter Case Permutation"
date:   2019-05-13 11:24:00 +0930
categories: Leetcode
tags: Medium Backtrack
---

[{{page.title}}](https://leetcode.com/problems/letter-case-permutation/){:target="_blank"}


    Given a string S, we can transform every letter individually to be lowercase or uppercase to create another
    string.  Return a list of all possible strings we could create.

    Examples:
    Input: S = "a1b2"
    Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

    Input: S = "3z4"
    Output: ["3z4", "3Z4"]

    Input: S = "12345"
    Output: ["12345"]

    Note:

        S will be a string with length between 1 and 12.
        S will consist only of letters or digits.



```java

public List<String> letterCasePermutation(String S) {
    List<String> result = new ArrayList<>();
    generate(result, S, "");
    return result;
}
public void generate(List<String> result, String s, String buffer) {
    if(buffer.length() == s.length()) {
        result.add(buffer);
        return;
    }
    int i = buffer.length();
    char c  = s.charAt(i);
    generate(result, s, buffer + c);
    if(Character.isLetter(c)) {
        String next = buffer;
        if(c >= 'a' && c <= 'z') {
            next += Character.toUpperCase(c);
        } else {
            next += Character.toLowerCase(c);
        }
        generate(result, s, next);
    }
}
```
