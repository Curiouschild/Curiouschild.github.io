---
title:  "165. Compare Version Numbers"
date:   2019-4-30 22:10:00 +0930
categories: Leetcode
tags: Medium
---

[{{page.title}}](https://leetcode.com/problems/compare-version-numbers/){:target="_blank"}

    Compare two version numbers version1 and version2.
    If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

    You may assume that the version strings are non-empty and contain only digits and the . character.

    The . character does not represent a decimal point and is used to separate number sequences.

    For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level
    revision of the second first-level revision.

    You may assume the default revision number for each level of a version number to be 0. For example, version
    number 3.4 has a revision number of 3 and 4 for its first and second level revision number. Its third and
    fourth level revision number are both 0.

    Example 1:

    Input: version1 = "0.1", version2 = "1.1"
    Output: -1

    Example 2:

    Input: version1 = "1.0.1", version2 = "1"
    Output: 1

* easy

```java
public int compareVersion(String version1, String version2) {
    String[] arr1 = version1.split("\\."), arr2 = version2.split("\\.");
    int i = 0, j = 0;
    while(i < arr1.length || j < arr2.length) {
        int a = i < arr1.length ? Integer.valueOf(arr1[i]) : 0, b = j < arr2.length ? Integer.valueOf(arr2[j]) : 0;
        if(a < b) return -1;
        else if(a > b) return 1;

        i++;
        j++;
    }
    return 0;
}
```
