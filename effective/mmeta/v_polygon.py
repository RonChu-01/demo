# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/9/24.
# Copyright (c) 2019 3KWan.
# Description :


class ValidatePolygon(type):

    def __new__(meta, name, bases, class_dict):
        """
            type(object_or_name, bases, dict)
            type(object) -> the object's type
            type(name, bases, dict) -> a new type
        :param name: 类名
        :param bases: 父类的元组（针对继承的情况，可以为空）
        :param class_dict: 包含属性的字典（名称和值）
        :return:
        """
        if bases != (object,):
            if class_dict["sides"] < 3:
                raise ValueError("Polygon need 3+ sides")
        return type.__new__(meta, name, bases, class_dict)


class Polygon(object, metaclass=ValidatePolygon):
    sides = None

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180


class Triangle(Polygon):
    sides = 3


print("1------------")


class Line(Polygon):
    print("2------------")
    sides = 1
    print("3-------------")


# triangle = Triangle()

# line = Line()
