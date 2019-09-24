# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/9/23.
# Copyright (c) 2019 3KWan.
# Description :

from collections import defaultdict

words = ["hello", "world", "test", "dev", "project"]

count = defaultdict(lambda: 0)

for word in words:
    count[word] += 1

print(count)
