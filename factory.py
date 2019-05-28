#!/usr/bin/env python3.6
"""
这个设计模式是关于什么的？
使用一个对象创建其他对象的工厂。

这个例子干什么的？
这里的代码用两种语言将单词进行本地化：英语和汉语。"get_localizer"根据选择的语言构造一个翻
器的工厂函数。根据本地语言，定位器对象将会是一个来自不同类的实例。然而，主要的代码不要操心实例化
的是那个定位器，因为使用相同的方式调用"localize"方法而不依赖于语言。

在实际中，这个设计模式用在哪里？
这个工厂方法可以在流行的web框架 Django可到：
http://django.wikispaces.asu.edu/*NEW*+Django+Design+Patterns，例如，在网页中的一张
联系表单，主题字段和信息字段使用相同的表单工厂(CharField())创建，甚至根据它们的目的，可以有
不同的实现

引用：
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/

原文太长了，总而言之，不用指定确切的类而创建对象。
"""


class ChineseLocalizer:
    """
        一个简单的定位器
    """

    def __init__(self):
        self.translations = {"dog": "狗", "cat": "猫"}

    def localize(self, msg):
        """如果没有对应的翻译文本则远洋返回"""
        return self.translations.get(msg, msg)


class EnglishLocalizer:
    """简单的输出信息"""

    def localize(self, msg):
        return msg


def get_localizer(language="English"):
    """Factory"""
    localizers = {"English": EnglishLocalizer, "Chinese": ChineseLocalizer}
    return localizers[language]()


def main():
    """
    # 创建定位器
    >>> eng, chn = (get_localizer(language="English"), get_localizer(language="Chinese"))
    >>> for msg in "dog parrot cat bear".split():
    ...     print(eng.localize(msg), chn.localize(msg))
    dog 狗
    parrot parrot
    cat 猫
    bear bear
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
