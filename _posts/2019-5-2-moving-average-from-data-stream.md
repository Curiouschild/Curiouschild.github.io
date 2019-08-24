---
title:  "346. Moving Average from Data Stream"
date:   2019-05-02 13:53:00 +0930
categories: Leetcode
tags: Easy Array Queue
---

[{{page.title}}](https://leetcode.com/problems/moving-average-from-data-stream/){:target="_blank"}

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3



* array or queue

```java
class MovingAverage {
    int[] arr;
    int p;
    int sum;
    int cnt;
    /** Initialize your data structure here. */
    public MovingAverage(int size) {
        arr = new int[size];
    }

    public double next(int val) {

        if(cnt < arr.length) {
            sum += val;
            arr[cnt++] = val;
            return sum / (double) cnt;
        } else {
            int removed = arr[p];
            arr[p++] = val;
            if(p == arr.length) p = 0;
            sum -= removed;
            sum += val;
            return sum / (double) arr.length;
        }
    }
}
```
