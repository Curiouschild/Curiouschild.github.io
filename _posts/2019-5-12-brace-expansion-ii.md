---
title:  "1096. Brace Expansion II"
date:   2019-05-12 18:53:00 +0930
categories: Leetcode
tags: Hard String
---

[{{page.title}}](https://leetcode.com/problems/brace-expansion-ii/){:target="_blank"}

    Under a grammar given below, strings can represent a set of lowercase words.  Let's use R(expr) to denote
    the set of words the expression represents.

    Grammar can best be understood through simple examples:

        Single letters represent a singleton set containing that word.
            R("a") = {"a"}
            R("w") = {"w"}
        When we take a comma delimited list of 2 or more expressions, we take the union of possibilities.
            R("{a,b,c}") = {"a","b","c"}
            R("{ {a,b},{b,c} }") = {"a","b","c"} (notice the final set only contains each word at most once)
        When we concatenate two expressions, we take the set of possible concatenations between two words
        where the first word comes from the first expression and the second word comes from the second
        expression.
            R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
            R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}

    Formally, the 3 rules for our grammar:

        For every lowercase letter x, we have R(x) = {x}
        For expressions e_1, e_2, ... , e_k with k >= 2, we have R({e_1,e_2,...}) = R(e_1) ∪ R(e_2) ∪ ...
        For expressions e_1 and e_2, we have R(e_1 + e_2) = {a + b for (a, b) in R(e_1) × R(e_2)}, where +
        denotes concatenation, and × denotes the cartesian product.

    Given an expression representing a set of words under the given grammar, return the sorted list of words
    that the expression represents.

    Example 1:

    Input: "{a,b}{c,{d,e} }"
    Output: ["ac","ad","ae","bc","bd","be"]

    Example 2:

    Input: "{ {a,z},a{b,c},{ab,z} }"
    Output: ["a","ab","ac","z"]
    Explanation: Each distinct word is written only once in the final answer.

    Constraints:

        1 <= expression.length <= 50
        expression[i] consists of '{', '}', ','or lowercase English letters.
        The given expression represents a set of words based on the grammar given in the description.



* Recursion

Spend too much time on this problem. Good thing is passing on first try.

```java

public List<String> braceExpansionII(String expression) {
    HashSet<String> set = divide(expression);
    ArrayList<String> result = new ArrayList<>(set);
    Collections.sort(result);
    return result;
}

public HashSet<String> divide(String expression) {
    // add or multiply ??? check the number of curly brackets
    HashSet<String> result = new HashSet<>();
    if(!expression.contains("{")) {
        result.add(expression);
        return result;
    }
    ArrayList<HashSet<String>> temp = new ArrayList<>();
    if(isAdd(expression)) {
        int pre = 1, i = 1, lc = 0, rc = 0;
        while(i < expression.length()-1) {
            char c = expression.charAt(i);
            if(c == '{') lc++;
            else if(c == '}') rc++;
            else if(c == ',' && lc == rc) {
                String sub = expression.substring(pre, i);
                HashSet<String> set = divide(sub);
                temp.add(set);
                pre = i+1;
            }
            i++;
        }
        String sub = expression.substring(pre, expression.length()-1);
        HashSet<String> set = divide(sub);
        temp.add(set);
        add(temp, result);
    } else {
        int pre = 0, i = 0, lc = 0, rc = 0;
        while(i < expression.length()) {
            char c = expression.charAt(i);
            if(c == '{') {
                if(rc == lc) {
                    String sub = expression.substring(pre, i);
                    HashSet<String> set = divide(sub);
                    temp.add(set);
                    pre = i;
                }
                lc++;
            }
            else if(c == '}') {
                rc++;
            } else if(lc > 0 && rc == lc && expression.charAt(i-1) == '}') {
                String sub = expression.substring(pre, i);
                HashSet<String> set = divide(sub);
                temp.add(set);
                pre = i;
            }
            i++;
        }
        String sub = expression.substring(pre, expression.length());
        HashSet<String> set = divide(sub);
        temp.add(set);
        multiply(temp, result, "", 0);
    }

    return result;
}

public boolean isAdd(String s) {
    int lc = 0, rc = 0;
    for(int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if(c == '{') lc++;
        else if(c == '}') rc++;
        else if(rc == lc) return false; // a single character outside brackets aaaa{}aaa{}
        if(lc > 0 && rc == lc && i < s.length()-1)  // {}{}{}
            return false;
    }
    return true; // { {},sdf{},sfd{}{} }
}

public void add(ArrayList<HashSet<String>> temp, HashSet<String> result) {
    HashSet<String> buffer = new HashSet<>();
    for(HashSet<String> set : temp) buffer.addAll(set);
    result.addAll(buffer);
}
public void multiply(ArrayList<HashSet<String>> temp, HashSet<String> result, String buffer, int curr) {
    if(curr == temp.size()) result.add(buffer);
    else {
        for(String s : temp.get(curr)) {
            multiply(temp, result, buffer+s, curr+1);
        }
    }
}
```
