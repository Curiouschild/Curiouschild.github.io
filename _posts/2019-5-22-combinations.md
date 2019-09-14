---
title:  "77. Combinations"
date:   2019-05-22 13:00:00 +0930
categories: Leetcode
tags: Medium HashMap
---

[{{page.title}}](https://leetcode.com/problems/combinations/){:target="_blank"}

    Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

    Example:

    Input: n = 4, k = 2
    Output:
    [
      [2,4],
      [3,4],
      [2,3],
      [1,2],
      [1,3],
      [1,4],
    ]

* Easy

```java
public List<List<Integer>> combine(int n, int k) {
     List<List<Integer>> result = new ArrayList<>();
     backtrack(n, k, new ArrayList<Integer>(), result, 1);
     return result;
 }

 public void backtrack(int n, int k, ArrayList<Integer> temp, List<List<Integer>> result, int start) {
     if(temp.size() == k) {
         result.add(new ArrayList<>(temp));
         return;
     }
     for(int i = start; i <= n; i++) {
         temp.add(i);
         backtrack(n, k, temp, result, i+1);
         temp.remove(temp.size()-1);
     }
 }
```
