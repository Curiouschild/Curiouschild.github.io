---
title:  "228. Summary Ranges"
date:   2019-06-02 09:55:00 +0930
categories: Leetcode
tags: Medium Interval
---

[{{page.title}}](https://leetcode.com/problems/summary-ranges/){:target="_blank"}

    Given a sorted integer array without duplicates, return the summary of its ranges.

    Example 1:

    Input:  [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]
    Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

    Example 2:

    Input:  [0,2,3,4,6,8,9]
    Output: ["0","2->4","6","8->9"]
    Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.


* One pass
  - easier than Medium
```java

public List<String> summaryRanges(int[] nums) {
    ArrayList<String> result = new ArrayList<>();
    if(nums.length == 0) return result;
    int start = nums[0], end = nums[0];
    for(int i = 0; i < nums.length; i++) {
        if(i+1 == nums.length || nums[i+1] != nums[i]+1) {
            if(start == end) result.add(""+start);
            else result.add(start + "->" + end);
            if(i+1 < nums.length) {
                start = nums[i+1];
                end = start;
            }
        } else {
            end = nums[i+1];
        }
    }
    return result;
}
```
