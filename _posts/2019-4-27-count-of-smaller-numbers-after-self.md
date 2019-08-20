---
title:  "315. Count of Smaller Numbers After Self"
date:   2019-4-27 18:37:00 +0930
categories: Leetcode
tags: DynamicProgramming Hard
---

[{{page.title}}](https://leetcode.com/problems/count-of-smaller-numbers-after-self/){:target="_blank"}

    You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

    Example:

    Input: [5,2,6,1]
    Output: [2,1,1,0]
    Explanation:
    To the right of 5 there are 2 smaller elements (2 and 1).
    To the right of 2 there is only 1 smaller element (1).
    To the right of 6 there is 1 smaller element (1).
    To the right of 1 there is 0 smaller element.


* Brutal Force

```java
public List<Integer> countSmaller(int[] nums) {
    int[] result = new int[nums.length];
    for(int i = nums.length-2; i >= 0; i--) {
        for(int j = i+1; j < nums.length; j++)
            if(nums[j] < nums[i])
                result[i]++;
    }
    ArrayList<Integer> arr = new ArrayList<>();
    for(int i : result) arr.add(i);
    return arr;
}

```


* TreeMap TLE pass 15/16

```java

public List<Integer> countSmaller(int[] nums) {
    int min = Integer.MAX_VALUE;
    for(int i : nums) if(i < min) min = i;
    TreeMap<Node,Integer> map = new TreeMap<>((x,y)->{
        int r = x.v-y.v;
        if(r == 0) return Integer.compare(x.i, y.i);
        return r;
        });
    Node minNode = new Node(min-1, -1);
    LinkedList<Integer> result = new LinkedList<>();
    for(int i = nums.length-1; i >= 0; i--) {
        Node curr = new Node(nums[i], i);
        int size = map.subMap(minNode, curr).size();
        map.put(curr, i);
        result.addFirst(size);
    }
    return result;
}
class Node {
    int v;
    int i;
    public Node(int v, int i) {
        this.v = v;
        this.i = i;
    }
}
```
