---
title:  "912. Sort an Array"
date:   2019-3-12 18:00:21 +0930
categories: Leetcode
tags: Sort Array
---

[{{page.title}}](https://leetcode.com/problems/sort-an-array/){:target="_blank"}

    Given an array of integers nums, sort the array in ascending order.

![Example1](/img/posts/sort_an_array.png)


* BubbleSort

```java
public int[] bubbleSort(int[] nums) {
    for(int i = 0; i < nums.length; i++) {
        for(int j = 0; j < nums.length - 1 - i; j++) {
            if(nums[j] > nums[j+1]) swap(nums, j, j+1);
        }
    }
    return nums;
}
```

* SelectSort

```java
public int[] selectSort(int[] nums) {
    for(int i = 0; i < nums.length; i++) {
        int maxIndex = 0, max = Integer.MIN_VALUE;
        for(int j = 0; j < nums.length - i; j++) {
            if(max < nums[j]) {
                max = nums[j];
                maxIndex = j;
            }
        }
        swap(nums, nums.length - 1 - i, maxIndex);
    }
    return nums;
}
```

* InsertSort

```java
public int[] insertSort(int[] nums) {
    for(int i = 1; i < nums.length; i++) {
        int j = i;
        while(j-1 >= 0 && nums[j-1] > nums[j]) {
            swap(nums, j, j-1);
            j--;
        }
    }
    return nums;
}
```

* MergeSort

```java
public int[] mergeSort(int[] nums) {
    mergeSort(nums, 0, nums.length-1);
    return nums;
}

public void mergeSort(int[] nums, int start, int end) {
    if(start >= end) return;
    int mid = start + (end - start) / 2;
    mergeSort(nums, start, mid);
    mergeSort(nums, mid+1, end);
    int[] temp = new int[end - start + 1];
    int p = start, q = mid+1, i = 0;
    while(p <= mid && q <= end)
        temp[i++] = nums[p] < nums[q] ? nums[p++] : nums[q++];
    while(p <= mid) temp[i++] = nums[p++];
    while(q <= end) temp[i++] = nums[q++];
    System.arraycopy(temp, 0, nums, start, end - start + 1);
}
```

* QuickSort

```java
public void quickSort(int[] nums, int start, int end) {
    if(start >= end) return;
    int l = start + 1, r = end;
    while(l <= r) {
        if(nums[l] > nums[start])
            swap(nums, l--, r--);
        l++;
    }
    l--;
    swap(nums, l, start);
    quickSort(nums, start, l-1);
    quickSort(nums, l+1, end);
}
```

* HeapSort

```java
public int[] heapSort(int[] nums) {
    for(int i = nums.length-1; i >= 0; i--) {
        maxHeapify(nums, i, nums.length-1);
    }
    System.out.println(Arrays.toString(nums));

    int end = nums.length-1;
    while(end >= 0) {
        swap(nums, 0, end--);
        for(int i = 0; i <= end; i++) {
            maxHeapify(nums, i, end);
        }
    }
    return nums;
}

public void maxHeapify(int[] nums, int i, int limit) {
        int l = 2 * i + 1, r = 2 * i + 2;
        int maxIndex = i;
        if(l <= limit) maxIndex = nums[l] > nums[maxIndex] ? l : maxIndex;
        if(r <= limit) maxIndex = nums[r] > nums[maxIndex] ? r : maxIndex;
        if(maxIndex != i) {
            swap(nums, i, maxIndex);
            maxHeapify(nums, maxIndex, limit);
        }
}
```
