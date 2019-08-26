---
title:  "943. Find the Shortest Superstring"
date:   2019-05-03 12:12:00 +0930
categories: Leetcode
tags: Hard Graph ShortestPath
---

[{{page.title}}](https://leetcode.com/problems/find-the-shortest-superstring/){:target="_blank"}

    Given an array A of strings, find any smallest string that contains each string in A as a substring.

    We may assume that no string in A is substring of another string in A.


    Example 1:

    Input: ["alex","loves","leetcode"]
    Output: "alexlovesleetcode"
    Explanation: All permutations of "alex","loves","leetcode" would also be accepted.

    Example 2:

    Input: ["catg","ctaagt","gcta","ttca","atgcatc"]
    Output: "gctaagttcatgcatc"

    Note:

        1 <= A.length <= 12
        1 <= A[i].length <= 20


This is a travelling salesman problem...
The answer is the shortest/longest distance of a weighted directed graph...
Each String can be regarded as a node, and the overlapped length are the reward of edges

* A fast coded TLE version 58 / 72 test cases passed.

TODO: A iterative DP Solution

```java
class Solution {
    String result = "";
    int max;
    HashSet<String> visited = new HashSet<>();
    HashMap<Integer, Integer> map = new HashMap<>();
    public String shortestSuperstring(String[] A) {
        for(String s : A) result += s;
        max = result.length();
        HashSet<Integer> set = new HashSet<>();
        map.put(0, 0);
        build(A, "", set, 0, 0);
        return result;
    }

    public void build(String[] arr, String s, HashSet<Integer> set, int mask, int saved) {
        if(map.containsKey(mask)) {
            if(map.get(mask) > saved) return;
            map.put(mask, saved);
        }
        if(s.length() >= result.length()) return;
        if(set.size() == arr.length) {
            if(s.length() < result.length())
                result = s;
        }

        for(int j = 0; j < arr.length; j++) {
            int nextMask = mask | (1 << j);
            if(set.contains(j)) continue;
            set.add(j);
            String curr = arr[j];
            boolean overlap = false;
            if(s.contains(curr)) {
                build(arr, s, set, nextMask, saved + curr.length());
            }
            else {
                // curr[i:] overlap
                for(int i = curr.length()-1; i > 0; i--) {
                    String right = curr.substring(i);
                    if(s.startsWith(right)) {
                        build(arr, curr.substring(0, i) + s, set, nextMask, saved + right.length());
                        overlap = true;
                    }
                }
                // curr[:i] overlap
                for(int i = 1; i < curr.length(); i++) {
                    String left = curr.substring(0, i);
                    if(s.endsWith(left)) {
                        build(arr, s + curr.substring(i), set, nextMask, saved + left.length());
                        overlap = true;
                    }
                }
            }
            if(!overlap) {
                build(arr, s + curr, set, nextMask, saved);
                build(arr, curr + s, set, nextMask, saved);
            }

            set.remove(j);
        }
    }
```
