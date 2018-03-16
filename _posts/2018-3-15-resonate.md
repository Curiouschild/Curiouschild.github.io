---
title:  "Tech Test"
date:   2018-3-15 00:50:01 +0930
categories: Java
tags: Java
---


Answer For Internship
==
<!-- more -->

Basics:

1.

a. Software and websites need to provide service to multiple users simultaneously.

b. Users need to use multiple applications at one time.

c. Multi threaded programming provides efficiency when one thread is too slow (eg. I/O).

2.

When many functions require a variable.

When a variable's value does not change.

3.

Queue is a first-in-first-out data structure, while stack is a first-in-last-out structure.

4.

Array is a collection of items with index.

List is a collection of items with references one to another.
For example, if we have an array named arr and a list named list (single linked list whose head is firstItem), we can get an array item with arr.get(index) and an list item with firstItem.next.

A simple list item:

```java
class ListNode {
  int val;
  ListNode next;
  ListNode(int val) {
      this.val = val;
      this.next = null;
  }
}
```

You must know the size before creating an array.

List is more efficient when you need to remove items at the head of the collection frequently.

Array is more efficient when you need to search items at the middle and end of the collection frequently.

5.
```java
public ArrayList<Integer> getPrimeNumber(int max) {
  if (max <= 1) {
        throw new InvalidParameterException("Input number must be larger than 1");
    }
  ArrayList<Integer> result = new ArrayList<Integer>();
  out:for(int i=2;i<=max;i++) {
    for(int j=2;j<Math.sqrt(i) + 1;j++) {
      if(i%j==0) {
        continue out;
      }
    }
    result.add(i);
  }
  return result;
}
```

Level 100:

1.
```java
public LinkedList<Integer> removeDuplicates(Integer[] values) {
  if(values == null) {
    return null;
  }
  LinkedList<Integer> list = new LinkedList<Integer>(Arrays.asList(values));
  // use linkedhashset to remove duplicates
  LinkedHashSet<Integer> set = new LinkedHashSet<Integer>(list);
  return new LinkedList<Integer>(set);
}

```
2.
```java
public String getBase64(String json) {
  byte[] bytes = Base64.getEncoder().encode(json.getBytes());
  String result = new String(bytes);
  return result;
}

```
3.
```java
public boolean isUnique(String s) {
  if(s==null) {
    return fasle;
  }
  char[] arr = s.toCharArray();

  HashSet<Character> set = new HashSet<Character>();
  for (char c : arr) {
    if (!set.add(c)) {
      return false;
    }

  }
  return true;
}
```

4.

```java

public boolean isPermutation(String s1, String s2) {
		if (s1 == null || s2 == null) {
			return false;
		}
		HashMap<Character, Integer> map = new HashMap<Character, Integer>();

		// add first string to the map and count the number of each character
		for (char c : s1.toCharArray()) {
			if (map.containsKey(c)) {
				map.put(c, map.get(c) + 1);
			} else {
				map.put(c, 1);
			}
		}

		// iterate the second string and reduce the number of each character
		for (char c : s2.toCharArray()) {
			if (map.containsKey(c)) {
				map.put(c, map.get(c) - 1);
			} else {
				// there is a character that exists in the second string while not in the first
				// string
				return false;
			}
		}

		// is a permutation if the fianl number of each character is zero
		Iterator<Entry<Character, Integer>> it = map.entrySet().iterator();
		while (it.hasNext()) {
			Entry<Character, Integer> pair = it.next();
			if (pair.getValue() != 0) {
				return false;
			}
			System.out.println(pair.getKey() + " = " + pair.getValue());
		}

		return true;
	}

```
Level 200:    

```java

public int[] findLargestThreeSum(int[] inputArr) {
    if (inputArr.length < 9) {
        throw new InvalidParameterException("Input array must has no less than 9 numbers");
    }

    // test if the number in the input array could be divided by 3
    int groupNum = inputArr.length % 3 == 0 ? inputArr.length / 3 : (inputArr.length / 3) + 1;

    // add the sums to the group array
    int[] groups = new int[groupNum];
    for (int i = 0 ; i < groupNum - 1 ; i++) {
        groups[i] = inputArr[i * 3] + inputArr[i * 3 + 1] + inputArr[i * 3 + 2];
    }

    // add the last one, two or three sum to the groups
    int[] left = new int[inputArr.length - ((groupNum - 1) * 3)];
    System.arraycopy(inputArr, (groupNum - 1) * 3, left, 0, left.length);
    int lastSum = 0;
    for (int i = 0 ; i < left.length ; i++) {
        lastSum += left[i];
    }
    groups[groupNum - 1] = lastSum;

    // sort and get output
    int[] output = new int[3];
    Arrays.sort(groups);

    output[0] = groups[groupNum - 1];
    output[1] = groups[groupNum - 2];
    output[2] = groups[groupNum - 3];

    return output;
}

```

Real world problem:

<a class="twitter-timeline" data-tweet-limit="3" href="https://twitter.com/resonateAU">Tweets by resonateAU</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
