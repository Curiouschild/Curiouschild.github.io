---
title:  "43. Multiply Strings"
date:   2019-4-20 16:13:00 +0930
categories: Leetcode
tags: Math String
---

[{{page.title}}](https://leetcode.com/problems/multiply-strings/){:target="_blank"}

    Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2,
     also represented as a string.

    Example 1:

    Input: num1 = "2", num2 = "3"
    Output: "6"

    Example 2:

    Input: num1 = "123", num2 = "456"
    Output: "56088"

    Note:

        The length of both num1 and num2 is < 110.
        Both num1 and num2 contain only digits 0-9.
        Both num1 and num2 do not contain any leading zero, except the number 0 itself.
        You must not use any built-in BigInteger library or convert the inputs to integer directly.




* Multiply all pairs of digits, and store the product in an array.

```java
public String multiply(String num1, String num2) {
    int[] result = new int[num1.length()+num2.length()];
    for(int i = num1.length()-1; i >= 0; i--) {
        for(int j = num2.length()-1; j >= 0; j--) {
            result[i+j+1] += (num1.charAt(i)-'0') * (num2.charAt(j)-'0');
        }
    }
    int carry = 0;

    for(int i = result.length-1; i >= 0; i--) {
        int temp = (result[i]+carry) % 10;
        carry = (result[i]+carry) / 10;
        result[i] = temp;
    }
    StringBuilder sb = new StringBuilder();
    for(int d : result)
        if(!(sb.length()==0 && d == 0))
            sb.append(d);
    return sb.length() == 0 ? "0" : sb.toString();
}
```
