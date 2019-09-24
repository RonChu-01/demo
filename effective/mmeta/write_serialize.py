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
        # 在元类中执行注册操作
        register_class(cls)
        return cls


class Serializable(object):
    """  json序列化 """

    def __init__(self, *args):
        self.args = args

    def serialize(self):
        res = json.dumps({
            "class": self.__class__.__name__,
            "args": self.args
        }, indent=4, ensure_ascii=False)

        with open("local.json", "w") as f:
            f.write(res)

        return res

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
    # 返回类实例对象
    return target_class(*params["args"])


class ModUpload(RegisterSerializable):
    """  测试mod """

    def __init__(self, param_info):
        super().__init__(param_info)
        self.param_info = param_info


if __name__ == '__main__':
    params_info = {
        "keystore_name": "qxjh_3k.keystore",
        "common_sdk_version": "1.3.0",
        "channel_version": "",
        "is_old": "0",
        "is_online": "1",
        "common_params": {
            "package_game_new": [
                {
                    "CONSOLE_GAME_COMMON_PACKAGE_ID": "2",
                    "CONSOLE_GAME_COMMON_GAME_ID": "2",
                    "CONSOLE_GAME_CHANNEL_ID": "4"
                }
            ],
            "package_game_old": []
        }
    }

    mod = ModUpload(params_info)
    print(mod)
    before = mod.serialize()
    print(before)

