---
title:  "635. Design Log Storage System"
date:   2019-4-23 20:52:00 +0930
categories: Leetcode
tags: TreeMap
---

[{{page.title}}](https://leetcode.com/problems/design-log-storage-system/){:target="_blank"}

    You are given several logs that each log contains a unique id and timestamp. Timestamp is a string that has
    the following format: Year:Month:Day:Hour:Minute:Second, for example, 2017:01:01:23:59:59. All domains are
    zero-padded decimal numbers.

    Design a log storage system to implement the following functions:

    void Put(int id, string timestamp): Given a log's unique id and timestamp, store the log in your storage system.

    int[] Retrieve(String start, String end, String granularity): Return the id of logs whose timestamps are
    within the range from start to end. Start and end all have the same format as timestamp. However,
    granularity means the time level for consideration. For example, start = "2017:01:01:23:59:59", end =
    "2017:01:02:23:59:59", granularity = "Day", it means that we need to find the logs within the range from
    Jan. 1st 2017 to Jan. 2nd 2017.

    Example 1:

    put(1, "2017:01:01:23:59:59");
    put(2, "2017:01:01:22:59:59");
    put(3, "2016:01:01:00:00:00");
    retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"); // return [1,2,3], because you need to return
    all logs within 2016 and 2017.
    retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"); // return [1,2], because you need to return
    all logs start from 2016:01:01:01 to 2017:01:01:23, where log 3 is left outside the range.

    Note:

        There will be at most 300 operations of Put or Retrieve.
        Year ranges from [2000,2017]. Hour ranges from [00,23].
        Output for Retrieve has no order required.

* TreeMap

```java

TreeMap<String, ArrayList<Integer>> map = new TreeMap<>();
HashMap<String, Integer> dict = new HashMap<>();
public LogSystem() {
    dict.put("Year", 0);
    dict.put("Month", 1);
    dict.put("Day", 2);
    dict.put("Hour", 3);
    dict.put("Minute", 4);
    dict.put("Second", 5);
}

public void put(int id, String timestamp) {
    ArrayList<Integer> arr = map.getOrDefault(timestamp, new ArrayList<Integer>());
    arr.add(id);
    map.put(timestamp, arr);
}

public List<Integer> retrieve(String s, String e, String gra) {
    List<Integer> result = new ArrayList<>();
    int i = dict.get(gra);
    String min = s.substring(0, i * 3 + 4), max = e.substring(0, i * 3 + 4);
    max += ":9"; // :9 is the largest lexicographically
    for(ArrayList<Integer> ids : map.subMap(min, max).values())
        result.addAll(ids);
    return result;
}
```
