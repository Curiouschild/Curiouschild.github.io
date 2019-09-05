---
title:  "216. Combination Sum III"
date:   2019-05-12 23:22:00 +0930
categories: Leetcode
tags: Medium Backtrack
---

[{{page.title}}](https://leetcode.com/problems/combination-sum-iii/){:target="_blank"}

    Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9
    can be used and each combination should be a unique set of numbers.

    Note:

        All numbers will be positive integers.
        The solution set must not contain duplicate combinations.

    Example 1:

    Input: k = 3, n = 7
    Output: [[1,2,4]]

    Example 2:

    Input: k = 3, n = 9
    Output: [[1,2,6], [1,3,5], [2,3,4]]



```java

public List<List<Integer>> combinationSum3(int k, int n) {
    List<List<Integer>> result = new ArrayList<>();
    backtrack(k, n, result, new ArrayList<Integer>(), 1, 0);
    return result;
}

public void backtrack(int k, int n, List<List<Integer>> result, ArrayList<Integer> temp, int curr, int sum) {
    if(temp.size() > k) return;
    if(sum >= n) {
        if(sum == n && temp.size() == k) result.add(new ArrayList<>(temp));
        return;
    }
    for(int i = curr; i < 10; i++) {
        temp.add(i);
        backtrack(k, n, result, temp, i+1, sum+i);
        temp.remove(temp.size()-1);
    }
}
```
