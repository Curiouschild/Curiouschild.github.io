---
title:  "40. Combination Sum II"
date:   2019-05-12 23x:07:00 +0930
categories: Leetcode
tags: Medium Backtrack
---

[{{page.title}}](https://leetcode.com/problems/minimum-index-sum-of-two-lists/){:target="_blank"}


    Given a collection of candidate numbers (candidates) and a target number (target), find all unique
    combinations in candidates where the candidate numbers sums to target.

    Each number in candidates may only be used once in the combination.

    Note:

        All numbers (including target) will be positive integers.
        The solution set must not contain duplicate combinations.

    Example 1:

    Input: candidates = [10,1,2,7,6,1,5], target = 8,
    A solution set is:
    [
      [1, 7],
      [1, 2, 5],
      [2, 6],
      [1, 1, 6]
    ]

    Example 2:

    Input: candidates = [2,5,2,1,2], target = 5,
    A solution set is:
    [
      [1,2,2],
      [5]
    ]




* HashMap

```java

public List<List<Integer>> combinationSum2(int[] candidates, int target) {
    Arrays.sort(candidates);
    List<List<Integer>> result = new ArrayList<>();
    backtrack(result, candidates, new ArrayList<Integer>(), target, 0, 0);
    return result;
}

public void backtrack(List<List<Integer>> result, int[] candidates, ArrayList<Integer> temp, int target, int sum, int start) {

    if(sum >= target) {
        if(sum == target) result.add(new ArrayList<>(temp));
        return;
    }
    for(int i = start; i < candidates.length; i++) {
        if(i > start && candidates[i] == candidates[i-1]) continue;
        temp.add(candidates[i]);
        backtrack(result, candidates, temp, target, sum+candidates[i], i+1);
        temp.remove(temp.size()-1);
    }
}
```
