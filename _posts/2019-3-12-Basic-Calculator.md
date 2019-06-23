---
title:  "224. Basic Calculator"
date:   2019-3-12 23:16:09 +0930
categories: Leetcode
tags: Math Stack
---

[{{page.title}}](https://leetcode.com/problems/basic-calculator/){:target="_blank"}

    Implement a basic calculator to evaluate a simple expression string.

    The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

    Example 1:

    Input: "1 + 1"
    Output: 2

* Stack Version

```java
public int calculate(String s) {
    Stack<Integer> stack = new Stack<>();
    int num = 0, sign = 1, result = 0;
    int result = 0;
    for(char c : s.toCharArray()) {
        if(c == ' ') continue;
        if(Character.isDigit(c)) {
            num = num * 10 + (c - '0');
        } else if(c == '(') {
            stack.push(sign);
            stack.push(result);
            result = 0;
            num = 0;
            sign = 1;
        } else if(c == ')') {
            result += sign * num;
            System.out.println(stack);
            result = stack.pop() + stack.pop() * result; // previous result + current result * sign
            num = 0;
        } else {
            result += sign * num;
            sign = c == '+' ? 1 : -1;
            num = 0;
        }
    }
    if(num != 0) result += sign * num;
    return result;
}
```
* Recursion

```java
public int calculate(String s) {
    s = s.trim();
    int result = 0, num = 0, temp = 0;
    char sign = '+';
    for(int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if(c == ' ') continue;
        if(Character.isDigit(c)) num = 10 * num + c - '0';
        if(c == '(') {
            int l = 0, r = 0;
            int start = i;
            while(i < s.length()) {
                if(s.charAt(i) == '(') l++;
                if(s.charAt(i) == ')') r++;
                if(l == r) break;
                i++;
            }
            num = calculate(s.substring(start + 1, i));
        }
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
```
