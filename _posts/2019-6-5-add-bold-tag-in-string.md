---
title:  "616. Add Bold Tag in String"
date:   2019-06-05 15:38:00 +0930
categories: Leetcode
tags: Medium Interval
---

[{{page.title}}](https://leetcode.com/problems/add-bold-tag-in-string/){:target="_blank"}

    Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap
    the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by
    only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to
    combine them.

    Example 1:

    Input:
    s = "abcxyz123"
    dict = ["abc","123"]
    Output:
    "<b>abc</b>xyz<b>123</b>"

    Example 2:

    Input: 
    s = "aaabbcc"
    dict = ["aaa","aab","bc"]
    Output:
    "<b>aaabbc</b>c"

    Note:

        The given dict won't contain duplicates, and its length won't exceed 100.
        All the strings in input have length in range [1, 1000].


* Merge Interval

```java

public String addBoldTag(String input, String[] dict) {
        HashSet<String> set = new HashSet<>();
        int max = 0;
        for(String s : dict) {
            set.add(s);
            max = Math.max(max, s.length());
        }
        ArrayList<int[]> arr = new ArrayList<>();
        for(int i = 0; i < input.length(); i++) {
            for(int j = Math.min(i + max, input.length()); j > i; j--) {
                String candidate = input.substring(i, j);
                if(set.contains(candidate)) {
                    if(arr.size() > 0 && arr.get(arr.size()-1)[1] >= i-1) {
                        arr.get(arr.size()-1)[1] = Math.max(j-1, arr.get(arr.size()-1)[1]);
                    } else {
                        arr.add(new int[]{i, j-1});
                    }
                    break;
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        int j = 0;
        for(int i = 0; i < input.length(); i++) {
            if(j < arr.size() && i == arr.get(j)[0]) sb.append("<b>");
            sb.append(input.charAt(i));
            if(j < arr.size() && i == arr.get(j)[1]) {
                sb.append("</b>");
                j++;
            }
        }
        return sb.toString();
    }
```
