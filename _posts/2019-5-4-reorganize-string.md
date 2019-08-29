---
title:  "767. Reorganize String"
date:   2019-05-04 18:35:00 +0930
categories: Leetcode
tags: Medium Sorting
---

[{{page.title}}](https://leetcode.com/problems/partition-equal-subset-sum/){:target="_blank"}

    Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

    If possible, output any possible result.  If not possible, return the empty string.

    Example 1:

    Input: S = "aab"
    Output: "aba"

    Example 2:

    Input: S = "aaab"
    Output: ""

    Note:
        S will consist of lowercase letters and have length in range [1, 500].

* Similar to CPU cool down time

```java
class Solution {
    public String reorganizeString(String S) {
        int[] count = new int[26];
        for(char c : S.toCharArray()) count[c-'a']++;
        int[][] c2c = new int[26][];
        for(int i = 0; i < 26; i++) c2c[i] = new int[] {i, count[i]};
        char p = 'A';
        String result = "";
        while(true) {
            Arrays.sort(c2c, (a,b)->(a[1]-b[1]));
            int i = 25;
            while(i >= 0 && c2c[i][1] == 0) i--;
            if(i == -1) break;
            if('a' + c2c[i][0] == p) {
                i--;
                while(i >= 0 && c2c[i][1] == 0) i--;
                if(i == -1) return "";
            }
            c2c[i][1]--;
            result += (char)('a' + c2c[i][0]);
            p = (char)('a' + c2c[i][0]);
        }
        return result;
    }
}
```

* PriorityQueue

```java
public String reorganizeString(String S) {
    int[][] count = new int[26][];
    for(int i = 0; i < 26; i++) count[i] = new int[] {i, 0};
    for(char c : S.toCharArray()) count[c-'a'][1]++;
    PriorityQueue<int[]> q = new PriorityQueue<>((a,b)->(b[1]-a[1] == 0 ? a[0]-b[0] : b[1]-a[1]));
    for(int[] c : count)
        if(c[1] > 0)
            q.offer(c);
    String r = "";
    while(!q.isEmpty()) {
        int[] most = q.poll();
        if(q.isEmpty()) {
            if(r.length()-1 >= 0 && r.charAt(r.length()-1) == (char)(most[0]+'a')) return "";
            r += (char)(most[0]+'a');
        } else {
            int[] second = q.poll();

            r += (char)(most[0]+'a') + "" + (char)(second[0]+'a');
            second[1]--;
            if(second[1] > 0)
                q.offer(second);
        }
        most[1]--;
        if(most[1] > 0)
            q.offer(most);
    }
    return r;
}
```
