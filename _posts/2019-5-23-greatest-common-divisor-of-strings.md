---
title:  "1071. Greatest Common Divisor of Strings"
date:   2019-05-23 22:26:00 +0930
categories: Leetcode
tags: Hard SegmentTree
---

[{{page.title}}](https://leetcode.com/problems/range-sum-query-mutable/){:target="_blank"}

    For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or
    more times)

    Return the largest string X such that X divides str1 and X divides str2.



    Example 1:

    Input: str1 = "ABCABC", str2 = "ABC"
    Output: "ABC"

    Example 2:

    Input: str1 = "ABABAB", str2 = "ABAB"
    Output: "AB"

    Example 3:

    Input: str1 = "LEET", str2 = "CODE"
    Output: ""



    Note:

        1 <= str1.length <= 1000
        1 <= str2.length <= 1000
        str1[i] and str2[i] are English uppercase letters.


* Brutal Force

```java
class Solution {
    public String gcdOfStrings(String s1, String s2) {
        int l1 = s1.length(), l2 = s2.length();
        String result = "";
        for(int i = 0; i < Math.min(l1, l2); i++) {
            if(s1.charAt(i) != s2.charAt(i)) return "";
            int l = i+1;
            if(l1 % l != 0 || l2 % l != 0) continue;
            String s = s1.substring(0, i+1);
            if(check(s1, s) && check(s2, s)) {
                result = s;
            }
        }
        return result;
    }

    public boolean check(String s, String t) {
        if(s.equals(t)) return true;
        if(s.substring(0, t.length()).equals(t)) {
            return check(s.substring(t.length()), t);
        }
        return false;
    }
}

}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * obj.update(row,col,val);
 * int param_2 = obj.sumRegion(row1,col1,row2,col2);
 */
```
