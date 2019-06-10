"""透明地重用村的具有相似/相同状态的对象的实例

这个设计模式是关于什么？
这个模式的目标是将程序运行时所需要的对象的数量u最小化。一个享元是通过多上下文进行共享的一个对象，
并且与非共享对象是可却分的。

享元的状态不应该被它的上下文影响到，这就是它的内部状态。从对象的的上下文将对象状态进行解偶，
从而允许享元能够被被共享。

这个例子干什么事情？
下面的例子建立一个存储初始化后的对象的'对象池'。当一张“Card”创建时，首先检查是否已经存在一张
“Card”而不是创建一张新的。这个是为了减少程序初始化对象的数量。

参考：
http://codesnipers.com/?q=python-flyweights
https://python-patterns.guide/gang-of-four/flyweight/


在Python生态系统中的例子
https://docs.python.org/3/library/sys.html#sys.intern

总而言之，享元模式描述的是使用其他相似的对象，通过共享数据来最小化内存使用
"""
import weakref


class Card:
    """享元"""

    # 可以是简单的字典
    # 使用WeakValueDictionary垃圾回收可以回收对象，当它没有其他引用的时候
    _pool = weakref.WeakValueDictionary()

    def __new__(cls, value, suit):
        # 如果对象存在在对象池中，则返回它
        obj = cls._pool.get(value + suit)
        # 否则，创建一个新的对象并将其放入对象池中
        if obj is None:
            obj = object.__new__(Card)
            cls._pool[value + suit] = obj
            # 这一行经常在`__init__`中经常看到的
            obj.value, obj.suit = value, suit
        return obj

    def __repr__(self):
        return "<Card: %s%s>" % (self.value, self.suit)


def main():
    """
    >>> c1 = Card('9', 'h')
    >>> c2 = Card('9', 'h')
    >>> c1, c2
    (<Card: 9h>, <Card: 9h>)
    >>> c1 is c2
    True
    >>> c1 == c2
    True
    
    >>> c1.new_attr = 'temp'  # Python 描述器协议
    >>> c3 = Card('9', 'h')
    >>> hasattr(c3, 'new_attr')
    True

    >>> Card._pool.clear()
    >>> c4 = Card('9', 'h')
    >>> hasattr(c4, 'temp')
    False
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
