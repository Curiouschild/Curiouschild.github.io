---
title:  "163. Missing Ranges"
date:   2019-05-09 09:46:00 +0930
categories: Leetcode
tags: Medium Array
---

[{{page.title}}](https://leetcode.com/problems/missing-ranges/){:target="_blank"}

* A better solution, shrink lower boundary
```java
public List<String> findMissingRanges(int[] nums, int lower, int upper) {
     List<String> list = new ArrayList<String>();
     long l = lower;
     for(int n : nums){
         long justBelow = (long)n - 1;
         if(l == justBelow) list.add(l+"");
         else if(l < justBelow) list.add(l + "->" + justBelow);
         l = (long)n+1;
     }
     if(l == upper) list.add(l+"");
     else if(l < upper) list.add(l + "->" + upper);
     return list;
 }
 ```

* My Trival solution

```java
public List<String> findMissingRanges(int[] nums, int lower, int upper) {

    List<String> result = new ArrayList<>();
    int l = 0, r = nums.length;
    int start = 0, end = nums.length-1;
    while(start < nums.length && nums[start] < lower) start++;
    while(end >= 0 && nums[end] > upper) end--;
    if(start > end) {
        if(upper == lower) result.add("" + upper);
        else result.add(lower+"->"+upper);
        return result;
    }

    if((long)nums[start]-lower == 1) result.add(lower+"");
    else if((long)nums[start]-lower > 1) result.add(lower + "->" + ((long)nums[start]-1));

    for(int i = start; i < end; i++) {
        if((long)nums[i]+2 == nums[i+1]) {
            result.add(nums[i]+1+"");
        } else if((long)nums[i+1]-(long)nums[i] > 2) {
            result.add((long)nums[i]+1 + "->" + ((long)nums[i+1]-1));
        }
    }
    if(nums[end] == (long)upper-1) result.add(upper+"");
    else if(nums[end] < upper-1) result.add((long)nums[end]+1 + "->" + (upper));
    return result;
}
```
