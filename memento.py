"""生成一个能够被用于恢复到以前状态的不透明的记号
http://code.activestate.com/recipes/413838-memento-closure/

总而言之，提供恢复一个对象到以前状态的能力。
"""
from copy import copy
from copy import deepcopy


def memento(obj, deep=False):
    state = deepcopy(obj.__dict__) if deep else copy(obj.__dict__)  # 深拷贝或浅拷贝

    def restore():
        obj.__dict__.clear()  # 清除对象当前的状态
        obj.__dict__.update(state)  # 更新对象的状态

    return restore


class Transaction:
    """一个事务对象
    
    事实上，这只是围绕memento闭包的语法糖。
    """

    deep = False
    states = []

    def __init__(self, deep, *targets):
        self.deep = deep
        self.targets = targets
        self.commit()  # 初始化事务对象时，开始保留事务对象的起始状态

    def commit(self):
        self.states = [
            memento(target, self.deep) for target in self.targets
        ]  # restore函数对象列表

    def rollback(self):
        for a_state in self.states:
            a_state()  # 调用restore函数


class Transactional:
    """
    给方法加上事务语义。被@Transactional修饰的方法一旦产生异常，将回滚到进入时的状态。
    """

    def __init__(self, method):
        self.method = method

    def __get__(self, instance, owner_class):
        def transaction(*args, **kwargs):
            state = memento(instance)  # 记住实例当前的状态
            try:
                return self.method(instance, *args, **kwargs)  # 调用do_stuff方法
            except Exception as e:
                state()  # 调用restore函数
                raise e

        return transaction


class NumObj:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "<%s: %r>" % (self.__class__.__name__, self.value)

    def increment(self):
        self.value += 1

    @Transactional
    def do_stuff(self):
        self.value = "1111"  # <- 无效值
        self.increment()  # <- 将引起失败并且回滚


def main():
    """
    >>> num_obj = NumObj(-1)
    >>> print(num_obj, num_obj.do_stuff.__name__, type(num_obj.do_stuff))
    <NumObj: -1> transaction <class 'function'>

    >>> a_transaction = Transaction(True, num_obj)

    >>> try:
    ...     for i in range(3):
    ...         num_obj.increment()
    ...         print(num_obj)
    ...     a_transaction.commit()
    ...     print("-- committed")
    ...     for i in range(3):
    ...         num_obj.increment()
    ...         print(num_obj)
    ...     num_obj.value += "x"  # 失败
    ...     print(num_obj)
    ... except Exception:
    ...     a_transaction.rollback()
    ...     print("-- roll back")
    <NumObj: 0>
    <NumObj: 1>
    <NumObj: 2>
    -- committed
    <NumObj: 3>
    <NumObj: 4>
    <NumObj: 5>
    -- roll back

    >>> print(num_obj)
    <NumObj: 2>

    >>> print("-- now doing stuff ...")
    -- now doing stuff ...

    >>> try:
    ...     num_obj.do_stuff()
    ... except Exception:
    ...     print("-> doing stuff failed!")
    ...     import sys
    ...     import traceback
    ...     traceback.print_exc(file=sys.stdout)
    -> doing stuff failed!
    Traceback (most recent call last):
    ...
    TypeError: can only concatenate str (not "int") to str

    >>> print(num_obj)
    <NumObj: 2>
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

