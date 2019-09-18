---
title:  "809. Expressive Words"
date:   2019-05-25 22:44:00 +0930
categories: Leetcode
tags: Medium String
---

[{{page.title}}](https://leetcode.com/problems/expressive-words/){:target="_blank"}

    Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" ->
    "hiiii".  In these strings like "heeellooo", we have groups of adjacent letters that are all the same:
    "h", "eee", "ll", "ooo".

    For some given string S, a query word is stretchy if it can be made to be equal to S by any number of
    applications of the following extension operation: choose a group consisting of characters c, and add some
    number of characters c to the group so that the size of the group is 3 or more.

    For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we
    cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like
    "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy
    because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

    Given a list of query words, return the number of words that are stretchy.

    Example:
    Input:
    S = "heeellooo"
    words = ["hello", "hi", "helo"]
    Output: 1
    Explanation:
    We can extend "e" and "o" in the word "hello" to get "heeellooo".
    We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.

    Notes:

        0 <= len(S) <= 100.
        0 <= len(words) <= 100.
        0 <= len(words[i]) <= 100.
        S and all words in words consist only of lowercase letters



* half a hour to finish...


```java

public int expressiveWords(String S, String[] words) {
    int result = 0;
    for(String w : words) {
        if(isStretchy(S, w)) {
            result++;
        }
    }
    return result;
}

public boolean isStretchy(String t, String s) {
    if(s.length() > t.length() || t.length() < 3) return false;
    int i = 0, j = 0;
    int cnt = 0;
    while(i < t.length() || j < s.length()) {
        if(i == t.length() && j < s.length()) return false; // t: eeeeeeee
                                                            // s: ed
        if(j < s.length() && t.charAt(i) == s.charAt(j)) {
            i++;
            j++;
            continue;
        }
        if(i == 0 && j == 0) return false;
        if(t.charAt(i) == t.charAt(i-1)) { // if this is a valid expansion position
            char c = t.charAt(i);
            // check if there are three consecutive c, if yes, consume them all
            if(i-2 >= 0 && t.charAt(i-2) == c || i+1 < t.length() && t.charAt(i+1) == c) {
                while(i < t.length() && t.charAt(i) == c) i++;
                if(j == s.length()) return i == t.length();
                continue;
            }
        }
        return false;
    }
    return true;

}
```
