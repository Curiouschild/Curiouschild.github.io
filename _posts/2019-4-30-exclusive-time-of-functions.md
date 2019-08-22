---
title:  "636. Exclusive Time of Functions"
date:   2019-4-30 10:41:00 +0930
categories: Leetcode
tags: Medium Stack
---

[{{page.title}}](https://leetcode.com/problems/exclusive-time-of-functions/){:target="_blank"}


    On a single threaded CPU, we execute some functions.  Each function has a unique id between 0 and N-1.

    We store logs in timestamp order that describe when a function is entered or exited.

    Each log is a string with this format: "{function_id}:{"start" | "end"}:{timestamp}".  For example,
    "0:start:3" means the function with id 0 started at the beginning of timestamp 3.  "1:end:2" means the
    function with id 1 ended at the end of timestamp 2.

    A function's exclusive time is the number of units of time spent in this function.  Note that this does not
    include any recursive calls to child functions.

    The CPU is single threaded which means that only one function is being executed at a given time unit.

    Return the exclusive time of each function, sorted by their function id.

    Example 1:

![img1](/img/posts/exclusive-time-of-functions-1.png)

    Input:
    n = 2
    logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
    Output: [3, 4]
    Explanation:
    Function 0 starts at the beginning of time 0, then it executes 2 units of time and reaches the end of time
    1.
    Now function 1 starts at the beginning of time 2, executes 4 units of time and ends at time 5.
    Function 0 is running again at the beginning of time 6, and also ends at the end of time 6, thus executing
    for 1 unit of time.
    So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time
    executing.


* Optimzed Solution, use only one stack to record starting indexs

``` java
public int[] exclusiveTime(int n, List<String> logs) {
    ArrayDeque<Integer> starts = new ArrayDeque<>();
    int[] result = new int[n];
    int prev = 0;
    for(String s : logs) {
        String[] arr = s.split(":");
        int index = Integer.valueOf(arr[0]), time = Integer.valueOf(arr[2]);
        if(arr[1].equals("start")) { // start
            if(!starts.isEmpty())
                result[starts.peek()] += time - prev; // prev -> next_start (exclusive)
            starts.push(index);
            prev = time;
        } else {
            int start = starts.poll();
            result[start] += time - prev + 1; // prev -> end (inclusive)
            prev = time+1;
        }
    }
    return result;
}
```

* The first complex solution ... spend 50 minutes...

```java

public int[] exclusiveTime(int n, List<String> logs) {
    ArrayDeque<int[]> starts = new ArrayDeque<>(), ends = new ArrayDeque<>();
    int[] result = new int[n];
    for(String s : logs) {
        String[] arr = s.split(":");
        int index = Integer.valueOf(arr[0]), time = Integer.valueOf(arr[2]), status = arr[1].equals("start") ? 0 : 1;
        int[] log = new int[] {index, status, time};

        if(log[1] == 0) { // start
            if(!starts.isEmpty()) {
                int[] ongoing = starts.peek();
                int[] latest = (ends.isEmpty() || ongoing[2] > ends.peek()[2]) ? ongoing : ends.peek();
                result[ongoing[0]] += log[2] - latest[2] - (latest == ongoing ? 0 : 1);
            }
            starts.push(log);
        } else {
            int[] ongoing = starts.poll();
            int[] latest = (ends.isEmpty() || ongoing[2] > ends.peek()[2]) ? ongoing : ends.peek();
            result[log[0]] += log[2] - latest[2] + (latest == ongoing ? 1 : 0);
            ends.push(log);
        }
    }
    return result;
}
```
