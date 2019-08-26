---
title:  "282. Expression Add Operators"
date:   2019-05-03 12:59:00 +0930
categories: Leetcode
tags: Hard String Backtrack
---

[{{page.title}}](https://leetcode.com/problems/expression-add-operators/){:target="_blank"}

    Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

    Example 1:

    Input: num = "123", target = 6
    Output: ["1+2+3", "1*2*3"]

    Example 2:

    Input: num = "232", target = 8
    Output: ["2*3+2", "2+3*2"]

* Brutal force

```java
public class Solution {

    public List<String> addOperators(String num, int target) {
        List<String> result = new ArrayList<>();
        calculate(result, num, "", target, 0, 0, 0);
        return result;
    }

    public void calculate(List<String> result, String s, String path, int target, long value, int start, long multi) {
        if(start == s.length() && value == target) {
            result.add(path);
        }
        for(int i = start; i < s.length(); i++) {
            if(i > start && s.charAt(start) == '0') return;
            Long curr = Long.valueOf(s.substring(start, i+1));
            if(start == 0) {
                calculate(result, s, path + curr, target, curr, i+1, curr);
            } else {
                calculate(result, s, path + "+" + curr, target, value+curr, i+1, curr);
                calculate(result, s, path + "-" + curr, target, value-curr, i+1, -curr);
                calculate(result, s, path + "*" + curr, target, value-multi+curr*multi, i+1, curr*multi);
            }
        }
    }
  }
```
