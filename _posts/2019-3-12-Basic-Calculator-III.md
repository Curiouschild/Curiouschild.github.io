---
title:  "772. Basic Calculator III"
date:   2019-3-13 00:38:10 +0930
categories: Leetcode
tags: Math Stack
---

[{{page.title}}](https://leetcode.com/problems/basic-calculator-iii/){:target="_blank"}

    Implement a basic calculator to evaluate a simple expression string.

    The expression string may contain open ( and closing parentheses ), the plus + or minus
    sign -, non-negative integers and empty spaces .

    The expression string contains only non-negative integers, +, -, *, / operators , open
    ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.

    You may assume that the given expression is always valid. All intermediate results will
    be in the range of [-2147483648, 2147483647].


  * General template Recursion

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
