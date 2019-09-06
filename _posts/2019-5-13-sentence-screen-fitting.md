---
title:  "418. Sentence Screen Fitting"
date:   2019-05-13 16:09:00 +0930
categories: Leetcode
tags: Medium String
---

[{{page.title}}](https://leetcode.com/problems/sentence-screen-fitting/){:target="_blank"}

    Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the
    given sentence can be fitted on the screen.

    Note:

        A word cannot be split into two lines.
        The order of words in the sentence must remain unchanged.
        Two consecutive words in a line must be separated by a single space.
        Total words in the sentence won't exceed 100.
        Length of each word is greater than 0 and won't exceed 10.
        1 ≤ rows, cols ≤ 20,000.

    Example 1:

    Input:
    rows = 2, cols = 8, sentence = ["hello", "world"]

    Output:
    1

    Explanation:
    hello---
    world---

    The character '-' signifies an empty space on the screen.

    Example 2:

    Input:
    rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

    Output:
    2

    Explanation:
    a-bcd-
    e-a---
    bcd-e-

    The character '-' signifies an empty space on the screen.


* A good version from the discussion

great explanation:

https://leetcode.com/problems/sentence-screen-fitting/discuss/90845/21ms-18-lines-Java-solution/95272

Imagine an infinite sentence that are concatenated by words from the given sentence, infiStr. We want to cut the infiStr properly and put a piece at each row of the screen.
We maintain a pointer ptr. The ptr points to a position at infiStr, where next row will start. Cutting the infiStr and putting a piece at a row can be simulated as advancing the pointer by cols positions.
After advancing the pointer, if ptr points to a space, it means the piece can fit in row perfectly. If ptr points to the middle of a word, we must retreat the pointer to the beginning of the word, because a word cannot be split into two lines.


```java

public class Solution {
    public int wordsTyping(String[] sentence, int rows, int cols) {
        String s = String.join(" ", sentence) + " ";
        int start = 0, l = s.length();
        for (int i = 0; i < rows; i++) {
            start += cols;
            if (s.charAt(start % l) == ' ') {
                start++;
            } else {
                while (start > 0 && s.charAt((start-1) % l) != ' ') {
                    start--;
                }
            }
        }

        return start / s.length();
    }
}
```


```java

public int wordsTyping(String[] arr, int rows, int cols) {
    int result = 0, p = 0, r = 0, remain = cols;
    ArrayList<Integer> memo = new ArrayList<>();
    memo.add(0);
    while(r < rows) {
        if((remain == cols && remain >= arr[p].length()) || remain >= 1+arr[p].length()) { // enough space in this line
            remain -= remain == cols ? arr[p].length() : (1+arr[p].length());
            if(p+1 == arr.length) result++;
            p = (p+1) % arr.length;
        } else {
            r++;
            memo.add(result);
            if(p == 0) break;
            remain = cols;
        }
    }
    int mult = rows / r;
    result = mult * result + memo.get(rows - mult * r);
    return result;
}
```
