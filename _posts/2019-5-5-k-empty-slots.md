---
title:  "683. K Empty Slots"
date:   2019-05-05 10:25:00 +0930
categories: Leetcode
tags: Hard TreeMap
---

[{{page.title}}](https://leetcode.com/problems/k-empty-slots/){:target="_blank"}

    You have N bulbs in a row numbered from 1 to N. Initially, all the bulbs are turned off. We turn on exactly one bulb everyday until all bulbs are on after N days.

    You are given an array bulbs of length N where bulbs[i] = x means that on the (i+1)th day, we will turn on the bulb at position x where i is 0-indexed and x is 1-indexed.

    Given an integer K, find out the minimum day number such that there exists two turned on bulbs that have exactly K bulbs between them that are all turned off.

    If there isn't such day, return -1.



    Example 1:

    Input:
    bulbs: [1,3,2]
    K: 1
    Output: 2
    Explanation:
    On the first day: bulbs[0] = 1, first bulb is turned on: [1,0,0]
    On the second day: bulbs[1] = 3, third bulb is turned on: [1,0,1]
    On the third day: bulbs[2] = 2, second bulb is turned on: [1,1,1]
    We return 2 because on the second day, there were two on bulbs with one off bulb between them.


* Sliding Window: jump on fail and success

```java
public int kEmptySlots(int[] bulbs, int K) {
    if(bulbs.length-2 < K) return -1;
    int[] days = new int[bulbs.length+1];
    for(int i = 0; i < bulbs.length; i++) days[bulbs[i]] = i+1;
    int l = 1, r = 2;
    int result = bulbs.length+1;
    while(r < days.length && l+K+1 < days.length) {
        if(r-l-1 == K) {
            result = Math.min(result, Math.max(days[l], days[r]));
            l = r;
        } else if(days[r] < days[l] || days[r] < days[l+K+1]) {
            l = r;
        }
        r++;
    }
    return result == bulbs.length+1 ? -1 : result;
}
```

* Deque sliding window

```java
public int kEmptySlots(int[] bulbs, int K) {
    if(bulbs.length-2 < K) return -1;
    Deque<Integer> q = new ArrayDeque<>();
    int[] days = new int[bulbs.length+1];
    for(int i = 0; i < bulbs.length; i++) days[bulbs[i]] = i+1;
    for(int i = 2; i < 2+K; i++) {
        while(!q.isEmpty() && days[i] < q.peekLast()) q.pollLast();
        q.offerLast(days[i]);
    }
    int result = bulbs.length+1;
    for(int i = 2+K; i <= bulbs.length; i++) {
        int earliest = q.isEmpty() ? bulbs.length+1 : q.peekFirst();
        if(earliest > days[i] && earliest > days[i-K-1])
            result = Math.min(result, Math.max(days[i], days[i-K-1]));
        if(!q.isEmpty()) {
            if(q.peekFirst() == days[i-K]) q.pollFirst();
            while(!q.isEmpty() && days[i] < q.peekLast()) q.pollLast();
            q.offerLast(days[i]);
        }
    }
    return result == bulbs.length+1 ? -1 : result;
}
```

* PriorityQueue

```java
public int kEmptySlotsPriorityQueue(int[] bulbs, int K) {
    if(bulbs.length - 2 < K) return -1;
    PriorityQueue<Integer> q = new PriorityQueue<>();
    int[] days = new int[bulbs.length+1];
    for(int i = 0; i < bulbs.length; i++) days[bulbs[i]] = i+1;
    for(int i = 2; i-2 < K; i++)
        q.offer(days[i]);
    int result = bulbs.length+1;
    for(int i = K+2; i < days.length; i++) {
        int earliest = q.isEmpty() ? bulbs.length + 1 : q.peek(); // k == 0 ?
        int l = i-K-1;
        if(earliest > days[l] && earliest > days[i])
            result = Math.min(result, Math.max(days[l], days[i]));
        if(!q.isEmpty()) { // K > 0
            q.remove(days[l+1]);
            q.offer(days[i]);
        }
    }
    return result == bulbs.length+1 ? -1 : result;
}
```

* Easy

```java
public int kEmptySlots(int[] bulbs, int K) {
    TreeMap<Integer, Integer> map = new TreeMap<>();
    for(int b : bulbs) {
        Integer low = map.floorKey(b);
        Integer high = map.ceilingKey(b);
        if(low == null) low = b;
        if(high == null) high = b;
        if(b - low - 1 == K || high - b - 1 == K) return map.size()+1;
        map.put(b,0);
    }
    return -1;
}
```
