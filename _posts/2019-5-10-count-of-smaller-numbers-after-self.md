---
title:  "315. Count of Smaller Numbers After Self"
date:   2019-05-10 13:00:00 +0930
categories: Leetcode
tags: Hard MergeSort
---

[{{page.title}}](https://leetcode.com/problems/count-of-smaller-numbers-after-self/){:target="_blank"}

* MergeSort

```java
public List<Integer> countSmaller(int[] nums) {
    ArrayList<Integer> result = new ArrayList<>();
    int[][] arr = new int[nums.length][2];
    for(int i = 0; i < nums.length; i++) {
        arr[i][0] = nums[i];
        arr[i][1] = i;
    }
    int[] buffer = new int[nums.length];
    split(arr, buffer, 0, nums.length-1);
    for(int i = 0; i < buffer.length; i++) result.add(buffer[i]);
    return result;
}

public void split(int[][] nums, int[] result, int start, int end) {
    if(start >= end) return;
    int mid = start + (end-start) / 2;
    split(nums, result, start, mid);
    split(nums, result, mid+1, end);
    int l = start, r = mid+1, p = 0;
    int[][] temp = new int[end-start+1][];
    while(l <= mid && r <= end) {
        if(nums[l][0] <= nums[r][0]) { // pop left when equals
            result[nums[l][1]] += r-mid-1;
            temp[p++] = nums[l++];
        } else {
            temp[p++] = nums[r++];
        }
    }
    while(l <= mid) {
        result[nums[l][1]] += r-mid-1;
        temp[p++] = nums[l++];
    }
    while(r <= end) temp[p++] = nums[r++];
    System.arraycopy(temp, 0, nums, start, temp.length);
}
```
