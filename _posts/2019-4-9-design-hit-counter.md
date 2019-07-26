---
title:  "362. Design Hit Counter"
date:   2019-4-9 22:23:00 +0930
categories: Leetcode
tags: DataStructure TreeMap Queue Array
---

[{{page.title}}](https://leetcode.com/problems/design-hit-counter/){:target="_blank"}

    Design a hit counter which counts the number of hits received in the past 5 minutes.

    Each function accepts a timestamp parameter (in seconds granularity) and you may assume
    that calls are being made to the system in chronological order (ie, the timestamp is
    monotonically increasing). You may assume that the earliest timestamp starts at 1.

    It is possible that several hits arrive roughly at the same time.

    Example:

    HitCounter counter = new HitCounter();

    // hit at timestamp 1.
    counter.hit(1);

    // hit at timestamp 2.
    counter.hit(2);

    // hit at timestamp 3.
    counter.hit(3);

    // get hits at timestamp 4, should return 3.
    counter.getHits(4);

    // hit at timestamp 300.
    counter.hit(300);

    // get hits at timestamp 300, should return 4.
    counter.getHits(300);

    // get hits at timestamp 301, should return 3.
    counter.getHits(301);

    Follow up:
    What if the number of hits per second could be very large? Does your design scale?



* Two Array; Record the timestamps

```java
    private int[] times;
    private int[] hits;
    /** Initialize your data structure here. */
    public HitCounter() {
        times = new int[300];
        hits = new int[300];
    }

    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    public void hit(int timestamp) {
        int index = timestamp % 300;
        if (times[index] != timestamp) {
            times[index] = timestamp;
            hits[index] = 1;
        } else {
            hits[index]++;
        }
    }

    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    public int getHits(int timestamp) {
        int total = 0;
        for (int i = 0; i < 300; i++) {
            if (timestamp - times[i] < 300) {
                total += hits[i];
            }
        }
        return total;
    }
```


* Array; Record Max Timestamp; clear on every action

```java
public class HitCounter {
    int max;
    int[] hits;
    public HitCounter() {
        hits = new int[300];
    }

    public void hit(int timestamp) {
        for(int i = max + 1; i <= timestamp; i++)
            hits[i%300] = 0;
        hits[timestamp % 300]++;
        max = timestamp;
    }

    public int getHits(int timestamp) {
        int sum = 0;
        for(int i = max + 1; i <= timestamp; i++)
            hits[i%300] = 0;
        for(int i = 0; i < 300; i++)
            sum += hits[i];
        max = timestamp;
        return sum;
    }
}
```


* TreeMap

```java
class HitCounter {
    TreeMap<Integer, Integer> map = new TreeMap<>();
    /** Initialize your data structure here. */
    public HitCounter() {}

    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    public void hit(int timestamp) {
        int cnt = map.getOrDefault(timestamp, 0);
        map.put(timestamp, cnt+1);
    }

    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    public int getHits(int timestamp) {
        int ans = 0;
        for(Integer v : map.tailMap(timestamp - 299).values())
            ans += v;
        return ans;
    }
}
```

* Queue; Each hit as an element; Not scalable

```java
public class HitCounter {
        Queue<Integer> q = null;
        /** Initialize your data structure here. */
        public HitCounter() {
            q = new LinkedList<Integer>();
        }

        /** Record a hit.
            @param timestamp - The current timestamp (in seconds granularity). */
        public void hit(int timestamp) {
            q.offer(timestamp);
        }

        /** Return the number of hits in the past 5 minutes.
            @param timestamp - The current timestamp (in seconds granularity). */
        public int getHits(int timestamp) {
            while(!q.isEmpty() && timestamp - q.peek() >= 300) {
                q.poll();
            }
            return q.size();
        }
    }
```
