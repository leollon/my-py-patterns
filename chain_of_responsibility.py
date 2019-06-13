"""应用连续的处理程序链来处理数据

这个设计模式是关于什么的?

责任链是一个`if elif elif else ...`语法的面向对象的版本，具有运行时动态重新
排列和重新配置的条件动作语句块的优势。

该设计模式的目的是通过允许请求通过链状接收器直到被处理来将请求发送器从请求接收器中解偶出来。

请求接收器用简单的形式保留一个单独的继承者的引用。作为变型一些接收器可能在几个方向上将请求发送出去，
形成一棵责任树。

总而言之，允许一个请求沿请求接收器链向下传递直到请求被处理。
"""
import abc


class Handler(metaclass=abc.ABCMeta):
    """抽象类，不可以用于实例一个对象"""

    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        """
        处理请求并停止。
        如果不能处理，调用链状中的下一个请求处理程序。

        可能调用下一个处理程序的时候，请求处理成功了作为第二种选择。
        """
        res = self.check_range(request)
        if not res and self.successor:
            self.successor.handle(request)

    @abc.abstractmethod
    def check_range(self, request):
        """比较传递的值和预先定义的间隔
        
        子类必须实现抽象方法。
        """


class ConcreteHandler0(Handler):
    """每个处理程序可能不相同。
    保持简单和静态...
    """

    @staticmethod
    def check_range(request):
        if 0 <= request <= 10:
            print("request {} handled in handler 0".format(request))
            return True


class ConcreteHandler1(Handler):
    """使用自己的内部状态"""

    start, end = 10, 20

    def check_range(self, request):
        if self.start <= request < self.end:
            # 对象自己的内部状态
            print("request {} handled in heandler 1".format(request))
            return True


class ConcreteHandler2(Handler):
    """使用助手方法。"""

    def check_range(self, request):
        start, end = self.get_interval_from_db()  # 使用助手方法
        if start <= request < end:
            print("request {} handled in handler 2".format(request))
            return True

    @staticmethod
    def get_interval_from_db():
        """助手方法"""
        return (20, 30)


class FallbackHandler(Handler):
    @staticmethod
    def check_range(request):
        print("end of chain, no handler {}".format(request))
        return False


def main():
    """
    >>> h0 = ConcreteHandler0()
    >>> h1 = ConcreteHandler1()
    >>> h2 = ConcreteHandler2()
    >>> h3 = FallbackHandler()
    >>> h0.successor = h1
    >>> h1.successor = h2
    >>> h2.successor = h3


    >>> requests = [2, 5, 14, 22, 18, 3, 35, 27, 20]
    >>> for request in requests:
    ...     h0.handle(request)
    request 2 handled in handler 0
    request 5 handled in handler 0
    request 14 handled in heandler 1
    request 22 handled in handler 2
    request 18 handled in heandler 1
    request 3 handled in handler 0
    end of chain, no handler 35
    request 27 handled in handler 2
    request 20 handled in handler 2
   """


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)

##### OUTPUT #####
# request 2 handled in handler 0
# request 5 handled in handler 0
# request 14 handled in heandler 1
# request 22 handled in handler 2
# request 18 handled in heandler 1
# request 3 handled in handler 0
# end of chain, no handler 35
# request 27 handled in handler 2
# request 20 handled in handler 2
