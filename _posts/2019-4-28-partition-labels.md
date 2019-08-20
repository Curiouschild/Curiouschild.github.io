---
title:  "763. Partition Labels"
date:   2019-4-28 16:26:00 +0930
categories: Leetcode
tags: Medium Greedy
---

[{{page.title}}](https://leetcode.com/problems/partition-labels/){:target="_blank"}

    A string S of lowercase letters is given. We want to partition this string into as many parts as possible
    so that each letter appears in at most one part, and return a list of integers representing the size of
    these parts.

    Example 1:

    Input: S = "ababcbacadefegdehijhklij"
    Output: [9,7,8]
    Explanation:
    The partition is "ababcbaca", "defegde", "hijhklij".
    This is a partition so that each letter appears in at most one part.
    A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

    Note:

       S will have length in range [1, 500].
       S will consist of lowercase letters ('a' to 'z') only.


* Greedy

```java
public List<Integer> partitionLabels(String s) {
    HashMap<Character, Integer> map = new HashMap<>();
    for(int i = s.length()-1; i >= 0; i--) {
        if(!map.containsKey(s.charAt(i))) {
            map.put(s.charAt(i), i);
        }
    }
    ArrayList<Integer> result = new ArrayList<>();
    int i = 0, j = 0;
    while(j < s.length()) {
        for(int k = i; k <= j; k++) {
            j = Math.max(j, map.get(s.charAt(k)));
        }
        result.add(j-i+1);
        i = j + 1;
        j = i;
    }
    return result;
}
```
