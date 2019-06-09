"""将功能与其他功能包装在一起，来达到影响输出的效果

这个模式是关于什么的？
装饰器模式用来向一个对象动态添加新特性，而不用更改它的实现。这与集成不一样，原因是新特性只被
添加特定的对象，而不是整个子类。


这个例子干什么？
这个例子要做的是通过添加标签（<b>和<i>）来向一段文本添加格式化选项的方式。还有，可以看到装饰器
能够被用于一个接一个的文本，由于源文本被传递给加粗包装器，包装器返回值被传递给斜体包装器。

这个例子的实际使用在什么地方？
Grok框架使用装饰器来给方法增加功能，比如权限或者订阅事件：
https://github.com/zopefoundation/grok/blob/aee7f35def07237f474934f813ed14c29adc6479/src/grok/tests/event/subscriber.py#L28


参考
https://sourcemaking.com/design_patterns/decorator

总而言之，装饰器模式描述的是向对象添加行为而不影响它的类
"""


class TextTag:
    """表示基本文本标签"""

    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class BoldWrapper(TextTag):
    """给文本添加<b>标签"""

    def __init__(self, wrapped_object):
        self._wrapped_object = wrapped_object

    def render(self):
        return "<b>{}</b>".format(self._wrapped_object.render())


class ItalicWrapper(TextTag):
    """给文本添加<i>标签"""

    def __init__(self, wrapped_object):
        self._wrapped_object = wrapped_object

    def render(self):
        return "<i>{}</i>".format(self._wrapped_object.render())


if __name__ == "__main__":
    simple_hello = TextTag("hello world!")
    wrapped_hello = ItalicWrapper(BoldWrapper(simple_hello))
    print("Before wrapped:", simple_hello.render())
    print("After wrapped:", wrapped_hello.render())


########## OUTPUT ##########
# Before wrapped: hello world!
# After wrapped: <i><b>hello world!</b></i>
