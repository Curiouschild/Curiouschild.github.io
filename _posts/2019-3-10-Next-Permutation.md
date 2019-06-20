---
title:  "31. Next Permutation"
date:   2019-3-10 17:57:30 +0930
categories: Leetcode
tags: Array Permutation
---

[{{page.title}}](https://leetcode.com/problems/next-permutation/){:target="_blank"}

    Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

    If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

    The replacement must be in-place and use only constant extra memory.

    Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1

```java
public void nextPermutation(int[] nums) {
    for(int i = nums.length - 2; i >= 0 && i+1 < nums.length; i--) {
        if(nums[i+1] > nums[i]) {
            int p = i+1;
            while(p+1 < nums.length && nums[p+1] > nums[i])
                p++;
            swap(nums, p, i);
            Arrays.sort(nums, i+1, nums.length);
            return;
        }
    }
    Arrays.sort(nums);
    return;

}
public void swap(int[] nums, int i, int j) {
    int temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
}
```

![Example1](/img/posts/next_permutation.png)
