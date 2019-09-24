# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/9/24.
# Copyright (c) 2019 3KWan.
# Description :

import json


class Serializable(object):
    """  json序列化 """

    def __init__(self, *args):
        self.args = args

    def serialize(self, task_index):

        res = json.dumps({"{key}".format(key=task_index): self.args}, indent=4, ensure_ascii=False)

        with open("file.json", "w") as f:
            f.write(res)
        return res


class BetterSerializable(object):
    """  改进版json序列化 """

    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({
            "class": self.__class__.__name__,
            "args": self.args
        })

    def __repr__(self):
        return "BetterSerializable{0}".format(self.args)


class Deserializable(Serializable):
    """  json反序列化 """

    @classmethod
    def deserialize(cls, task_index, json_data):
        params = json.loads(json_data)
        return cls(*params["{key}".format(key=task_index)])


class Point2D(Serializable):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point2D {0} {1}".format(self.x, self.y)


class BetterPoint(Deserializable):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return "BetterPoint {0} {1}".format(self.x, self.y)


registers = {}


def register_class(target_class):
    registers[target_class.__name__] = target_class


def deserialize(json_data):
    params = json.loads(json_data)
    name = params["class"]
    target_class = registers[name]
    return target_class(*params["args"])


class EvenBetterSerializable(BetterSerializable):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y


register_class(EvenBetterSerializable)


if __name__ == '__main__':
    # point = Point2D(4, 5)
    # print(point)
    # print(point.serialize("1001"))
    #
    # b_point = BetterPoint(5, 3)
    # print(b_point)
    # task_index = "1002"
    # s_data = b_point.serialize(task_index)
    # print(s_data)
    # d_data = BetterPoint.deserialize(task_index, s_data)
    # print(d_data)
    #

    point = EvenBetterSerializable(5, 3)
    print(point)
    data = point.serialize()
    print(data)
    after = deserialize(data)
    print(after)
