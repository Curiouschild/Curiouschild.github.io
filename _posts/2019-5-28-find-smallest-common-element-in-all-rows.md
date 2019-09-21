---
title:  "1198. Find Smallest Common Element in All Rows"
date:   2019-05-28 10:37:00 +0930
categories: Leetcode
tags: Medium Matrix
---

[{{page.title}}](https://leetcode.com/problems/minimum-knight-moves/){:target="_blank"}

    Given a matrix mat where every row is sorted in increasing order, return the smallest common element in all
    rows.

    If there is no common element, return -1.



    Example 1:

    Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
    Output: 5



    Constraints:

        1 <= mat.length, mat[i].length <= 500
        1 <= mat[i][j] <= 10^4
        mat[i] is sorted in increasing order.



* Cnt


```java
public int smallestCommonElement(int[][] mat) {
    int[] cnt = new int[100001];
    for(int i = 0; i < mat.length; i++) {
        for(int j = 0; j < mat[0].length; j++) {
            cnt[mat[i][j]]++;
            if(cnt[mat[i][j]] == mat.length) return mat[i][j];
        }
    }
    return -1;
}


```

* set


```java

public int smallestCommonElement2(int[][] mat) {
    HashSet<Integer> set = new HashSet<>();
    for(int j : mat[0]) set.add(j);
    for(int i = 1; i < mat.length; i++) {
        HashSet<Integer> temp = new HashSet<>();
        for(int j : mat[i]) {
            if(set.contains(j))
                temp.add(j);
        }
        set = temp;
    }
    ArrayList<Integer> arr = new ArrayList<>(set);
    Collections.sort(arr);
    if(arr.size() == 0) return -1;
    return arr.get(0);
}

```
