---
title:  "151. Reverse Words in a String"
date:   2019-4-9 23:17:00 +0930
categories: Leetcode
tags: PriorityQueue
---

[{{page.title}}](https://leetcode.com/problems/reverse-words-in-a-string/){:target="_blank"}

    Given an input string, reverse the string word by word.

    Example 1:

    Input: "the sky is blue"
    Output: "blue is sky the"

    Example 2:

    Input: "  hello world!  "
    Output: "world! hello"
    Explanation: Your reversed string should not contain leading or trailing spaces.



```java
public String reverseWords(String s) {
    StringBuilder result = new StringBuilder(), temp = new StringBuilder();
    int i = s.length()-1;
    while(i >= 0) {
        while(i >= 0 && s.charAt(i) == ' ') i--;
        int j = i;
        while(i >= 0 && s.charAt(i) != ' ') i--;
        temp.setLength(0);
        if(j >= 0) {
            temp.append(s.substring(i+1, j+1)).append(' ');
            result.append(temp);
        }
    }
    if(result.length() == 0) return "";
    else result.setLength(result.length()-1);
    return result.toString();
}
```

```java
public String reverseWords(String s) {
    s = s.trim().replace("\\s+", " ");
    System.out.println(s);
    char[] arr = s.toCharArray();
    int i = 0, j = 0;
    while(j < arr.length) {
        // System.out.println(j);
        while(j < arr.length && arr[j] != ' ') j++;
        reverse(arr, i, j-1);
        j++;
        i = j;
    }
    reverse(arr, 0, arr.length-1);
    String n = new String(arr);
    return n;
}

public void reverse(char[] arr, int i, int j) {
    while(i < j) {
        char temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
        i++;j--;
    }
}
```
