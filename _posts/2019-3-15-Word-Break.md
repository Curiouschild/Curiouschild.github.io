---
title:  "139. Word Break"
date:   2019-3-15 18:41:13 +0930
categories: Leetcode
tags: DynamicProgramming String Recursive
---

[{{page.title}}](https://leetcode.com/problems/word-break/){:target="_blank"}

    Given a non-empty string s and a dictionary wordDict containing a list of non-empty
    words, determine if s can be segmented into a space-separated sequence of one or more
    dictionary words.

    Note:

        The same word in the dictionary may be reused multiple times in the segmentation.
        You may assume the dictionary does not contain duplicate words.

    Example 1:

    Input: s = "leetcode", wordDict = ["leet", "code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet code".

    Example 2:

    Input: s = "applepenapple", wordDict = ["apple", "pen"]
    Output: true
    Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
                 Note that you are allowed to reuse a dictionary word.


* Bootom Up

```java
public boolean wordBreak(String s, List<String> wordDict) {
    boolean[] dp = new boolean[s.length()+1];
    HashSet<String> dict = new HashSet<String>(wordDict);
    dp[0] = true;
    for(int i = 1; i < dp.length; i++) {
        for(int j = 0; j < i; j++) {
            if(dp[j] && dict.contains(s.substring(j, i))) {
                dp[i] = true;
                break;
            }
        }
    }
    return dp[s.length()];
}
```

* Memorisation

```java
public boolean wordBreak(String s, List<String> wordDict) {
    HashSet<String> dict = new HashSet<String>(wordDict);
    HashMap<String, Boolean> dp = new HashMap<>();
    dp.put("", true);
    boolean result = recursive(s, dict, dp);
    return result;
}

public boolean recursive(String s, HashSet<String> dict, HashMap<String, Boolean> dp) {
    if(dp.containsKey(s)) return dp.get(s);
    for(int i = 0; i <= s.length(); i++) {
        if(dict.contains(s.substring(0,i))) {
            if(recursive(s.substring(i, s.length()), dict, dp)) {
                dp.put(s, true);
                return true;
            }
        }
    }
    dp.put(s, false);
    return false;
}
```
