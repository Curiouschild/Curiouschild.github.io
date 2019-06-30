---
title:  "904. Fruit Into Baskets"
date:   2019-3-19 21:56:11 +0930
categories: Leetcode
tags: HashMap TwoPointers SlidingWindow
---

[{{page.title}}](){:target="_blank"}

    In a row of trees, the i-th tree produces fruit with type tree[i].

    You start at any tree of your choice, then repeatedly perform the following steps:

        Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
        Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.

    Note that you do not have any choice after the initial choice of starting tree: you must perform step 1,
    then step 2, then back to step 1, then step 2, and so on until you stop.

    You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only
    carry one type of fruit each.

    What is the total amount of fruit you can collect with this procedure?

    Example 1:

    Input: [1,2,1]
    Output: 3
    Explanation: We can collect [1,2,1].


```java
public int totalFruit(int[] arr) {
    int l = 0, r = 0, result = 0;
    HashMap<Integer, Integer> map = new HashMap<>();
    while(r < arr.length) {
        while(map.size() == 2 && !map.containsKey(arr[r])) {
            int v = map.get(arr[l]);
            if(v == 1) map.remove(arr[l]);
            else map.put(arr[l], v-1);
            l++;
        }
        map.put(arr[r], map.getOrDefault(arr[r], 0)+1);
        result = Math.max(result, r - l + 1);
        r++;
    }
    return result;
}
```
