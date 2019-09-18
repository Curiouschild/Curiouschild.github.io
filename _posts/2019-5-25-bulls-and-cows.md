---
title:  "246. Strobogrammatic Number"
date:   2019-05-25 10:53:00 +0930
categories: Leetcode
tags: Easy Math
---

[{{page.title}}](https://leetcode.com/problems/strobogrammatic-number/){:target="_blank"}

    A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

    Write a function to determine if a number is strobogrammatic. The number is represented as a string.

    Example 1:

    Input:  "69"
    Output: true

    Example 2:

    Input:  "88"
    Output: true

    Example 3:

    Input:  "962"
    Output: false

* Easy

A very smart one pass solution. [{{source}}](https://leetcode.com/problems/bulls-and-cows/discuss/74621/One-pass-Java-solution/){:target="_blank"}

Increment or decrement the count of characters for chars from secret or guess.

```java

public String getHint(String secret, String guess) {
    int[] cnt = new int[10];
    int bull = 0, cow = 0;
    for(int i = 0; i < secret.length(); i++) {
        int s = secret.charAt(i)-'0', g = guess.charAt(i)-'0';
        if(s == g) {
            bull++;
        } else {
            if(cnt[s] < 0) cow++;
            if(cnt[g] > 0) cow++;
            cnt[s]++;
            cnt[g]--;
        }
    }
    return bull + "A" + cow + "B";
}
```

* Two pass

```java

public String getHintTwoPass(String secret, String guess) {
    HashMap<Character, Integer> map = new HashMap<>();
    ArrayList<Character> incorrect = new ArrayList<>();
    int bull = 0, cow = 0;
    for(int i = 0; i < secret.length(); i++) {
        char s = secret.charAt(i), g = guess.charAt(i);
        if(s == g) {
            bull++;
        } else {
            map.put(s, map.getOrDefault(s, 0)+1);
            incorrect.add(g);
        }
    }
    for(char c : incorrect) {
        if(map.containsKey(c) && map.get(c) > 0) {
            map.put(c, map.get(c)-1);
            cow++;
        }
    }
    return bull + "A" + cow + "B";
}
```
