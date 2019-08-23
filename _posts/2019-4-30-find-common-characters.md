---
title:  "1002. Find Common Characters"
date:   2019-4-30 22:24:00 +0930
categories: Leetcode
tags: Easy
---

[{{page.title}}](https://leetcode.com/problems/find-common-characters/){:target="_blank"}

    Given an array A of strings made only from lowercase letters, return a list of all characters that show up
    in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all
    strings but not 4 times, you need to include that character three times in the final answer.

    You may return the answer in any order.

    Example 1:

    Input: ["bella","label","roller"]
    Output: ["e","l","l"]

    Example 2:

    Input: ["cool","lock","cook"]
    Output: ["c","o"]

* Easy

int[26] is a good friend of all lower case letters

```java
public List<String> commonChars(String[] A) {
    ArrayList<String> result = new ArrayList<>();
    int[] cnt = new int[26], temp = new int[26];
    Arrays.fill(cnt, Integer.MAX_VALUE);
    for(int i = 0; i < A.length; i++) {
        for(char c : A[i].toCharArray()) temp[c-'a']++;
        for(int j = 0; j < 26; j++) cnt[j] = Math.min(cnt[j], temp[j]);
        Arrays.fill(temp, 0);
    }
    for(int i = 0; i < 26; i++)
        for(int j = 0; j < cnt[i]; j++)
            result.add("" + (char)(i+'a'));
    return result;
}
```
