---
title:  "39. Combination Sum"
date:   2019-3-27 17:41:00 +0930
categories: Leetcode
tags: Recursion
---

[{{page.title}}](https://leetcode.com/problems/combination-sum/){:target="_blank"}

    Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
    find all unique combinations in candidates where the candidate numbers sums to target.

    The same repeated number may be chosen from candidates unlimited number of times.

    Note:

        All numbers (including target) will be positive integers.
        The solution set must not contain duplicate combinations.

    Example 1:

    Input: candidates = [2,3,6,7], target = 7,
    A solution set is:
    [
      [7],
      [2,2,3]
    ]


```java
public List<List<Integer>> combinationSum(int[] candidates, int target) {
    List<List<Integer>> result = new ArrayList<>();
    backtrack(0, target, candidates, 0, new ArrayList<Integer>(), result);
    return result;

}

public void backtrack(int curr, int target, int[] candidates, int index, ArrayList<Integer> temp, List<List<Integer>> result) {
    if(curr >= target) {
        if(curr == target) result.add(new ArrayList(temp));
        return;
    }
    for(int i = index; i < candidates.length; i++) {
        temp.add(candidates[i]);
        backtrack(curr + candidates[i], target, candidates, i, temp, result);
        temp.remove(temp.size()-1);
    }
}
```
