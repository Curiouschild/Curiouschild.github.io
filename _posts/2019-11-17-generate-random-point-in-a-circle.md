---
title:  "478. Generate Random Point in a Circle"
date:   2019-11-17 19:05:00 +0930
categories: Leetcode
tags: Medium Randomness
---

[{{page.title}}](https://leetcode.com/problems/generate-random-point-in-a-circle/){:target="_blank"}

    Given the radius and x-y positions of the center of a circle, write a function randPoint which generates a uniform
    random point in the circle.

    Note:

      input and output values are in floating-point.
      radius and x-y position of the center of the circle is passed into the class constructor.
      a point on the circumference of the circle is considered to be in the circle.
      randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.

    Example 1:

    Input:
    ["Solution","randPoint","randPoint","randPoint"]
    [[1,0,0],[],[],[]]
    Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]

    Example 2:

    Input:
    ["Solution","randPoint","randPoint","randPoint"]
    [[10,5,-7.5],[],[],[]]
    Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]


* Give up illegal data points

```java

class Solution {
    double r, xc, yc;
    Random random = new Random();
    public Solution(double radius, double x_center, double y_center) {
        r = radius;
        xc = x_center;
        yc = y_center;
    }

    public double[] randPoint() {
        while(true) {
            double x = random.nextDouble() * r * 2 - r;
            double y = random.nextDouble() * r * 2 - r;
            if(x * x + y * y <= r * r) {
                return new double[]{xc + x, yc + y};
            }
        }
    }
}
```
