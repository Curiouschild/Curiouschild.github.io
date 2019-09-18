---
title:  "271. Encode and Decode Strings"
date:   2019-05-25 23:36:00 +0930
categories: Leetcode
tags: Medium String Design
---

[{{page.title}}](https://leetcode.com/problems/encode-and-decode-strings/){:target="_blank"}

    Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

    Machine 1 (sender) has the function:

    string encode(vector<string> strs) {
    // ... your code
    return encoded_string;
    }

    Machine 2 (receiver) has the function:

    vector<string> decode(string s) {
    //... your code
    return strs;
    }

    So Machine 1 does:

    string encoded_string = encode(strs);

    and Machine 2 does:

    vector<string> strs2 = decode(encoded_string);

    strs2 in Machine 2 should be the same as strs in Machine 1.

    Implement the encode and decode methods.



    Note:

      The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
      Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
      Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.



* Like encoding and decoding a tcp head

len + content

9 decimal for len becasue the len of a string has 9 or less digit; offset with 0

```java

public class Codec {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        if(strs.size() == 0) return null;
        StringBuilder sb = new StringBuilder();
        for(String s : strs) {
            StringBuilder len = new StringBuilder();
            int l = s.length();
            int cnt = 0;
            while(l > 0) {
                cnt++;
                l = l / 10;
            }
            // System.out.println(cnt);
            for(int i = 0; i < 9-cnt; i++) {
                len.append('0');
            }
            if(cnt > 0)
                len.append(s.length());
            sb.append(len).append(s);
        }
        return sb.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String encoded) {
        List<String> result = new ArrayList<>();
        if(encoded == null) return result;
        // System.out.println(encoded);
        int i = 0;
        while(i < encoded.length()) {
            int len = Integer.valueOf(encoded.substring(i, i+9));
            i += 9;
            String word = encoded.substring(i, i+len);
            i += len;
            result.add(word);
        }
        return result;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(strs));
```
