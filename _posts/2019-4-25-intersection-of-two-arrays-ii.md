---
title:  "350. Intersection of Two Arrays II"
date:   2019-4-25 21:12:00 +0930
categories: Leetcode
tags: HashMap Easy
---

[{{page.title}}](https://leetcode.com/problems/intersection-of-two-arrays-ii/){:target="_blank"}

    Given two arrays, write a function to compute their intersection.

    Example 1:

    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2,2]

    Example 2:

    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [4,9]

    Note:

        Each element in the result should appear as many times as it shows in both arrays.
        The result can be in any order.

    Follow up:

        What if the given array is already sorted? How would you optimize your algorithm?
        What if nums1's size is small compared to nums2's size? Which algorithm is better?
        What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

* Sort

```java
public int[] intersect(int[] nums1, int[] nums2) {
    Arrays.sort(nums1);
    Arrays.sort(nums2);
    int x = 0, y = 0;
    ArrayList<Integer> arr = new ArrayList<>();
    while(x < nums1.length && y < nums2.length) {
        if(nums1[x] < nums2[y]) x++;
        else if(nums1[x] > nums2[y]) y++;
        else {
            arr.add(nums1[x]);
            x++;
            y++;
        }
    }
    int[] result = new int[arr.size()];
    for(int i = 0; i < result.length; i++) result[i] = arr.get(i);
    return result;
}
```

* HashMap

```java

public int[] intersect(int[] nums1, int[] nums2) {
    HashMap<Integer, Integer> map = new HashMap<>();
    ArrayList<Integer> result = new ArrayList<>();
    for(int i : nums1) map.put(i, map.getOrDefault(i, 0)+1);
    for(int i : nums2) {
        if(map.containsKey(i)) {
            result.add(i);
            if(map.get(i) == 1) map.remove(i);
            else map.put(i, map.get(i)-1);
        }
    }
    int[] arr = new int[result.size()];
    for(int i = 0; i < arr.length; i++) arr[i] = result.get(i);
    return arr;
}
```
