---
title:  "229. Majority Element II"
date:   2019-06-03 12:00:00 +0930
categories: Leetcode
tags: Medium Math
---

[{{page.title}}](https://leetcode.com/problems/majority-element-ii/){:target="_blank"}

    Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

    Note: The algorithm should run in linear time and in O(1) space.

    Example 1:

    Input: [3,2,3]
    Output: [3]

    Example 2:

    Input: [1,1,1,3,3,2,2,2]
    Output: [1,2]

* Boyer-Moore Majority Vote algorithm
  - n1 and n2 are not necessarily the valid results
  - the second pass check their validity

```java

public List<Integer> majorityElement(int[] nums) {
    int cnt1 = 0, cnt2 = 0, n1 = 0, n2 = 0;
    for(int i : nums) {
        if(n1 == i) cnt1++;
        else if(n2 == i) cnt2++;
        else if(cnt1 == 0) {
            cnt1 = 1;
            n1 = i;
        } else if(cnt2 == 0) {
            cnt2 = 1;
            n2 = i;
        } else {
            cnt1--;
            cnt2--;
        }
    }
    cnt1 = 0;
    cnt2 = 0;
    for(int i : nums) {
        if(i == n1) cnt1++;
        if(i == n2) cnt2++;
    }
    List<Integer> result = new ArrayList<>();
    if(cnt1 > nums.length/3) result.add(n1);
    if(n1 != n2 && cnt2 > nums.length/3) result.add(n2);
    return result;
}
```
