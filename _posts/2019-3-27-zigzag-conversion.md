---
title:  "6. ZigZag Conversion"
date:   2019-3-27 12:12:00 +0930
categories: Leetcode
tags: Math String
---

[{{page.title}}](https://leetcode.com/problems/zigzag-conversion/){:target="_blank"}

    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
    (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R

    And then read line by line: "PAHNAPLSIIGYIR"

    Write the code that will take a string and make this conversion given a number of rows:

    string convert(string s, int numRows);

    Example 1:

    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"


```java
public String convert(String s, int numRows) {
    if(numRows == 1) return s;
    int row = 0, step = -1;
    String[] result = new String[numRows];
    Arrays.fill(result, "");
    for(char c : s.toCharArray()) {
        if(row == 0 || row == numRows-1) step = -step;
        result[row] += c;
        row += step;
    }
    return String.join("", result);
}
```

* Pure math

```java
class Solution {
    public String convert(String s, int numRows) {
        //如果是有一行，可以直接返回
        if (numRows == 1) {
            return s;
        }
        StringBuilder result = new StringBuilder();
        //运用数学规律，逐行取值
        for (int i = 0; i < numRows; i++) {
            int j = 0;//表示第i行的第j个数
            while (j + i < s.length()) {
                result.append(s.charAt(j + i));//j每次循环时，首先取j+i坐标上的字母
                //如果不是第一排或者最后一排，一般情况下，每两个竖排间会有两个字母，第二个字母的规律是j+numRows * 2 - 2 - i
                if (i != 0 && i != numRows - 1 && j + numRows * 2 - 2 - i < s.length()) {
                    result.append(s.charAt(j + numRows * 2 - 2 - i));
                }
                //第一竖排和第二竖排的坐标差值为numRows * 2 - 2
                j += numRows * 2 - 2;
            }
        }
        return result.toString();
    }
}
```
