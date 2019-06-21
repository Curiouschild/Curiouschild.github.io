---
title:  "215. Kth Largest Element in an Array"
date:   2019-3-11 15:29:21 +0930
categories: Leetcode
tags: Matrix
---

[{{page.title}}](https://leetcode.com/problems/kth-largest-element-in-an-array/){:target="_blank"}

    Find the kth largest element in an unsorted array. Note that it is the kth largest
    element in the sorted order, not the kth distinct element.

    Example 1:

    Input: [3,2,1,5,6,4] and k = 2
    Output: 5

    Example 2:

    Input: [3,2,3,1,2,4,5,5,6] and k = 4
    Output: 4

* PriorityQueue

```java
public int findKthLargestPriorityQueue(int[] nums, int k) {
    PriorityQueue<Integer> q = new PriorityQueue<>();
    for(int i : nums) {
        if(q.size() < k) q.offer(i);
        else {
            if(q.peek() < i) {
                q.poll();
                q.offer(i);
            }
        }
    }
    return q.peek();
}
```

* Quick Select Iterative

```java

public int findKthLargestIterative(int[] nums, int k) {
    k = nums.length - k; // now k is the index of target element in a sorted array
    int l = 0, r = nums.length - 1;
    while(l <= r) {
        int p = l + 1, q = r;
        while(p <= q) {
            if(nums[p] > nums[l])
                swap(nums, p--, q--);
            p++;
        }
        p--; // p is first element larger than pivot, it is not the index in a sorted array becasue there may be other elements on the right side less than it (it is not the least largest element of pivot).
        swap(nums, p, l);
        // <=pivot <-- p(==pivot) --> >pivot
        // now nums[p] is the pivot and all elemets on the left side of p are <= nums[p], so p is the index of value nums[p] in a sorted array
        // In a word, nums[p] is the least largest element in terms of elements from 0 to p-1
        if(p < k) {
            l = p + 1;
        } else if(p > k) {
            r = p - 1;
        } else {
            return nums[k];
        }
    }
    return -1;
}

```

* QuickSelect recursive

```java
public int quickSelect(int[] nums, int k, int l, int r) {
    if(l == r) return nums[l];
    int p = l + 1, q = r;
    while(p <= q) {
        if(nums[p] > nums[l])
            swap(nums, p--, q--);
        p++;
    }
    p--;
    swap(nums, l, p);
    if(p < k) return quickSelect(nums, k, p+1, r);
    else if(p > k) return quickSelect(nums, k, l, p-1);
    else return nums[k];
}

public void swap(int[] nums, int i, int j) {
    int temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
}
```
