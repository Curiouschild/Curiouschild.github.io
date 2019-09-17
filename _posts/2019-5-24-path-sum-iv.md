---
title:  "666. Path Sum IV"
date:   2019-05-24 11:51:00 +0930
categories: Leetcode
tags: Medium DynamicProgramming
---

[{{page.title}}](https://leetcode.com/problems/path-sum-iv/){:target="_blank"}

    If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits
    integers.

    For each integer in this list:

        The hundreds digit represents the depth D of this node, 1 <= D <= 4.
        The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The
        position is the same as that in a full binary tree.
        The units digit represents the value V of this node, 0 <= V <= 9.



    Given a list of ascending three-digits integers representing a binary tree with the depth smaller than 5,
    you need to return the sum of all paths from the root towards the leaves.

    Example 1:

    Input: [113, 215, 221]
    Output: 12
    Explanation:
    The tree that the list represents is:
        3
       / \
      5   1

    The path sum is (3 + 5) + (3 + 1) = 12.



    Example 2:

    Input: [113, 221]
    Output: 4
    Explanation:
    The tree that the list represents is:
        3
         \
          1

    The path sum is (3 + 1) = 4.

* Iterative counting the leafs of each node

```java

public int pathSum(int[] nums) {
    HashMap<Integer, Integer> cnt = new HashMap<>(); // cnt of each node in the calculation
                                                    // equals the number of leafs in the substree
    for(int j = nums.length-1; j >= 0; j--) {
        int i = nums[j];
        int level = i / 100; // level of current node
        int pos = (i - (i/100) * 100) / 10; // position of current node
        int p1 = 2 * pos - 1, p2 = p1 + 1; // position of left and right child
        int k = i / 10, k1 = (level+1) * 10 + p1, k2 = (level+1) * 10 + p2;
        if(!cnt.containsKey(k1) && !cnt.containsKey(k2)) { // leaf
            cnt.put(k, 1);
        } else { // internal
            int left = cnt.getOrDefault(k1, 0), right = cnt.getOrDefault(k2, 0);
            cnt.put(k, left + right);
        }
    }
    int result = 0;
    for(int i : nums) {
        int key = i / 10, value = i % 10;
        result += cnt.get(key) * value;
    }
    return result;
}
```
