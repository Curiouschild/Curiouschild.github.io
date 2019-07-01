---
title:  "347. Top K Frequent Elements"
date:   2019-3-20 12:00:00 +0930
categories: Leetcode
tags: PriorityQueue
---

[{{page.title}}](https://leetcode.com/problems/top-k-frequent-elements/){:target="_blank"}

    Given a non-empty array of integers, return the k most frequent elements.

    Example 1:

    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

    Example 2:

    Input: nums = [1], k = 1
    Output: [1]

    Note:

        You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
        Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


```java

public List<Integer> topKFrequent(int[] nums, int k) {
    HashMap<Integer, Integer> map = new HashMap<>();
    for(int i : nums) {
        int v = map.getOrDefault(i, 0);
        map.put(i, v+1);
    }
    PriorityQueue<Integer> q = new PriorityQueue<>((x,y) -> Integer.compare(map.get(x), map.get(y)));

    for(int key : map.keySet()) {
        if(q.size() < k) q.offer(key);
        else if(map.get(q.peek()) < map.get(key)) {
            q.poll();
            q.offer(key);
        }
    }
    return new ArrayList<>(q);
}
```
