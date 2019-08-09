---
title:  "17. Letter Combinations of a Phone Number"
date:   2019-3-15 17:29:09 +0930
categories: Leetcode
tags: Permutation BackTraking
---

[{{page.title}}](https://leetcode.com/problems/letter-combinations-of-a-phone-number/){:target="_blank"}

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

![kdf](/img/posts/letter_combinations_of_a_phone_number.png)

```java
public List<String> letterCombinations(String digits) {
    if(digits.length() == 0) return new ArrayList<>();
    String[] dict = new String[10];
    dict[2] = "abc";
    dict[3] = "def";
    dict[4] = "ghi";
    dict[5] = "jkl";
    dict[6] = "mno";
    dict[7] = "pqrs";
    dict[8] = "tuv";
    dict[9] = "wxyz";
    List<String> result = new ArrayList<>();
    dfs(digits, result, dict, new StringBuilder(), 0);
    return result;
}

public void dfs(String digits, List<String> result, String[] dict, StringBuilder sb, int i) {
    if(i == digits.length()) {
        result.add(sb.toString());
    } else {
        for(char c : dict[digits.charAt(i)-'0'].toCharArray()) {
            sb.append(c);
            dfs(digits, result, dict, sb, i+1);
            sb.setLength(sb.length()-1);
        }
    }
}
```
