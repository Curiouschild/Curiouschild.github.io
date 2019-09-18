---
title:  "1087. Brace Expansion"
date:   2019-05-25 10:53:00 +0930
categories: Leetcode
tags: Easy Math
---

[{{page.title}}](https://leetcode.com/problems/brace-expansion/){:target="_blank"}

    A string S represents a list of words.

    Each letter in the word has 1 or more options.  If there is one option, the letter is represented as is.  If there is more than one option, then curly braces delimit the options.  For example, "{a,b,c}" represents options ["a", "b", "c"].

    For example, "{a,b,c}d{e,f}" represents the list ["ade", "adf", "bde", "bdf", "cde", "cdf"].

    Return all words that can be formed in this manner, in lexicographical order.

    Example 1:

    Input: "{a,b}c{d,e}f"
    Output: ["acdf","acef","bcdf","bcef"]

    Example 2:

    Input: "abcd"
    Output: ["abcd"]

    Note:

        1 <= S.length <= 50
        There are no nested curly brackets.
        All characters inside a pair of consecutive opening and ending curly brackets are different.



* Easy

Brace expansion is easier than Medium
Brace expansion 2 is harder than Hard

```java

public String[] expand(String S) {
    ArrayList<String[]> arr = new ArrayList<>();
    int prev = 0;
    for(int i = 0; i < S.length(); i++) {
        char c = S.charAt(i);
        if(c == '{') {
            if(i > prev) {
                arr.add(getArr(S.substring(prev, i)));
            }
            prev = i+1;
        } else if(c == '}') {
            String sub = S.substring(prev, i);
            arr.add(getArr(sub));
            prev = i+1;
        }
    }
    if(prev < S.length()) arr.add(getArr(S.substring(prev)));
    ArrayList<String> result = new ArrayList<>();
    concatenate(result, 0, arr, "");
    return result.toArray(new String[0]);
}

public void concatenate(ArrayList<String> result, int index, ArrayList<String[]> arr, String temp) {
    if(index == arr.size()) {
        result.add(temp);
        return;
    }
    for(String s : arr.get(index)) {
        concatenate(result, index+1, arr, temp + s);
    }
}

public String[] getArr(String s) {
    if(s.contains(",")) {
        String[] result = s.split(",");
        Arrays.sort(result);
        return result;
    }
    return new String[] {s};
}
```
