#!/usr/bin/env python3
"""
这个设计模式是关于什么的？
适配器模式给一个类提供不同的接口。我们可以将其视为一种电线适配器，允许在具有不同形状插座的地方
为手机充电。跟着这个观点，适配器模式可用于集成那些由于它们的不兼容接口不能被集成的类。

这个例子干什么事情？

这个例子有一些用于表示能够付出不同声音的实体（Dog, Cat, Human, Car）的类。适配器类提供不同
的接口给能发出声音的的原始方法。所以，原始接口（例如，bark 和 meow）都在不同的名字下是可供
调用：make_noise。

实际中该模式使用在什么地方？
Grok 框架使用适配器使得对象能够很好地和一个特殊的API工作而不用修改对象自己：


参考：
http://ginstrom.com/scribbles/2008/11/06/generic-adapter-class-in-python/
https://sourcemaking.com/design_patterns/adapter
http://python-3-patterns-idioms-test.readthedocs.io/en/latest/ChangeInterface.html#adapter


总而言之，就是允许一个存在的类的接口当作另外接口来世使用。
"""


class Dog:
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof!"


class Cat:
    def __init__(self):
        self.name = "Cat"

    def meow(self):
        return "meow!"


class Human:
    def __init__(self):
        self.name = "Human"

    def speak(self):
        return "'hello'"


class Car:
    def __init__(self):
        self.name = "Car"

    def make_noise(self, octane_level):
        return "vroom{0}".format("!" * octane_level)


class Adapter:
    """
    通过替换方法来适配一个对象。
    使用：
    dog = Dog()
    dog = Adapter(dog, make_noise=dog.bark)
    """

    def __init__(self, obj, **adapted_methods):
        """在对象的字典中设置适配的方法"""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """所有未适配的调用都传递给对象"""
        return getattr(self.obj, attr)

    def original_dict(self):
        """打印原来对象的字典"""
        return self.obj.__dict__


def main():
    """
    >>> objects = []
    >>> dog = Dog()
    >>> print(dog.__dict__)
    {'name': 'Dog'}

    >>> objects.append(Adapter(dog, make_noise=dog.bark))

    >>> objects[0].__dict__['obj'], objects[0].__dict__['make_noise']
    (<...Dog object at 0x...>, <bound method Dog.bark of <...Dog object at 0x...>>)

    >>> print(objects[0].original_dict())
    {'name': 'Dog'}

    >>> cat = Cat()
    >>> objects.append(Adapter(cat, make_noise=cat.meow))
    >>> human = Human()
    >>> objects.append(Adapter(human, make_noise=human.speak))
    >>> car = Car()
    >>> objects.append(Adapter(car, make_noise=lambda: car.make_noise(3)))

    >>> for obj in objects:
    ...    print("A {0} goes {1}".format(obj.name, obj.make_noise()))
    A Dog goes woof!
    A Cat goes meow!
    A Human goes 'hello'
    A Car goes vroom!!!
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
