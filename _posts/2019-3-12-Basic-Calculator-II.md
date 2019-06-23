---
title:  "227. Basic Calculator II"
date:   2019-3-13 00:38:10 +0930
categories: Leetcode
tags: Math Stack
---

[{{page.title}}](https://leetcode.com/problems/basic-calculator-ii/){:target="_blank"}

    Implement a basic calculator to evaluate a simple expression string.

    The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

    Example 1:

    Input: "3+2*2"
    Output: 7


* Good Version

```java
public int calculate(String s) {
    s = s.trim();
    int result = 0, num = 0, temp = 0;
    char sign = '+';
    for(int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if(c == ' ') continue;
        if(Character.isDigit(c)) num = 10 * num + c - '0';
        if(c == '+' || c == '-' || c == '*' || c == '/' || i == s.length()-1) {
            switch(sign) {
                case '+' : temp += num; break;
                case '-' : temp -= num; break;
                case '*' : temp *= num; break;
                case '/' : temp /= num; break;
            }
            if(c == '+' || c == '-' || i == s.length() - 1) {
                result += temp;
                temp = 0;
            }
            sign = c;
            num = 0;
        }
    }
    return result;
}
}
```

* Verbose Version

```java 
public int calculateMyBadVersion(String s) {
    int result = 0, num = 0, temp = 1;
    char sign = '+';
    Stack<Integer> stack = new Stack<>();
    for(char c : s.toCharArray()) {
        if(c == ' ') continue;
        if(Character.isDigit(c)) num = num * 10 + (c - '0');
        else {
            if(c == '+' || c == '-') {
                if(sign == '+' || sign == '-') {
                    result += num * (sign == '+' ? 1 : -1);
                } else {
                    if(sign == '*') temp *= num;
                    if(sign == '/') temp /= num;
                    result += temp;
                    temp = 0;
                }
            } else if(c == '*' || c == '/') {
                if(sign == '+' || sign == '-') {
                    temp = sign == '+' ? num : -num;
                } else {
                    if(sign == '*') temp *= num;
                    if(sign == '/') temp /= num;
                }
            }
            sign = c;
            num = 0;
        }
    }
    if(sign == '+' || sign == '-') {
        result += sign == '+' ? num : -num;
    } else {
        if(sign == '*') temp *= num;
        if(sign == '/') temp /= num;
        result += temp;
    }
    return result;
}
```
