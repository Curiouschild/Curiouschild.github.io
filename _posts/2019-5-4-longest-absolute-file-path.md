---
title:  "388. Longest Absolute File Path"
date:   2019-05-04 23:59:00 +0930
categories: Leetcode
tags: Medium Stack String
---

[{{page.title}}](https://leetcode.com/problems/longest-absolute-file-path/){:target="_blank"}

    Suppose we abstract our file system by a string in the following manner:

    The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

    dir
        subdir1
        subdir2
            file.ext

    The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file
    file.ext.

    The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    represents:

    dir
        subdir1
            file1.ext
            subsubdir1
        subdir2
            subsubdir2
                file2.ext

    The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and
    an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2
    containing a file file2.ext.

    We are interested in finding the longest (number of characters) absolute path to a file within our file
    system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/
    file2.ext", and its length is 32 (not including the double quotes).

    Given a string representing the file system in the above format, return the length of the longest absolute
    path to file in the abstracted file system. If there is no file in the system, return 0.

    Note:

        The name of a file contains at least a . and an extension.
        The name of a directory or sub-directory will not contain a ..

    Time complexity required: O(n) where n is the size of the input string.

    Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/
    sth.png.


A stranger case:
"root1\n    abc.txt"
result == length of "    abc.txt"

* split string

```java
public int lengthLongestPath(String input) {
    String[] arr = input.split("\n");
    if(arr.length == 1 && arr[0].contains(".")) return arr[0].length();
    int len = 1;
    int result = 0;
    Stack<String> stack = new Stack<>();
    stack.push("");
    for(int i = 0; i < arr.length; i++) {
        String s = arr[i];
        int j = s.lastIndexOf("\t");
        int tCnt = j+1;
        s = s.substring(j+1, s.length());
        while(tCnt < stack.size()) {
            String prev = stack.pop();
            len -= prev.length()+1;
        }
        len += 1+s.length();
        stack.push(s);
        if(s.contains(".")) {
            result = Math.max(result, len-1);
        }
    }
    return result;
  }
```

* Stack stores the length of dirs. len is the curr length of absolute path

A slower but easy to code approach is to preprocess the data by spliting intput by \n

```java
public int lengthLongestPath(String input) {
    Stack<Integer> stack = new Stack<>();
    int i = 0;
    while(i < input.length() && input.charAt(i) != '\n') i++;
    if(i == input.length()) return input.contains(".") ? input.length() : 0;
    stack.push(i);
    int len = i;
    int result = 0;
    while(i < input.length()) {
        int level = 1;
        int j = i+1;
        while(input.charAt(j) == '\t') {
            j++;
            level++;
        }
        // now j is at the start point of the next directory
        int k = j;
        boolean isFile = false;
        while(k < input.length() && input.charAt(k) != '\n') {
            if(input.charAt(k) == '.') isFile = true;
            k++;
        }
        // k is at the next \n\t...
        while(level <= stack.size()) {
            int reduce = stack.pop();
            len -= reduce+1;
        }
        len += k-j+1;
        stack.push(k-j);
        if(isFile)
            result = Math.max(result, len);
        i = k;
    }
    return result;
}

}
```
