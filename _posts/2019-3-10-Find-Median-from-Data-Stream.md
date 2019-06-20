---
title:  "295. Find Median from Data Stream"
date:   2019-3-10 23:33:13 +0930
categories: Leetcode
tags: Heap DataStructure
---

[{{page.title}}](https://leetcode.com/problems/find-median-from-data-stream/){:target="_blank"}
    Median is the middle value in an ordered integer list. If the size of the list is even,
    there is no middle value. So the median is the mean of the two middle value.
    For example,

    [2,3,4], the median is 3

    [2,3], the median is (2 + 3) / 2 = 2.5

    Design a data structure that supports the following two operations:

        void addNum(int num) - Add a integer number from the data stream to the data structure.
        double findMedian() - Return the median of all elements so far.

    Example:

    addNum(1)
    addNum(2)
    findMedian() -> 1.5
    addNum(3)
    findMedian() -> 2


* min heap and max heap

The same with Shortest Edit Distance

```java
class MedianFinder {
    PriorityQueue<Integer> small, large;

    public MedianFinder() {
        large = new PriorityQueue<>(); //max heap store small values
        small = new PriorityQueue<Integer>(new Comparator<Integer>() { // min head store large values
            public int compare(Integer x, Integer y) { return Integer.compare(y, x); }
        });
    }

    public void addNum(int num) {
        if(small.size() < large.size())
            small.offer(large.poll());
        small.offer(num);
        large.offer(small.poll());
    }

    public double findMedian() {
        if(small.size() < large.size()) return large.peek();
        else return (large.peek() + small.peek()) / 2.0;
    }
}
```


    Follow up:

        If all integer numbers from the stream are between 0 and 100, how would you optimize it?
        If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

    Array from 0 to 100;
    Count and sum;
