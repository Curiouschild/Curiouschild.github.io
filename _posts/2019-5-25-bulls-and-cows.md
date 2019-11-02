---
title:  "299. Bulls and Cows"
date:   2019-05-25 20:03:00 +0930
categories: Leetcode
tags: Easy Math
---

[{{page.title}}](https://leetcode.com/problems/bulls-and-cows/){:target="_blank"}

    You are playing the following Bulls and Cows game with your friend: You write down a number and ask your
    friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates
    how many digits in said guess match your secret number exactly in both digit and position (called "bulls")
    and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend
    will use successive guesses and hints to eventually derive the secret number.

    Write a function to return a hint according to the secret number and friend's guess, use A to indicate the
    bulls and B to indicate the cows.

    Please note that both secret number and friend's guess may contain duplicate digits.

    Example 1:

    Input: secret = "1807", guess = "7810"

    Output: "1A3B"

    Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.

    Example 2:

    Input: secret = "1123", guess = "0111"

    Output: "1A1B"

    Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.

    Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.


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
