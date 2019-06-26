---
title:  "347. Top K Frequent Elements"
date:   2019-3-16 16:09:44 +0930
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
        PriorityQueue<Map.Entry<Integer, Integer>> q = new PriorityQueue<>(new Comparator<Map.Entry<Integer, Integer>>() {
            public int compare(Map.Entry<Integer, Integer> x, Map.Entry<Integer, Integer> y) {
                return Integer.compare(x.getValue(), y.getValue());
            }
        });
        for(Map.Entry<Integer, Integer> e : map.entrySet()) {
            if(q.size() < k) q.offer(e);
            else if(e.getValue() > q.peek().getValue()) {
                q.poll();
                q.offer(e);
            }
        }
        List<Integer> result = new ArrayList<Integer>();
        for(Map.Entry<Integer, Integer> e : q) result.add(e.getKey());
        return result;
    }
```
