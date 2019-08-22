---
title:  "71. Simplify Path"
date:   2019-4-28 19:22:00 +0930
categories: Leetcode
tags: Medium String
---

[{{page.title}}](https://leetcode.com/problems/simplify-path/){:target="_blank"}

    Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

    In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period ..
    moves the directory up a level. For more information, see: Absolute path vs relative path in Linux/Unix

    Note that the returned canonical path must always begin with a slash /, and there must be only a single
    slash / between two directory names. The last directory name (if it exists) must not end with a trailing /.
    Also, the canonical path must be the shortest string representing the absolute path.



    Example 1:

    Input: "/home/"
    Output: "/home"
    Explanation: Note that there is no trailing slash after the last directory name.

    Example 2:

    Input: "/../"
    Output: "/"
    Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level
    you can go.

    Example 3:

    Input: "/home//foo/"
    Output: "/home/foo"
    Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

    Example 4:

    Input: "/a/./b/../../c/"
    Output: "/c"

    Example 5:

    Input: "/a/../../b/../c//.//"
    Output: "/c"

    Example 6:

    Input: "/a//b////c/d//././/.."
    Output: "/a/b/c"



* Back to front (Or use stack to process the path from front to rear)

```java
public String simplifyPath(String path) {
    String[] arr = path.split("/+");
    System.out.println(Arrays.toString(arr));
    int up = 0;
    StringBuilder result = new StringBuilder();
    for(int i = arr.length-1; i >= 0; i--) {
        String s = arr[i];
        if(s.length() == 0 || s.equals(".")) continue;
        else if(s.equals("..")) up++;
        else if(up > 0) {
            up--;
            continue;
        } else
            result.insert(0, '/').insert(0, s);
    }
    result.insert(0, '/');
    if(result.length() > 1) result.setLength(result.length()-1);
    return result.toString();
}
```
