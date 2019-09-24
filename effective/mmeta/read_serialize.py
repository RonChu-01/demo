# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/9/24.
# Copyright (c) 2019 3KWan.
# Description :

import json

from local_serialize import deserialize


if __name__ == '__main__':
    with open("local.json", "r") as f:
        before = json.loads(f.read())
        print(before)
        after = deserialize(before)
        print(after)
        print(after.param_info.get("keystore_name"))
