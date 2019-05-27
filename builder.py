#!/usr/bin/env python3.6
"""
这个模式是关于什么的？
将复杂对象的创建进行解偶和它的表现形式，
目的是从同样的家族中重新使用同样的进程建立对象。
这样子做的好处是当你必须将一个对象的规范从它的实际表现形式（通常是抽象的）分离开来。

这个例子干什么？

第一个例子是通过使用一个抽象基类来建立而实现，其中初始化过程(__init__ 方法)指定了所需要的步骤
和具体子类要实现这些步骤。

在其他编程语言中，有时候，有必要提供更加复杂配置。特别是，在 C++中的一个构造函数中不能有多态行为。
更多信息查看链接https://stackoverflow.com/questions/1453131/how-can-i-get-polymorphic-behavior-in-a-c-constructor

意味着使用Python也不会奏效。多态行为需要通过一个已经由另外一个类构造的外部实例来提供。

总体而言，在Python中，这样子没必要，但是也是包含了第二个例子来表现这种配置。

在实际中，这个设计模式用在什么地方？

引文
https://sourcemaking.com/design_patterns/builder

原文太长了，总而言之，将一个复杂对象的创建与其表现形式进行解偶。
"""

# Abstract building
class Building:
    def __init__(self):
        self.build_floor()
        self.build_size()

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError

    def __str__(self):
        return f"Floor: {self.floor} | Size: {self.size}"


# 实际建立
class House(Building):
    def build_floor(self):
        self.floor = "One"

    def build_size(self):
        self.size = "Big"


class Flat(Building):
    def build_floor(self):
        self.floor = "More than One"

    def build_size(self):
        self.size = "Small"


# 在一些更加复杂的案例中，可能需要将建立过程中的逻辑抽出放入到另外一个函数中(或者另外一个类的
# 一个方法), 而不是在基类的`__init__`中。（这就出现一个实际的类中没有一个有用的构造函数的
# 奇怪情况）


class ComplexBuilding:
    def __str__(self):
        return f"Floor: {self.floor} | Size: {self.size}"


class ComplexHouse(ComplexBuilding):
    def build_floor(self):
        self.floor = "One"

    def build_size(self):
        self.size = "Big and fancy"


def construct_building(klass):
    building = klass()
    building.build_floor()
    building.build_size()
    return building


# 客户端代码
if __name__ == "__main__":
    house = House()
    print(house)
    flat = Flat()
    print(flat)

    # 使用外部构造函数:
    complex_house = construct_building(ComplexHouse)
    print(complex_house)

######## OUTPUT ########
# Floor: One | Size: Big
# Floor: More than One | Size: Small
# Floor: One | Size: Big and fancy
