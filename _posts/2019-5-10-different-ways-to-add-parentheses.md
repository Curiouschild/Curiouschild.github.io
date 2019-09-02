---
title:  "241. Different Ways to Add Parentheses"
date:   2019-05-10 16:39:00 +0930
categories: Leetcode
tags: Medium DynamicProgramming Recursive
---

[{{page.title}}](https://leetcode.com/problems/different-ways-to-add-parentheses/){:target="_blank"}

    Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

    Example 1:

    Input: "2-1-1"
    Output: [0, 2]
    Explanation:
    ((2-1)-1) = 0
    (2-(1-1)) = 2

    Example 2:

    Input: "2*3-4*5"
    Output: [-34, -14, -10, -10, 10]
    Explanation:
    (2*(3-(4*5))) = -34
    ((2*3)-(4*5)) = -14
    ((2*(3-4))*5) = -10
    (2*((3-4)*5)) = -10
    (((2*3)-4)*5) = 10


* Bottom Up
```java
public List<Integer> diffWaysToComputeBottomUp(String input) {
    ArrayList<Integer> result = new ArrayList<>();
    ArrayList<Integer> nums = new ArrayList<>();
    ArrayList<Character> ops = new ArrayList<>();
    int num = 0;
    for(char c : input.toCharArray()) {
        if(Character.isDigit(c)) {
            num = num * 10 + (c-'0');
        } else {
            nums.add(num);
            ops.add(c);
            num = 0;
        }
    }
    nums.add(num);
    ArrayList<Integer>[][] dp = new ArrayList[nums.size()][nums.size()];
    for(int i = 0; i < dp.length; i++) {
        dp[i][i] = new ArrayList<>();
        dp[i][i].add(nums.get(i));
    }
    for(int w = 2; w <= dp.length; w++) {
        for(int i = 0; i + w - 1 < dp.length; i++) {
            int r = i + w - 1;
            dp[i][r] = new ArrayList<>();
            for(int j = i; j < i + w - 1; j++) {
                ArrayList<Integer> left = dp[i][j], right = dp[j+1][r];
                char o = ops.get(j);
                for(int ln : left) {
                    for(int rn : right) {
                        if(o == '+') dp[i][r].add(ln + rn);
                        else if(o == '-') dp[i][r].add(ln - rn);
                        else dp[i][r].add(ln * rn);
                    }
                }
            }
        }
    }
    return dp[0][dp.length-1];
}
```

* Recursion

```java
public List<Integer> diffWaysToCompute(String input) {
    List<Integer> result = new ArrayList<>();
    boolean isNumber = true;
    for(int i = 0; i < input.length(); i++) {
        if(!Character.isDigit(input.charAt(i))) {
            isNumber = false;
            // recursion
            List<Integer> left = diffWaysToCompute(input.substring(0, i));
            List<Integer> right = diffWaysToCompute(input.substring(i+1));
            for(int l : left) {
                for(int r : right) {
                    if(input.charAt(i) == '+') result.add(l + r);
                    else if(input.charAt(i) == '-') result.add(l - r);
                    else result.add(l * r);
                }
            }
        }
    }
    if(isNumber) result.add(Integer.valueOf(input));
    return result;
}
```
