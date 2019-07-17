---
title:  "692. Top K Frequent Words"
date:   2019-4-3 15:45:00 +0930
categories: Leetcode
tags: PriorityQueue
---

[{{page.title}}](https://leetcode.com/problems/top-k-frequent-words/){:target="_blank"}

    Given a non-empty list of words, return the k most frequent elements.

    Your answer should be sorted by frequency from highest to lowest. If two words have
    the same frequency, then the word with the lower alphabetical order comes first.

    Example 1:

    Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
    Output: ["i", "love"]
    Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.


* Sorting

```java
public List<String> topKFrequentSort(String[] words, int k) {
    HashMap<String, Integer> map = new HashMap<>();
    for(String s : words) {
        if(!map.containsKey(s)) map.put(s, 0);
        map.put(s, map.get(s)+1);
    }
    ArrayList<Map.Entry<String,Integer>> arr = new ArrayList<>(map.entrySet());
    Collections.sort(arr, (x,y)->{
        int r = Integer.compare(y.getValue(), x.getValue());
        if(r == 0) return x.getKey().compareTo(y.getKey());
        return r;
    });
    ArrayList<String> result = new ArrayList<>();

    for(int i = 0; i < k; i++) result.add(arr.get(i).getKey());
    return result;
}
```

* PriorityQueue
```java
public List<String> topKFrequent(String[] words, int k) {
    HashMap<String, Integer> map = new HashMap<>();
    for(String s : words) {
        map.put(s, map.getOrDefault(s, 0)+1);
    }
    PriorityQueue<Map.Entry<String, Integer>> q = new PriorityQueue<>((x,y)->{
        int r = Integer.compare(x.getValue(), y.getValue());
        if(r == 0) return y.getKey().compareTo(x.getKey());
        return r;
    });

    for(Map.Entry<String, Integer> e : map.entrySet()) {
        if(q.size() < k) q.offer(e);
        else if(q.peek().getValue() < e.getValue() || q.peek().getValue() == e.getValue() && q.peek().getKey().compareTo(e.getKey()) > 0) {
            q.poll();
            q.offer(e);
        }
    }
    LinkedList<String> result = new LinkedList<>();
    while(!q.isEmpty()) {
        result.addFirst(q.poll().getKey());
    }
    return result;
}
```
