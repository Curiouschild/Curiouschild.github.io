---
title:  "68. Text Justification"
date:   2019-3-17 23:11:44 +0930
categories: Leetcode
tags: String
---

[{{page.title}}](https://leetcode.com/problems/text-justification/){:target="_blank"}

    Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

    You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

    Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

    For the last line of text, it should be left justified and no extra space is inserted between words.

    Note:

    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.

    Example 1:

    Input:
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    Output:
    [
    "This    is    an",
    "example  of text",
    "justification.  "
    ]

    Example 2:

    Input:
    words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16
    Output:
    [
    "What   must   be",
    "acknowledgment  ",
    "shall be        "
    ]
    Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.



```java
public List<String> fullJustify(String[] words, int max) {
        List<String> result = new ArrayList<>();
        int len = 0;
        int j = 0;
        for(int i = 0; i < words.length; i++) {
            String w = words[i];
            if(len + w.length() > max) { // give up current word, process words between j and i-1 (inclusive)
                // words j -> i-1
                int wCnt = i - j;
                int spaceSlot = wCnt - 1;
                int remain = max - (len - 1) + spaceSlot; // number of empty spaces to be added
                String temp = "";
                if(spaceSlot > 0) { // if multiple words in a line
                    int spaceCnt = 0;
                    while(spaceCnt < remain) {
                        for(int k = j; k <= i-2; k++) {
                            words[k] += " ";
                            spaceCnt++;
                            if(spaceCnt == remain) break;
                        }
                    }
                    for(int k = j; k <= i-2; k++) temp += words[k];
                }
                temp += words[i-1];
                if(spaceSlot == 0) { // if only one word in this line, add trailing spaces
                    for(int space = 0; space < remain; space++)
                        temp += " ";
                }
                result.add(temp);
                j = i;
                i--; // give up current word
                len = 0;
                continue;
            }
            len += w.length() + 1;
        }
        String temp = ""; // process last line
        while(j < words.length - 1) temp += words[j++] + " ";
        temp += words[j];
        int trailingSpace = max - len + 1;
        for(int i = 0; i < trailingSpace; i++) temp += " ";
        result.add(temp);
        return result;
    }
```

Anoter version

```java
public List<String> fullJustifyOld(String[] words, int maxWidth) {
    List<String> result = new ArrayList<>();
    StringBuilder sb = new StringBuilder();
    int length = 0;
    for(int i = 0; i < words.length; i++) {
        String curr = words[i];
        if(sb.length() == 0) sb.append(curr);
        else if(sb.length() + 1 + curr.length() <= maxWidth) {
            sb.append(" ").append(curr);
        } else {
            i--;
            String[] ws = sb.toString().split(" ");
            int slot = ws.length - 1;
            if(slot == 0) {
                int space = maxWidth - sb.length();
                for(int j = 0; j < space; j++) sb.append(" ");
                result.add(sb.toString());
                sb.setLength(0);
                continue;
            }
            int trail = maxWidth - sb.length();
            int total = slot + trail;
            int between = total / slot;
            int residual = total % slot;
            sb.setLength(0);
            for(int j = 0; j < ws.length; j++) {
                sb.append(ws[j]);
                if(j == ws.length - 1) break;
                for(int k = 0; k < between; k++) sb.append(" ");
                if(residual-- > 0) sb.append(" ");
            }
            result.add(sb.toString());
            sb.setLength(0);
        }
    }
    if(sb.length() > 0) {
        int space = maxWidth - sb.length();
        for(int i = 0; i < space; i++) sb.append(" ");
        result.add(sb.toString());
    }
    return result;
}
```
