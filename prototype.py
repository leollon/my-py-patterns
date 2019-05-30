#!/usr/bin/env python

"""
这个设计模式是关于什么？
这个设计模式的目的是减少一个应用所需要的类的数量。通过在运行时复制一个原型实例来创建对象而不是
依赖于子类。

这样做是有好处的，因为这样子可以很容易的派生出新对象类型，当这个类的实例只有一小部分状态组合的时候，
并且实例化过程消耗太大的时候。

这个例子做什么的？
当应用中的原型数量可能多样化的时候，有一个调度器（也就是说，注册器(Registry) 或者 管理器(Manager)）
是有好处的。这样就允许客户端在复制一个新的实例之前通过调度器查询原型。

下面提供了这样子的一个调度器，它包含了原型的三个副本: 'default', 'objecta', 和 'objectb'。

总而言之，就是通过复制原型来创建一个新的对象实例。
"""


class Prototype:
    value = "default"

    def clone(self, **attrs):
        """复制一个原型并且更新内部的属性字典"""
        # Python in Pratice, Mark Summerfield
        obj = self.__class__()
        obj.__dict__.update(attrs)
        return obj


class PrototypDispatcher:
    def __init__(self):
        self._objects = {}

    def get_objects(self):
        """获取所有的对象"""
        return self._objects

    def register_object(self, name, obj):
        """注册一个对象"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """注销一个对象"""
        del self._objects[name]


def main():
    prototype = Prototype()
    dispatcher = PrototypDispatcher()

    # 原型多样化
    d = prototype.clone()
    a = prototype.clone(value="a-value", category="a")
    b = prototype.clone(value="b-value", is_checked=True)

    # 通过调度器查询原型
    dispatcher.register_object("objecta", a)
    dispatcher.register_object("objectb", b)
    dispatcher.register_object("default", d)

    print([{n: p.value} for n, p in dispatcher.get_objects().items()])


if __name__ == "__main__":
    main()


#######Output#######
# [{'objecta': 'a-value'}, {'objectb': 'b-value'}, {'default': 'default'}]
