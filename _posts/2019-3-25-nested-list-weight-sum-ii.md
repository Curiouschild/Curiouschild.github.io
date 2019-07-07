---
title:  "364. Nested List Weight Sum II"
date:   2019-3-25 23:39:00 +0930
categories: Leetcode
tags: Recursion DataStructure
---

[{{page.title}}](https://leetcode.com/problems/nested-list-weight-sum-ii/){:target="_blank"}

    Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

    Each element is either an integer, or a list -- whose elements may also be integers or other lists.

    Different from the previous question where weight is increasing from root to leaf, now the weight is
    defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have
    the largest weight.

    Example 1:

    Input: [[1,1],2,[1,1]]
    Output: 8
    Explanation: Four 1's at depth 1, one 2 at depth 2.

See Also: [nested-list-weight-sum](https://leetcode.com/problems/nested-list-weight-sum/){:target="_blank"}

```java
public int depthSumInverse(List<NestedInteger> nestedList) {
    int h = getHeight(nestedList);
    return count(nestedList, h);
}

public int count(List<NestedInteger> nestedList, int level) {
    int sum = 0;
    for(NestedInteger n : nestedList)
        sum += n.isInteger() ? n.getInteger() * level : count(n.getList(), level - 1);
    return sum;
}

public int getHeight(List<NestedInteger> nestedList) {
    int h = 0;
    for(NestedInteger n : nestedList)
        if(!n.isInteger())
            h = Math.max(h, getHeight(n.getList()));
    return h + 1;
}
```
