---
title:  "1215. Stepping Numbers"
date:   2019-06-08 22:08:00 +0930
categories: Leetcode
tags: Medium Matrix
---

[{{page.title}}](https://leetcode.com/problems/stepping-numbers/){:target="_blank"}

    A Stepping Number is an integer such that all of its adjacent digits have an absolute difference of exactly
    . For example, 321 is a Stepping Number while 421 is not.

    Given two integers low and high, find and return a sorted list of all the Stepping Numbers in the range
    [low, high] inclusive.



    Example 1:

    Input: low = 0, high = 21
    Output: [0,1,2,3,4,5,6,7,8,9,10,12,21]



    Constraints:

        0 <= low <= high <= 2 * 10^9

* BFS

```java

class Solution {
    public List<Integer> countSteppingNumbers(int low, int high) {
        ArrayList<Integer> result = new ArrayList<>();
        if(low == 0) result.add(low);
        Queue<Integer> q = new LinkedList<>();
        for(int i = 1; i <= 9; i++) q.offer(i);
        while(!q.isEmpty()) {
            int size = q.size();
            for(int k = 0; k < size; k++) {
                int n = q.poll();
                if(n >= low && n <= high) result.add(n);
                if((long)n * 10 > high) continue;
                int last = n % 10;
                if(last > 0) q.offer(n * 10 + last-1);
                if(last < 9) q.offer(n * 10 + last+1);
            }
        }
        return result;
    }
}
```
