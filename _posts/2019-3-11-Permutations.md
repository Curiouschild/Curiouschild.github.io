---
title:  "46. Permutations"
date:   2019-3-11 13:39:31 +0930
categories: Leetcode
tags: Permutation Recursive
---

[{{page.title}}](https://leetcode.com/problems/permutations/){:target="_blank"}

    Given a collection of distinct integers, return all possible permutations.

    Example:

    Input: [1,2,3]
    Output:
    [
    [1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,1,2],
    [3,2,1]
    ]


* Recursive (Swap)(Modify the original array)

```java
public List<List<Integer>> permute(int[] nums) {
    List<List<Integer>> result = new ArrayList<>();
    backtrack(nums, 0, result, new ArrayList<Integer>());
    return result;
}

public void backtrack(int[] nums, int start, List<List<Integer>> result, ArrayList<Integer> temp) {
    if(start == nums.length) {
        result.add(new ArrayList<Integer>(temp));
    }
    for(int i = start; i < nums.length; i++) {
        swap(nums, i, start);
        temp.add(nums[start]);
        backtrack(nums, start + 1, result, temp);
        temp.remove(temp.size()-1);
        swap(nums, i, start);
    }
}

public void swap(int[] nums, int i, int j) {
    int temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
}
```

* Recursive (Visited Memorisation)

```java
public List<List<Integer>> permute(int[] nums) {
    List<List<Integer>> result = new ArrayList<>();
    backtrack(nums, 0, result, new ArrayList<Integer>(), new boolean[nums.length]);
    return result;
}

public void backtrack(int[] nums, int start, List<List<Integer>> result, ArrayList<Integer> temp, boolean[] visited) {
    if(temp.size() == nums.length) {
        result.add(new ArrayList<Integer>(temp));
    }
    for(int i = 0; i < nums.length; i++) {
        if(visited[i]) continue;
        visited[i] = true;
        temp.add(nums[i]);
        backtrack(nums, 0, result, temp, visited);
        temp.remove(temp.size()-1);
        visited[i] = false;
    }
}
```
