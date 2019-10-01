---
title:  "1209. Remove All Adjacent Duplicates in String II"
date:   2019-06-04 21:38:00 +0930
categories: Leetcode
tags: Medium Stack Recursive
---

[{{page.title}}](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/){:target="_blank"}

    Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and
    removing them causing the left and the right side of the deleted substring to concatenate together.

    We repeatedly make k duplicate removals on s until we no longer can.

    Return the final string after all such duplicate removals have been made.

    It is guaranteed that the answer is unique.

    Example 1:

    Input: s = "abcd", k = 2
    Output: "abcd"
    Explanation: There's nothing to delete.

    Example 2:

    Input: s = "deeedbbcccbdaa", k = 3
    Output: "aa"
    Explanation:
    First delete "eee" and "ccc", get "ddbbbdaa"
    Then delete "bbb", get "dddaa"
    Finally delete "ddd", get "aa"

    Example 3:

    Input: s = "pbbcggttciiippooaais", k = 2
    Output: "ps"



    Constraints:

        1 <= s.length <= 10^5
        2 <= k <= 10^4
        s only contains lower case English letters.


* Stack

```java

public String removeDuplicates(String s, int k) {
    Stack<int[]> stack = new Stack<>();
    for(char c : s.toCharArray()) {
        if(!stack.isEmpty() && stack.peek()[0] == c)
            stack.peek()[1]++;
        else {
            stack.push(new int[]{c, 1});
        if(stack.peek()[1] == k)
            stack.pop();
    }
    StringBuilder sb = new StringBuilder();
    while(!stack.isEmpty()) {
        int[] pair = stack.pop();
        for(int i = 0; i < pair[1]; i++)
            sb.insert(0, (char)pair[0]);
    }
    return sb.toString();
}

```


* Recursion
  - remove repeats every pass

```java

class Solution {
    public String removeDuplicates(String s, int k) {
        return remove(s, k);
    }

    public String remove(String s, int k) {
        // System.out.println(s);
        if(s.length() < k) return s;
        int cnt = 1;
        boolean flag = false;

        int l = 0;
        ArrayList<int[]> arr = new ArrayList<>();
        for(int i = 1; i < s.length(); i++) {
            if(s.charAt(i) != s.charAt(i-1)) {
                cnt = 1;
                l = i;
            } else {
                cnt++;
            }
            if(cnt == k) {
                arr.add(new int[]{l,i});
                flag = true;
                l = i+1;
                i++;
                cnt = 1;
            }
        }
        if(!flag) return s;
        StringBuilder sb = new StringBuilder();
        sb.append(s.substring(0, arr.get(0)[0]));
        for(int i = 1; i < arr.size(); i++) {
            sb.append(s.substring(arr.get(i-1)[1]+1, arr.get(i)[0]));
        }
        sb.append(s.substring(arr.get(arr.size()-1)[1]+1));
        return remove(sb.toString(), k);
    }
}
```
