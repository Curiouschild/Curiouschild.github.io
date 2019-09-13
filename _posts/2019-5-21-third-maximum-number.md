---
title:  "414. Third Maximum Number"
date:   2019-05-21 16:42:00 +0930
categories: Leetcode
tags: Easy Array
---

[{{page.title}}](https://leetcode.com/problems/third-maximum-number/){:target="_blank"}

    Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

    Example 1:

    Input: [3, 2, 1]

    Output: 1

    Explanation: The third maximum is 1.

    Example 2:

    Input: [1, 2]

    Output: 2

    Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

    Example 3:

    Input: [2, 2, 3, 1]

    Output: 1

    Explanation: Note that the third maximum here means the third maximum distinct number.
    Both numbers with value 2 are both considered as second maximum.



* Heap

```java
public int thirdMaxQ(int[] nums) {
    PriorityQueue<Integer> q = new PriorityQueue<>();
    HashSet<Integer> set = new HashSet<>();
    for(int i : nums) set.add(i);
    for(int i : set) {
        if(q.size() < 3) q.offer(i);
        else if(q.peek() < i) {
            q.poll();
            q.offer(i);
        }
    }
    if(q.size() == 2) q.poll();
    return q.peek();
}
```

* Intuitive

```java
public int thirdMax(int[] nums) {
    Integer m1 = null, m2 = null, m3 = null;
    for(int i : nums) {
        if(m1 == null) m1 = i;
        else if(m1 < i) {
            m3 = m2;
            m2 = m1;
            m1 = i;
        } else if(m1 > i) {
            if(m2 == null) m2 = i;
            else if(m2 < i) {
                m3 = m2;
                m2 = i;
            } else if(m2 > i) {
                if(m3 == null) m3 = i;
                else if(m3 < i) m3 = i;
            }
        }
    }
    if(m3 != null) return m3;
    return m1;
}
```
