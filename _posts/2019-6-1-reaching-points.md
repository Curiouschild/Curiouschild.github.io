---
title:  "780. Reaching Points"
date:   2019-06-01 20:48:00 +0930
categories: Leetcode
tags: Hard Math BinarySearch
---

[{{page.title}}](https://leetcode.com/problems/reaching-points/){:target="_blank"}

    A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).

    Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves
    exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.

    Examples:
    Input: sx = 1, sy = 1, tx = 3, ty = 5
    Output: True
    Explanation:
    One series of moves that transforms the starting point to the target is:
    (1, 1) -> (1, 2)
    (1, 2) -> (3, 2)
    (3, 2) -> (3, 5)

    Input: sx = 1, sy = 1, tx = 2, ty = 2
    Output: False

    Input: sx = 1, sy = 1, tx = 1, ty = 1
    Output: True

    Note:

        sx, sy, tx, ty will all be integers in the range [1, 10^9].


* A better way to shrink.......oh my math.

[Algorithm](https://leetcode.com/articles/reaching-points/){:target="_blank"}

Say tx > ty. We know that the next parent operations will be to subtract ty from tx, until such time that tx =
tx % ty. When both tx > ty and ty > sy, we can perform all these parent operations in one step, replacing
while tx > ty: tx -= ty with tx %= ty.

Otherwise, if say tx > ty and ty <= sy, then we know ty will not be changing (it can only decrease). Thus,
only tx will change, and it can only change by subtracting by ty. Hence, (tx - sx) % ty == 0 is a necessary
and sufficient condition for the problem's answer to be True.

```java
class Solution {
    public boolean reachingPoints(int sx, int sy, int tx, int ty) {
        while (tx >= sx && ty >= sy) {
            if (tx == ty) break;
            if (tx > ty) {
                if (ty > sy) tx %= ty; // equal to reduce tx until tx < ty
                else return (tx - sx) % ty == 0; // ty == sy; equal to reduce tx to see if finally tx == sx
            } else {
                if (tx > sx) ty %= tx;
                else return (ty - sy) % tx == 0; // tx = sx
            }
        }
        return (tx == sx && ty == sy);
    }
}
```

* Binary Search
  - shrink the search scope with binary search
```java

class Solution {
    public boolean reachingPoints(int sx, int sy, int tx, int ty) {
        if(tx + ty < sx + sy) return false;

        int x = tx, y = ty;
        int sum1 = sx + sy;
        while(x + y >= sx + sy) {
            if(x == sx && y == sy) return true;
            int[] arr = shrink(sum1, x, y); // shrink x or y
                                            // x still be greater than y if x > y before shrink
                                            // and vice versa
            x = arr[0];
            y = arr[1];
            if(x == sx && y == sy) return true;
            if(x == y) {
                if(x == sx && sy == 0 || sx == 0 && sy == y) return true;
                else return false;
            } else if(x > y) {
                x = x - y;
            } else {
                y = y - x;
            }
        }
    }

    public int[] shrink(int sum1, int x, int y) {
        int small = Math.min(x, y);
        int large = Math.max(x, y);
        int l = 1, r = (large / small)-1;
        while(l < r) {
            int mid = l + (r-l) / 2; // large-mid*small is always greater than small
            int sum = large + small - mid * small;
            if(sum < sum1) {
                r = mid-1;
            } else if(sum >= sum1) {
                if(mid == l) { // ugly...
                    r = l;
                    break;
                }
                l = mid;
            }
        }
        if(x > y) {
            x = large - r * small;
        } else {
            y = large - r * small;
        }
        return new int[]{x, y};
    }
}
```
