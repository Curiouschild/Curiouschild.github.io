---
title:  "First Map Reduce"
date:   2018-2-1 14:26:01 +0930
categories: CloudComputing
tags: CC
---

This my first attempt on MapReduce. My purpose is to analyse 170 TB Wikipedia pageview data. A single personal computer is not capable to process a dataset with such a volume. So I take help from AWS. Below is my simple mapper and reducer.
<!-- more -->

Map
```python
#!/usr/bin/env python3
# -*- coding: <utf-8> -*-

import os
import sys
import os.path
import gzip
import re
from collections import Counter


def decode(encoded):
    def getHexValue(b):
        if '0' <= b <= '9':
            return chr(ord(b) - 0x30)
        elif 'A' <= b <= 'F':
            return chr(ord(b) - 0x37)
        elif 'a' <= b <= 'f':
            return chr(ord(b) - 0x57)
        return None

    if encoded is None:
        return None
    encodedChars = encoded
    encodedLength = len(encodedChars)
    decodedChars = ''
    encodedIdx = 0
    while encodedIdx < encodedLength:
        if encodedChars[encodedIdx] == '%' and encodedIdx + 2 < encodedLength and getHexValue(encodedChars[encodedIdx + 1]) and getHexValue(encodedChars[encodedIdx + 2]):
            #  current character is % char
            value1 = getHexValue(encodedChars[encodedIdx + 1])
            value2 = getHexValue(encodedChars[encodedIdx + 2])
            decodedChars += chr((ord(value1) << 4) + ord(value2))
            encodedIdx += 2
        else:
            decodedChars += encodedChars[encodedIdx]
        encodedIdx += 1
    return str(decodedChars)

# black list of extensions
blacklist_extension = [".png", ".gif", ".jpg", ".jpeg", ".tiff", ".tif", ".xcf", ".mid", ".ogg", ".ogv", ".svg", ".djvu", ".oga", ".flac", ".opus", ".wav", ".webm", ".ico", ".txt"]

# black list of domains
blacklist_domain = ["user_talk:","wikipedia:","wikipedia_talk:","file:","file_talk:","mediawiki:","mediawiki_talk:","template:","template_talk:","help:","help_talk:","category:","category_talk:","portal:","portal_talk:","book:","book_talk:","draft:","draft_talk:","education_program:","education_program_talk:","timedtext:","timedtext_talk:","module:","module_talk:","gadget:","gadget_talk:","gadget_definition:","gadget_definition_talk:"]

# black list of special pages
blacklist_special = ["404.php", "Main_Page", "-"]

diction = Counter()

# filter black lists
def filter(line):

    line = line.replace("\n", "")

    arr = line.split()

    if(len(arr) != 4):
        return True

    arr[1] = decode(arr[1])

    # conditions
    if arr[0] in ['en', 'en.m'] and len(arr) == 4  and not ('a' <= arr[1][0] <= 'z') and not any(arr[1].lower().startswith(prefix) for prefix in blacklist_domain) and not any(arr[1].lower().endswith(extension) for extension in blacklist_extension) and not arr[1].lower().endswith("_(disambiguation)") and not arr[1] in blacklist_special:
        diction[arr[1]] += int(arr[2])
    return True

# read file
# con = read_file('pageviews-20161109-000000')

# filter data
# for line in con:
#     if not filter(line):
#         break

for line in sys.stdin:
    if not filter(line):
        break

file_name = os.environ["mapreduce_map_input_file"]
# file_name = "s3://cmucc-datasets/wikipediatraf/201611/pageviews-20161109-000000.gz"
file_name_parse = file_name.split("-")
date = file_name_parse[2]


for key,view in diction.items():
    value = str(view) + "-" + date
    print('%s\t%s\t' % (key, value))

```
Reduce
```python
#!/usr/bin/env python3

from operator import itemgetter
from collections import Counter
import sys

current_word = None
total_count = 0
day_count = 0
days = Counter()
for x in range(20161101,20161131):
    days[x] = 0

word = None

for line in sys.stdin:
    line = line.strip()
    if line == "":
        continue

    word, value = line.split('\t', 1)

    value_parse = value.split("-")
    count = value_parse[0]

    try:
        count = int(count)
        day = int(value_parse[1])
    except ValueError:
        print("parse error")
        continue

    if current_word == word:
        total_count += count
        days[day] += count
    else:
        day_data = ""
        if current_word:
            if total_count > 100000:
                for x in range(20161101,20161131):
                    day_data += (str(days[x]) + "\t")

                print('%s\t%s\t%s' % (total_count, current_word, day_data[:-1]))

        days = Counter()
        for x in range(20161101,20161131):
            days[x] = 0

        total_count = count
        days[day] = count
        current_word = word

if current_word == word:
    day_data = ""
    if total_count > 100000:
        for x in range(20161101,20161131):
            day_data += (str(days[x]) + "\t")
        print('%s\t%s\t%s' % (total_count, current_word, day_data[:-1]))

```
