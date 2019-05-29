#!/usr/bin/env python3
"""
Lazily-evaluated property pattern in Python

https://en.wikipedia.org/wiki/Lazy_evaluation

引用：
bottle 框架
https://github.com/bottlepy/bottle/blob/cafc15419cbb4a6cb748e6ecdccf92893bb25ce5/bottle.py#L270

Django 框架
https://github.com/django/django/blob/ffd18732f3ee9e6f0374aff9ccf350d85187fac2/django/utils/functional.py#L19

pip
https://github.com/pypa/pip/blob/cb75cca785629e15efb46c35903827b3eae13481/pip/utils/__init__.py#L821

pyramimd 框架
https://github.com/Pylons/pyramid/blob/7909e9503cdfc6f6e84d2c7ace1d3c03ca1d8b73/pyramid/decorator.py#L4

werkzeug: Flask web框架依赖的一个工具库
https://github.com/pallets/werkzeug/blob/5a2bf35441006d832ab1ed5a31963cbc366c99ac/werkzeug/utils.py#L35

综上所述，直到它们的值被需的时候，才对表达式进行求值，并且避免了重复求值。

"""
import functools


class lazy_property:
    def __init__(self, function):
        self.function = function
        functools.update_wrapper(self, function)

    def __get__(self, obj, _type):
        if obj is None:
            return self
        val = self.function(obj)
        obj.__dict__[self.function.__name__] = val
        return val


def lazy_property2(fn):
    attr = "_lazy__" + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr):
            setattr(self, attr, fn(self))
        return getattr(self, attr)

    return _lazy_property


class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        self.call_count2 = 0

    @lazy_property
    def relatives(self):
        # 获取所有的亲属关系，假设这个过程耗时很长。
        relatives = "Many relatives."
        return relatives

    @lazy_property2
    def parents(self):
        self.call_count2 += 1
        return "Father and mother"


def main():
    """
    >>> John = Person('John', 'Coder')

    >>> John.name
    'John'
    >>> John.occupation
    'Coder'

    # 在访问`relatives`之前
    >>> sorted(John.__dict__.items())
    [('call_count2', 0), ('name', 'John'), ('occupation', 'Coder')]

    >>> John.relatives
    'Many relatives.'

    # 访问`relatives`之后
    >>> sorted(John.__dict__.items())
    [('call_count2', 0), ('name', 'John'), ('occupation', 'Coder'), ('relatives', 'Many relatives.')]

    >>> John.parents
    'Father and mother'

    >>> sorted(John.__dict__.items())
    [('_lazy__parents', 'Father and mother'), ('call_count2', 1), ('name', 'John'), ('occupation', 'Coder'), ('relatives', 'Many relatives.')]

    >>> John.call_count2
    1

    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
