"""遍历一个容器并且访问容器中的元素
使用生成器实现迭代器模式

总而言之
"""
from abc import ABCMeta, abstractmethod


def count_to(count):
    """通过单词数量计数，最高可达五个"""
    numbers = ["one", "two", "three", "four", "five"]
    for number in numbers[:count]:
        yield number


# 测试生成器
count_to_two = lambda: count_to(2)
count_to_five = lambda: count_to(5)


class AbstractIterator(metaclass=ABCMeta):
    """抽象迭代器类
    
    实现一个抽象迭代器类
    """

    @abstractmethod
    def has_next(self):
        raise NotImplementedError

    @abstractmethod
    def next(self):
        raise NotImplementedError

    @abstractmethod
    def get_value(self):
        raise NotImplementedError


class ConcreteIterator(AbstractIterator):
    def __init__(self, container):
        self._container = container
        self._count = len(container)
        self._index = 0

    def next(self):
        if self.has_next():
            self._index += 1

    def get_value(self):
        return self._container[self._index]

    def has_next(self):
        return self._index < self._count


def main():
    """
    # 计数为两个
    >>> for number in count_to_two():
    ...     print(number)
    one
    two

    # 计数为五
    >>> for number in count_to_five():
    ...     print(number)
    one
    two
    three
    four
    five

    # 测试用使用类实现的迭代器
    >>> aggregate = ["one", "two", "three", "four", "five"]
    >>> it = ConcreteIterator(aggregate)
    >>> while it.has_next():
    ...    print(it.get_value())
    ...    it.next()
    one
    two
    three
    four
    five
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
