---
title:  "911. Online Election"
date:   2019-06-26 21:38:00 +0930
categories: Leetcode
tags: Medium binarySearch Design
---

[{{page.title}}](https://leetcode.com/problems/online-election/){:target="_blank"}

    In an election, the i-th vote was cast for persons[i] at time times[i].

    Now, we would like to implement the following query function: TopVotedCandidate.q(int t) will return the number of
    the person that was leading the election at time t.

    Votes cast at time t will count towards our query.  In the case of a tie, the most recent vote (among tied
    candidates) wins.

    Example 1:

    Input: ["TopVotedCandidate","q","q","q","q","q","q"],
    [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
    Output: [null,0,1,1,0,0,1]
    Explanation:
    At time 3, the votes are [0], and 0 is leading.
    At time 12, the votes are [0,1,1], and 1 is leading.
    At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
    This continues for 3 more queries at time 15, 24, and 8.

    Note:

        1 <= persons.length = times.length <= 5000
        0 <= persons[i] <= persons.length
        times is a strictly increasing array with all elements in [0, 10^9].
        TopVotedCandidate.q is called at most 10000 times per test case.
        TopVotedCandidate.q(int t) is always called with t >= times[0].


* preprocess and binary search

```java
class TopVotedCandidate {
    int[] result;
    int[] times;
    public TopVotedCandidate(int[] persons, int[] times) {
        this.times = times;
        result = new int[persons.length+1];
        HashMap<Integer, Integer> map = new HashMap<>();
        int max = -1, id = -1;
        for(int i = 0; i < times.length; i++) {
            int v = 1 + map.getOrDefault(persons[i], 0);
            map.put(persons[i], v);
            if(v >= max) {
                max = v;
                id = persons[i];
            }
            result[i] = id;
        }
    }
    class Person {
        int id;
        int cnt;
        int time;
        public Person(int id, int cnt, int time) {
            this.id = id;
            this.cnt = cnt;
            this.time = time;
        }
    }

    public int q(int t) {
        int i = Arrays.binarySearch(times, t);
        if(i < 0) {
            i = -i-2;
        }
        return result[i];
    }
}
```
