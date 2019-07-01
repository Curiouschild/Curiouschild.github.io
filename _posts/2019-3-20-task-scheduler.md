---
title:  "621. Task Scheduler"
date:   2019-3-20 12:00:00 +0930
categories: Leetcode
tags: PriorityQueue Others
---

[{{page.title}}](https://leetcode.com/problems/task-scheduler/){:target="_blank"}

    Given a char array representing tasks CPU need to do. It contains capital letters A to Z
     where different letters represent different tasks. Tasks could be done without original
     order. Each task could be done in one interval. For each interval, CPU could finish one
     task or just be idle.

    However, there is a non-negative cooling interval n that means between two same tasks,
    there must be at least n intervals that CPU are doing different tasks or just be idle.

    You need to return the least number of intervals the CPU will take to finish all the
    given tasks.



    Example:

    Input: tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8
    Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

The result only related to the frequency of each character.

* PriorityQueue with Node help class

The Node class can be removed in the next solution.

```java

public int leastInterval(char[] tasks, int n) {
    PriorityQueue<Node> q = new PriorityQueue<>(new Comparator<Node>(){
        public int compare(Node x, Node y) {
            return Integer.compare(y.cnt, x.cnt);
        }
    });

    int[] cnts = new int[26];

    for(char c : tasks) cnts[c - 'A']++;
    for(int i = 0; i < cnts.length; i++)
        if(cnts[i] > 0)
            q.offer(new Node((char)(i+'A'), cnts[i]));

    int result = 0;
    while(true) {
        int intervals = 0;
        int size = q.size();
        LinkedList<Node> temp = new LinkedList<>();
        while(intervals < size && intervals < n+1) {
            Node curr = q.poll();
            intervals++;
            if(curr.cnt > 1) {
                curr.cnt--;
                temp.add(curr);
            }
        }
        for(Node node : temp) q.offer(node);
        result += q.isEmpty() ? size : n + 1;
        intervals = 0;
        if(q.isEmpty()) break;


    }
    return result;

}

class Node {
    char c;
    int cnt;
    public Node(char c, int cnt) {this.c = c; this.cnt = cnt;}
}
```

* PriorityQueue

```java
public int leastInterval(char[] tasks, int n) {
    PriorityQueue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());
    int[] cnts = new int[26];
    for(char c : tasks) cnts[c - 'A']++;
    for(int i = 0; i < cnts.length; i++)
        if(cnts[i] > 0) q.offer(cnts[i]);
    int result = 0;
    while(true) {
        int intervals = 0;
        int size = q.size();
        LinkedList<Integer> temp = new LinkedList<>();
        while(intervals < size && intervals < n+1) {
            int curr = q.poll();
            intervals++;
            if(curr > 1) temp.add(curr-1);
        }
        for(int num : temp) q.offer(num);
        result += q.isEmpty() ? size : n + 1;
        intervals = 0;
        if(q.isEmpty()) break;
    }
    return result;
}

```

* Sort Array

```java
public int leastInterval(char[] tasks, int n) {
    int[] cnts = new int[26];
    for(char c : tasks) cnts[c - 'A']++;
    int intervals = 0, result = 0;
    Arrays.sort(cnts);
    while(true) {
        for(int i = 25; i >=0; i--) {
            if(cnts[i] > 0) {
                cnts[i]--;
                intervals++;
            }
            if(intervals == n+1) break;
        }
        Arrays.sort(cnts);
        if(cnts[25] == 0) {
            result += intervals;
            break;
        } else
            result += n+1;
        intervals = 0;
    }
    return result;
}
```

* Hard to understand

```java
public int leastInterval(char[] tasks, int n) {
    Integer[] arr = new Integer[26];
    Arrays.fill(arr, 0);
    for(char c : tasks) arr[c -'A']++;
    Arrays.sort(arr);
    int longest = arr[25] - 1;
    int idle = longest * n;
    for(int i = 24; i >= 0 && arr[i] > 0; i--) {
        idle -= Math.min(longest, arr[i]);
    }
    // idle may be negative if there are many types of tasks with a short window
    return idle > 0 ? idle + tasks.length : tasks.length;
}
```
