---
title:  "929. Unique Email Addresses"
date:   2019-4-23 21:06:00 +0930
categories: Leetcode
tags: String
---

[{{page.title}}](https://leetcode.com/problems/rotate-image/){:target="_blank"}

    Every email consists of a local name and a domain name, separated by the @ sign.

    For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.

    Besides lowercase letters, these emails may contain '.'s or '+'s.

    If you add periods ('.') between some characters in the local name part of an email address, mail sent
    there will be forwarded to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule
    does not apply for domain names.)

    If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This
    allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.
    (Again, this rule does not apply for domain names.)

    It is possible to use both of these rules at the same time.

    Given a list of emails, we send one email to each address in the list.  How many different addresses
    actually receive mails?

    Example 1:

    Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    Output: 2
    Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails


```java

public void rotate(int[][] matrix) {
    int offset = 0;
    while(true) {
        if(matrix.length - offset * 2 <= 1) break;
        int far = matrix.length - 1 - offset;
        for(int j = offset; j < far; j++) {
            int temp = matrix[offset][j];
            matrix[offset][j] = matrix[far-(j-offset)][offset];
            matrix[far-(j-offset)][offset] = matrix[far][far-(j-offset)];
            matrix[far][far-(j-offset)] = matrix[j][far];
            matrix[j][far] = temp;
        }
        offset++;
    }
}
```


* Buffer array

```java

public int numUniqueEmails(String[] emails) {
    HashSet<String> set = new HashSet<>();
    for(String e : emails) {
        String[] localAndDomain = e.split("@");
        String local = localAndDomain[0].replaceAll("\\.", "");
        int index = local.indexOf("+");
        if(index > 0) local = local.substring(0, index);
        set.add(local+"@"+localAndDomain[1]);
    }
    return set.size();
}
```
