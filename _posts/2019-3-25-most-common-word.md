---
title:  "819. Most Common Word"
date:   2019-3-25 14:47:00 +0930
categories: Leetcode
tags: TwoPointers RegularExpression
---

[{{page.title}}](https://leetcode.com/problems/most-common-word/){:target="_blank"}

    Given a paragraph and a list of banned words, return the most frequent word that is not
    in the list of banned words.  It is guaranteed there is at least one word that isn't banned,
    and that the answer is unique.

    Words in the list of banned words are given in lowercase, and free of punctuation.  Words in
    the paragraph are not case sensitive.  The answer is in lowercase.


    Example:

    Input:
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    Output: "ball"
    Explanation:
    "hit" occurs 3 times, but it is a banned word.
    "ball" occurs twice (and no other word does), so it is the most frequent non-banned word
    in the paragraph.
    Note that words in the paragraph are not case sensitive,
    that punctuation is ignored (even if adjacent to words, such as "ball,"),
    and that "hit" isn't the answer even though it occurs more because it is banned.


```java
public String mostCommonWord(String paragraph, String[] banned) {
    HashSet<String> set = new HashSet<>(Arrays.asList(banned));
    HashMap<String, Integer> counter = new HashMap<>();
    int i = 0, j = 0;
    while(i < paragraph.length()) {
        while(i < paragraph.length() && !Character.isLetter(paragraph.charAt(i)))
            i++;
        j = i;
        while(i < paragraph.length() && Character.isLetter(paragraph.charAt(i)))
            i++;
        String curr = paragraph.substring(j, i).toLowerCase();
        if(i == j || set.contains(curr)) continue;
        counter.put(curr, counter.getOrDefault(curr, 0) + 1);
    }
    int max = 0;
    String result = "";
    for(Map.Entry<String, Integer> e : counter.entrySet()) {
        if(e.getValue() > max) {
            max = e.getValue();
            result = e.getKey();
        }
    }
    return result;
}
```

Or preprocess with regular expression

```java

public String mostCommonWordOld(String paragraph, String[] banned) {
    HashSet<String> set = new HashSet<>();
    for(String w : banned) set.add(w);
    paragraph = paragraph.replaceAll("[^a-zA-Z]", " ").toLowerCase();
    String[] words = paragraph.split("\\s+");
    HashMap<String, Integer> map = new HashMap<>();
    for(String w : words) {
        if(set.contains(w)) continue;
        int v = map.getOrDefault(w, 0);
        map.put(w, v+1);
    }
    int max = 0;
    String r = null;
    for(Map.Entry<String,Integer> e : map.entrySet()) {
        int v = e.getValue();
        if(max < v) {
            max = v;
            r = e.getKey();
        }
    }
    return r;
}
```
