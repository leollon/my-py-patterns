"""为一个集合的所有项调用回调

表示在一个对象结构的元素上被执行的操作。访问者模式可以让你定义一个用于操作元素的类的新操作而不用
改变元素的类。

http://peter-hoffmann.com/2010/extrinsic-visitor-pattern-python-inheritance.html

总而言之，将算法与其操作的对象结构分开。

一个有趣的例子能够在下面被找到
Brian Jones, David Beazley "Python Cookbook" (2013):
- "8.21. Implementing the Visitor Pattern"
- "8.22. Implementing the Visitor Pattern Without Recursion"

在Python中的例子：
- Python's ast.objVisitor: https://github.com/python/cpython/blob/master/Lib/ast.py#L250

在`pyflakes`这样子的工具中使用。
- `Black` 代码格式化工具实现的版本：https://github.com/ambv/black/blob/master/black.py#L718
"""


class obj:
    pass


class A(obj):
    pass


class B(obj):
    pass


class C(A, B):
    pass


class Visitor:
    """访问者"""

    def visit(self, obj, *args, **kwargs):
        meth = None
        for cls in obj.__class__.__mro__:
            meth_name = (
                "visit_" + cls.__name__
            )  # visit_A, visit_B, visit_C 三者之一
            meth = getattr(self, meth_name, None)
            if meth:
                break

        if not meth:
            meth = self.generic_visit
        return meth(obj, *args, **kwargs)

    def generic_visit(self, obj, *args, **kwargs):
        print("generic_visit " + obj.__class__.__name__)

    def visit_B(self, obj, *args, **kwargs):
        print("visit_B " + obj.__class__.__name__)


def main():
    """
    >>> a, b, c = A(), B(), C()
    >>> visitor = Visitor()

    >>> visitor.visit(a)
    generic_visit A

    >>> visitor.visit(c)
    visit_B C
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
