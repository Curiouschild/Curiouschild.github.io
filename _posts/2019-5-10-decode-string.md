---
title:  "394. Decode String"
date:   2019-05-10 17:15:00 +0930
categories: Leetcode
tags: Medium Recursive Stack
---

[{{page.title}}](https://leetcode.com/problems/decode-string/){:target="_blank"}

    Given an encoded string, return its decoded string.

    The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being
    repeated exactly k times. Note that k is guaranteed to be a positive integer.

    You may assume that the input string is always valid; No extra white spaces, square brackets are well-
    formed, etc.

    Furthermore, you may assume that the original data does not contain any digits and that digits are only for
    those repeat numbers, k. For example, there won't be input like 3a or 2[4].

    Examples:

    s = "3[a]2[bc]", return "aaabcbc".
    s = "3[a2[c]]", return "accaccacc".
    s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


* Recursion

Another approach is to use stack.

```java

public String decodeString(String s) {
    if(!s.contains("[")) return s;
    int repeat = 0;
    String result = "", temp = "";
    for(int i = 0; i < s.length(); i++) {
        if(Character.isDigit(s.charAt(i))) {
            repeat = repeat * 10 + (s.charAt(i)-'0');
        } else if(s.charAt(i) == '[') {
            int r = i+1, lc = 1;
            while(lc != 0) {
                if(s.charAt(r) == '[') lc++;
                else if(s.charAt(r) == ']') lc--;
                r++;
            }
            temp = decodeString(s.substring(i+1, r-1));
            while(repeat > 0) {
                result += temp;
                repeat--;
            }
            temp = "";
            i = r-1;
        } else {
            result += s.charAt(i);
        }
    }
    return result;
}
```

* Stack

```java
public String decodeString(String s) {
    Stack<String> stack = new Stack<>();
    String res = "";

    for(int i = 0; i < s.length(); i++) {
        if(Character.isDigit(s.charAt(i))) { // push the previous string and num for the next string into the stack
            String num = "";
            while(Character.isDigit(s.charAt(i))) {
                num += s.charAt(i++);
            }
            stack.push(res);
            stack.push(num);
            res = "";
        } else if(s.charAt(i) == '[') {
            // do nothing
        } else if(s.charAt(i) == ']') {
            int mul = Integer.valueOf(stack.pop()); // num for the current string
            String pre = stack.pop(); // previous string
            StringBuilder sb = new StringBuilder(pre); // add privous string
            while(mul-->0) sb.append(res); // multiply current string
            res = sb.toString();
        } else {
            res += s.charAt(i);
        }
    }
    return res;
}
```
