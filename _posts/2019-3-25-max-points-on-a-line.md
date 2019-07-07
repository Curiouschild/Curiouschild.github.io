---
title:  "149. Max Points on a Line"
date:   2019-3-25 21:51:00 +0930
categories: Leetcode
tags: HashMap Math
---

[{{page.title}}](https://leetcode.com/problems/max-points-on-a-line/){:target="_blank"}

    Given n points on a 2D plane, find the maximum number of points that lie on the
    same straight line.

    Example 1:

    Input: [[1,1],[2,2],[3,3]]
    Output: 3
    Explanation:
    ^
    |
    |        o
    |     o
    |  o
    +------------->
    0  1  2  3  4


```java
public int maxPoints(int[][] points) {
    int max = 0;
    for(int i = 0; i < points.length; i++) {
        HashMap<String, Integer> map = new HashMap<>();
        int temp = 0, overlap = 0;
        for(int j = 0; j < points.length; j++) {
            int[] a = points[i], b = points[j];
            int dx = a[0] - b[0], dy = a[1] - b[1];
            if(dx == 0 && dy == 0) overlap++;
            else {
                int gcd = generateGcd(dx, dy);
                dx /= gcd;
                dy /= gcd;
                String slope = dy + "/" + dx;
                map.put(slope, map.getOrDefault(slope, 0) + 1);
            }
        }
        for(Integer v : map.values()) temp = Math.max(v, temp);
        max = Math.max(max, temp + overlap);
    }
    return max;
}

 public int generateGcd(int x, int y) {
    if (y == 0) return x;
    return generateGcd(y, x % y);
}
```

Another version; Does not pass all test cases.

```java
public int maxPointsFailed(int[][] points) {
    HashMap<String, HashSet<int[]>> map = new HashMap<>();
    for(int i = 0; i < points.length; i++) {
        for(int j = i + 1; j < points.length; j++) {
            int[] a = points[i], b = points[j];
            int dx = a[0] - b[0], dy = a[1] - b[1];
            HashSet<int[]> set = null;
            String key = "";
            if(dx == 0) {
                key += a[0];
            } else {
                double slope =  (double)dy / (double)dx;
                double yIntercept = a[1] - slope * a[0];
                key += yIntercept + "," + slope;
            }
            set = map.getOrDefault(key, new HashSet<>());
            set.add(a);
            set.add(b);
            map.put(key, set);
        }
    }
    int max = points.length > 0 ? 1 : 0;
    String m = "";
    for(HashSet<int[]> set : map.values()) {
        max = Math.max(set.size(), max);
    }
    return max;
}
```
