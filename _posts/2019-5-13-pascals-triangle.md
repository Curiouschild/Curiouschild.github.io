---
title:  "118. Pascal's Triangle"
date:   2019-05-13 12:25:00 +0930
categories: Leetcode
tags: Easy DynamicProgramming
---

[{{page.title}}](https://leetcode.com/problems/pascals-triangle/){:target="_blank"}


    Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


    In Pascal's triangle, each number is the sum of the two numbers directly above it.

    Example:

    Input: 5
    Output:
    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    ]

```java

public List<List<Integer>> generate(int numRows) {
    List<List<Integer>> result = new ArrayList<>();
    if(numRows == 0) return result;
    result.add(Arrays.asList(1));
    for(int i = 1; i < numRows; i++) {
        ArrayList<Integer> temp = new ArrayList<>();
        List<Integer> lastRow = result.get(i-1);
        temp.add(1);
        for(int j = 1; j < lastRow.size(); j++) {
            temp.add(lastRow.get(j-1) + lastRow.get(j));
        }
        temp.add(1);
        result.add(temp);
    }
    return result;
}
```
