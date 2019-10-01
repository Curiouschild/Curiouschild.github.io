---
title:  "228. Summary Ranges"
date:   2019-06-02 09:55:00 +0930
categories: Leetcode
tags: Medium Interval
---

[{{page.title}}](https://leetcode.com/problems/valid-triangle-number/){:target="_blank"}

    Given a sorted integer array without duplicates, return the summary of its ranges.

    Example 1:

    Input:  [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]
    Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

    Example 2:

    Input:  [0,2,3,4,6,8,9]
    Output: ["0","2->4","6","8->9"]
    Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.


* O(N^2)
  - key: after sort, if k is the smallest index to the right of j to let nums[i]+nums[j] <= nums[k] and
         nums[i]+nums[j] > nums[k-1]
         then nums[i] + nums[j+1] > nums[k-1]
         so for each inner loop, k will monotonically increase which reduce a level of loop for k

```java

public int triangleNumber(int[] nums) {
    Arrays.sort(nums);
    int result = 0, prev = -1;
    for(int i = 0; i < nums.length-2; i++) {
        if(nums[i] == 0) continue;
        int k = i+2; // define k out of inner loop
        for(int j = i+1; j < nums.length-1; j++) {
            while(k < nums.length && nums[k] < nums[i] + nums[j]) k++;
            result += k - j - 1;
        }
    }
    return result;
}
```

* simple binary search

```java

public int triangleNumberBinarySearch(int[] nums) {
    Arrays.sort(nums);
    int result = 0, prev = -1;
    for(int i = 0; i < nums.length-2; i++) {
        for(int j = i+1; j < nums.length-1; j++) {
            int target = nums[i] + nums[j];
            int index = search(nums, j+1, target);
            result += index - j - 1;
        }
    }
    return result;
}



public int search(int[] nums, int l, int target) {
    int r = nums.length;
    while(l < r) {
        int mid = l + (r-l) / 2;
        if(nums[mid] < target) {
            l = mid+1;
        } else {
            r = mid;
        }
    }
    return l;
}
```
