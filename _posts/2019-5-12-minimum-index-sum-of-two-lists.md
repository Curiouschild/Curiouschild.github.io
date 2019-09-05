---
title:  "599. Minimum Index Sum of Two Lists"
date:   2019-05-12 21:07:00 +0930
categories: Leetcode
tags: Easy HashMap
---

[{{page.title}}](https://leetcode.com/problems/minimum-index-sum-of-two-lists/){:target="_blank"}


    Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite j
    restaurants represented by strings.

    You need to help them find out their common interest with the least list index sum. If there is a choice
    tie between answers, output all of them with no order requirement. You could assume there always exists an
    answer.

    Example 1:

    Input:
    ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    Output: ["Shogun"]
    Explanation: The only restaurant they both like is "Shogun".

    Example 2:

    Input:
    ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    ["KFC", "Shogun", "Burger King"]
    Output: ["Shogun"]
    Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

    Note:

        The length of both lists will be in the range of [1, 1000].
        The length of strings in both lists will be in the range of [1, 30].
        The index is starting from 0 to the list length minus 1.
        No duplicates in both lists.



* HashMap

```java

public String[] findRestaurant(String[] list1, String[] list2) {
    String[] l = list1.length > list2.length ? list1 : list2;
    String[] s = l == list1 ? list2 : list1;
    HashMap<String, Integer> map = new HashMap<>();
    for(int i = 0; i < l.length; i++) {
        map.put(l[i], i);
    }
    ArrayList<String> temp = new ArrayList<>();
    int sum = Integer.MAX_VALUE;
    for(int i = 0; i < s.length; i++) {
        if(map.containsKey(s[i])) {
            if(i + map.get(s[i]) == sum) {
                temp.add(s[i]);
            } else if(i + map.get(s[i]) < sum) {
                temp.clear();
                temp.add(s[i]);
                sum = i + map.get(s[i]);
            }
        }
    }
    String[] result = new String[temp.size()];
    for(int i = 0; i < result.length; i++) result[i] = temp.get(i);
    return result;
}
```
