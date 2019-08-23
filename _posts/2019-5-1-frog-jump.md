---
title:  "403. Frog Jump"
date:   2019-05-01 12:37:00 +0930
categories: Leetcode
tags: Hard Recursive
---

[{{page.title}}](https://leetcode.com/problems/frog-jump/){:target="_blank"}

    A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a
    stone. The frog can jump on a stone, but it must not jump into the water.

    Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to
    cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the
    first jump must be 1 unit.

    If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that
    the frog can only jump in the forward direction.

    Note:

        The number of stones is ≥ 2 and is < 1,100.
        Each stone's position will be a non-negative integer < 231.
        The first stone's position is always 0.

    Example 1:

    [0,1,3,5,6,8,12,17]

    There are a total of 8 stones.
    The first stone at the 0th unit, second stone at the 1st unit,
    third stone at the 3rd unit, and so on...
    The last stone at the 17th unit.

    Return true. The frog can jump to the last stone by jumping
    1 unit to the 2nd stone, then 2 units to the 3rd stone, then
    2 units to the 4th stone, then 3 units to the 6th stone,
    4 units to the 7th stone, and 5 units to the 8th stone.


* Backtrack with memoizatino

One option is to use dp[n][n] to store start and step states

An optimization is to binary search tree times the next possible position as the stones array is ordered
nextPosition = binarySearch(stones, start+1, stones.length, start+step(+1,-1,+0))

```java
class Solution {
    boolean find = false; // stop recursion when find
    HashSet<String> set = new HashSet<>(); // only record the faild situation
    public boolean canCross(int[] stones) {
        jump(stones, 0, 0);
        return find;
    }

    public void jump(int[] stones, int start, int step) {
        if(start == stones.length-1) {
            find = true;
            return;
        }
        if(set.contains(start + "," + step)) return;
        int left = stones[start] + step-1, right = stones[start] + step+1;
        for(int i = start + 1; i < stones.length; i++) {
            if(stones[i] >= left && stones[i] <= right) {
                jump(stones, i, stones[i]-stones[start]);
                if(find) return;
            } else if(stones[i] > right)
                break;
        }
        set.add(start+","+step);
    }
}
```

* DP O(N^2)

map< start, steps to jump to start >

```java
public boolean canCross(int[] stones) {
    HashMap<Integer, HashSet<Integer>> map = new HashMap<>();
    for(int i : stones) map.put(i, new HashSet<Integer>());
    map.get(0).add(0);
    for(int i = 0; i < stones.length; i++) {
        for(int step : map.get(stones[i])) {
            for(int next = step-1; next <= step+1; next++) {
                if(next > 0 && map.containsKey(stones[i]+next))
                    map.get(stones[i]+next).add(next);
            }
        }
    }
    return map.get(stones[stones.length-1]).size() > 0;
}
```
