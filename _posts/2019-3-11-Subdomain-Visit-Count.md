---
title:  "811. Subdomain Visit Count"
date:   2019-3-11 09:05:20 +0930
categories: Leetcode
tags: HashMap String
---

[{{page.title}}](https://leetcode.com/problems/subdomain-visit-count/){:target="_blank"}

    A website domain like "discuss.leetcode.com" consists of various subdomains.
    At the top level, we have "com", at the next level, we have "leetcode.com",
    and at the lowest level, "discuss.leetcode.com". When we visit a domain like
    "discuss.leetcode.com", we will also visit the parent domains "leetcode.com"
    and "com" implicitly.

    Now, call a "count-paired domain" to be a count (representing the number of
    visits this domain received), followed by a space, followed by the address.
    An example of a count-paired domain might be "9001 discuss.leetcode.com".

    We are given a list cpdomains of count-paired domains. We would like a list
    of count-paired domains, (in the same format as the input, and in any order),
    that explicitly counts the number of visits to each subdomain.

    Example 1:
    Input:
    ["9001 discuss.leetcode.com"]
    Output:
    ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
    Explanation:
    We only have one website domain: "discuss.leetcode.com". As discussed above,
    the subdomain "leetcode.com" and "com" will also be visited. So they will all
    be visited 9001 times.


* Recursive

```java
public List<String> subdomainVisits(String[] cpdomains) {
    HashMap<String, Integer> map = new HashMap<>();
    for(String p : cpdomains) {
        String[] cp = p.split(" ");
        String[] ds = cp[1].split("\\.");
        String temp = "";
        for(int i = ds.length - 1; i >= 0; i--) {
            temp = ds[i] + (i == ds.length - 1 ? "" : ".") + temp;
            int v = map.getOrDefault(temp, 0);
            map.put(temp, v + Integer.valueOf(cp[0]));
        }
    }
    List<String> result = new ArrayList<>();
    map.forEach((k,v)-> result.add(v + " " + k));
    return result;
}
```
