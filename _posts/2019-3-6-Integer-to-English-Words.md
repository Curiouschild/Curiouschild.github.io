---
title:  "273. Integer to English Words"
date:   2019-3-6 022:32:25 +0930
categories: Leetcode
tags: Math
---

[{{page.title}}](https://leetcode.com/problems/integer-to-english-words/){:target="_blank"}

    Convert a non-negative integer to its english words representation.
    Given input is guaranteed to be less than 231 - 1.

    Case:
    Input: 1234567
    Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"


```java
    String[] dict = {"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven"
                     , "Eight", "Nine", "Ten", "Eleven", "Twelve",
                     "Thirteen", "Fourteen", "Fifteen", "Sixteen",
                     "Seventeen", "Eighteen", "Nineteen", "Twenty"};
    String[] tens = {"Zero", "Ten", "Twenty", "Thirty", "Forty",
                    "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
    String[] suffixs = {"", "Thousand", "Million", "Billion"};

    public String numberToWords(int num) {
        if(num <= 20) return dict[num];
        StringBuilder sb = new StringBuilder();
        int cnt = 0;
        while(num > 0) {
            String prefix = three(num - num / 1000 * 1000).trim();
            if(prefix.length() != 0) {
                String suffix = ((suffixs[cnt].length() == 0) ? "" : " " + suffixs[cnt] + (sb.length() == 0 ? "" : " "));
                prefix += suffix;
            }
            cnt++;
            num /= 1000;
            sb.insert(0, prefix);
        }
        return sb.toString();
    }

    public String three(int num) {
        StringBuilder sb = new StringBuilder();
        if(num > 99) { // hundred
            sb.append(dict[num / 100]).append(" ").append("Hundred ");
            num -= num / 100 * 100;
        }
        if(num > 20) { // tens
            sb.append(tens[num / 10] + " ");
            num -= num / 10 * 10;
            if(num != 0) {
                sb.append(dict[num] + " ");
            }
        } else if(num != 0) { // ones
            sb.append(dict[num] + " ");
        }
        return sb.toString();
    }
```
