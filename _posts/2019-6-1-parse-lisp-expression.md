---
title:  "736. Parse Lisp Expression"
date:   2019-06-01 16:31:00 +0930
categories: Leetcode
tags: Hard String Recursive
---

[{{page.title}}](https://leetcode.com/problems/parse-lisp-expression/){:target="_blank"}

    You are given a string expression representing a Lisp-like expression to return the integer value of.

    The syntax for these expressions is given as follows.

    An expression is either an integer, a let-expression, an add-expression, a mult-expression, or an assigned
    variable. Expressions always evaluate to a single integer.

    (An integer could be positive or negative.)

    A let-expression takes the form (let v1 e1 v2 e2 ... vn en expr), where let is always the string "let",
    then there are 1 or more pairs of alternating variables and expressions, meaning that the first variable
    v1 is assigned the value of the expression e1, the second variable v2 is assigned the value of the
    expression e2, and so on sequentially; and then the value of this let-expression is the value of the
    expression expr.

    An add-expression takes the form (add e1 e2) where add is always the string "add", there are always two
    expressions e1, e2, and this expression evaluates to the addition of the evaluation of e1 and the
    evaluation of e2.

    A mult-expression takes the form (mult e1 e2) where mult is always the string "mult", there are always two
    expressions e1, e2, and this expression evaluates to the multiplication of the evaluation of e1 and the
    evaluation of e2.

    For the purposes of this question, we will use a smaller subset of variable names. A variable starts with
    a lowercase letter, then zero or more lowercase letters or digits. Additionally for your convenience, the
    names "add", "let", or "mult" are protected and will never be used as variable names.

    Finally, there is the concept of scope. When an expression of a variable name is evaluated, within the
    context of that evaluation, the innermost scope (in terms of parentheses) is checked first for the value
    of that variable, and then outer scopes are checked sequentially. It is guaranteed that every expression
    is legal. Please see the examples for more details on scope.

    Evaluation Examples:

    Input: (add 1 2)
    Output: 3

    Input: (mult 3 (add 2 3))
    Output: 15

    Input: (let x 2 (mult x 5))
    Output: 10

    Input: (let x 2 (mult x (let x 3 y 4 (add x y))))
    Output: 14
    Explanation: In the expression (add x y), when checking for the value of the variable x,
    we check from the innermost scope to the outermost in the context of the variable we are trying to evaluate.
    Since x = 3 is found first, the value of x is 3.

    Input: (let x 3 x 2 x)
    Output: 2
    Explanation: Assignment in let statements is processed sequentially.

    Input: (let x 1 y 2 x (add x y) (add x y))
    Output: 5
    Explanation: The first (add x y) evaluates as 3, and is assigned to x.
    The second (add x y) evaluates as 3+2 = 5.

    Input: (let x 2 (add (let x 3 (let x 4 x)) x))
    Output: 6
    Explanation: Even though (let x 4 x) has a deeper scope, it is outside the context
    of the final x in the add-expression.  That final x will equal 2.

    Input: (let a1 3 b2 (add a1 1) b2)
    Output 4
    Explanation: Variable names can contain digits after the first character.

    Note:
    The given string expression is well formatted: There are no leading or trailing spaces, there is only a single space separating different components of the string, and no space between adjacent parentheses. The expression is guaranteed to be legal and evaluate to an integer.
    The length of expression is at most 2000. (It is also non-empty, as that would not be a legal expression.)
    The answer and all intermediate calculations of that answer are guaranteed to fit in a 32-bit integer.

* recursion
  - end recursion when s is a variable or number
  - Otherwise read the operation and sub expression and go to next recursion

```java

class Solution {
    ArrayList<HashMap<String, Integer>> arr = new ArrayList<>();
    public int evaluate(String s) {
        // end of recursion
        Integer num = getNum(s);
        if(num != null) // a number
            return num;
        if(!s.contains("(")) // a variable
            return get(s);

        // flatten brackets
        int result = 0;
        HashMap<String, Integer> map = new HashMap<>();
        arr.add(map);
        s = s.substring(1, s.length()-1);
        if(s.substring(0,3).equals("add") || s.substring(0,4).equals("mult")) {
            int firstSpace = s.indexOf(" ");
            int l = 0, r = 0, i = firstSpace+1;
            while(i < s.length()) {
                if(l == r && s.charAt(i) == ' ') break;
                if(s.charAt(i) == '(') l++;
                if(s.charAt(i) == ')') r++;
                i++;
            }
            int secondSpace = i;
            String p1 = s.substring(firstSpace+1, secondSpace);
            String p2 = s.substring(secondSpace+1);
            if(s.substring(0,3).equals("add")) {
                result = evaluate(p1) + evaluate(p2);
            } else {
                result = evaluate(p1) * evaluate(p2);
            }
        } else { // let
            int start = s.indexOf(" ")+1;
            String key = "";
            int l = 0, r = 0, i = start, cnt = 0;
            while(i < s.length()) {
                if(l == r && s.charAt(i) == ' ') {
                    cnt++;
                    if((cnt & 1) == 1) {
                        key = s.substring(start, i);
                    } else {
                        int value = evaluate(s.substring(start, i));
                        map.put(key, value);
                    }
                    start = i+1;
                }
                if(s.charAt(i) == '(') l++;
                if(s.charAt(i) == ')') r++;
                i++;
            }
            result = evaluate(s.substring(start));
        }
        arr.remove(arr.size()-1);
        return result;
    }
    public Integer getNum(String s) {
        boolean isNum = true;
        int num = 0, start = 0;
        int sign = 1;
        if(s.charAt(0) == '-') {
            sign = -1;
            start = 1;
        }
        for(int i = start; i < s.length(); i++) {
            char c = s.charAt(i);
            if(Character.isDigit(c)) num = num * 10 + c - '0';
            else {
                isNum = false;
                break;
            }
        }
        if(isNum) return sign * num;
        else return null;
    }
    public int get(String key) {
        for(int i = arr.size()-1; i >= 0; i--) {
            if(arr.get(i).containsKey(key)) return arr.get(i).get(key);
        }
        return 0;
    }
  }
```
