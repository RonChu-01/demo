# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/9/24.
# Copyright (c) 2019 3KWan.
# Description :

from local_serialize import deserialize


def exec_deserialize(file):
    """
    执行反序列化（还原对象）
    :param file:
    :return:
    """
    with open(file, "r") as f:
        data = f.read()
        obj = deserialize(data)
        return obj


if __name__ == '__main__':
    ret = exec_deserialize("local.json")
    print(ret.param_info)
