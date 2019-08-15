---
title:  "128. Longest Consecutive Sequence"
date:   2019-4-19 21:30:00 +0930
categories: Leetcode
tags: HashSet
---

[{{page.title}}](https://leetcode.com/problems/longest-consecutive-sequence/){:target="_blank"}

    Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

    Your algorithm should run in O(n) complexity.

    Example:

    Input: [100, 4, 200, 1, 3, 2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.



```java
public int longestConsecutive(int[] num) {
    HashMap<Integer,Integer> map = new HashMap<>();
    HashSet<Integer> set = new HashSet<>();
    for(int i : num) set.add(i);
    int result = 0;
    for(int i : num) {
        if(set.contains(i)) {
            int cnt = 0, curr = i;
            while(set.contains(curr)) {
                set.remove(curr++);
                cnt++;
            }
            if(map.containsKey(curr)) cnt += map.get(curr);
            map.put(i, cnt);
            result = Math.max(result, cnt);
        }
    }
    return result;
}
```

* A smarter version
```java
public int longestConsecutive2(int[] num) {
    HashSet<Integer> set = new HashSet<>();
    int ans = 0;
    for(int n : num) set.add(n);
    for(int n : set) {
        if(!set.contains(n-1)) {
            int curr = n;
            int cnt  = 1;
            while(set.contains(curr+1)) {
                curr++;
                cnt++;
            }
            ans = Math.max(ans, cnt);
        }
    }
    return ans;
}
```
