# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/9/24.
# Copyright (c) 2019 3KWan.
# Description :

import json


registers = {}


def register_class(target_class):
    """
    注册
    :param target_class:
    :return:
    """
    registers[target_class.__name__] = target_class


class Meta(type):
    """  元类 """

    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        register_class(cls)
        return cls


class Serializable(object):
    """  json序列化 """

    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({
            "class": self.__class__.__name__,
            "args": self.args
        })

    def __repr__(self):
        return "Serializable {0}: args->{1}".format(self.__class__, self.args)


class RegisterSerializable(Serializable, metaclass=Meta):
    pass


def deserialize(json_data):
    """
    反序列化
    :param json_data:
    :return:
    """
    params = json.loads(json_data)
    name = params["class"]
    target_class = registers[name]
    return target_class(*params["args"])


class Vector3D(RegisterSerializable):

    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.x = x
        self.y = y
        self.z = z


if __name__ == '__main__':
    v = Vector3D(2, 3, 5)
    print(v)
    before = v.serialize()
    print(before)
    after = deserialize(before)
    print(after)
