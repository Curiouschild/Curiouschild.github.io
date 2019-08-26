---
title:  "759. Employee Free Time"
date:   2019-05-03 22:30:00 +0930
categories: Leetcode
tags: Hard Interval
---

[{{page.title}}](https://leetcode.com/problems/employee-free-time/){:target="_blank"}

    We are given a list schedule of employees, which represents the working time for each employee.

    Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

    Return the list of finite intervals representing common, positive-length free time for all employees, also
    in sorted order.

    Example 1:

    Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
    Output: [[3,4]]
    Explanation:
    There are a total of three employees, and all common
    free time intervals would be [-inf, 1], [3, 4], [10, inf].
    We discard any intervals that contain inf as they aren't finite.



    Example 2:

    Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
    Output: [[5,6],[7,9]]



    (Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists
    or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not
    defined.)

    Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

    Note:

        schedule and schedule[i] are lists with lengths in range [1, 50].
        0 <= schedule[i].start < schedule[i].end <= 10^8.

    NOTE: input types have been changed on June 17, 2019. Please reset to default code definition to get new method signature.

* the comparator is kind of tricky, but building a linkedlist of intervals is also troublesome

The main logic is the same with Merge K sorted LinkedList

```java
class Solution {
    // merge intervals
    public List<Interval> employeeFreeTime(List<List<Interval>> schedule) {
        int[] ps = new int[schedule.size()]; // the pointers to the current head interval for every person
        ArrayList<Interval> arr = new ArrayList<>();
        PriorityQueue<Integer> q = new PriorityQueue<>((a,b)->(schedule.get(a).get(ps[a]).start - schedule.get(b).get(ps[b]).start));
        for(int i = 0; i < ps.length; i++) {
            q.offer(i);
        }
        arr.add(schedule.get(q.peek()).get(0));
        while(!q.isEmpty()) {
            int index = q.poll();
            Interval i = schedule.get(index).get(ps[index]), j = arr.get(arr.size()-1); // j.start <= i.start
            if(ps[index]+1 < schedule.get(index).size()) {
                ps[index]++;
                q.offer(index);
            }

            if(i.start <= j.end) { // merge
                j.end = Math.max(j.end, i.end);
            } else { // add new
                arr.add(i);
            }
        }
        ArrayList<Interval> result = new ArrayList<>();
        for(int i = 1; i < arr.size(); i++) {
            result.add(new Interval(arr.get(i-1).end, arr.get(i).start));
        }

        return result;
    }
}
```
