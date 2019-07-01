"""
通用方法将根据构造函数的的参数调用不同的特别的方法。
"""


class Catalog:
    """根据初始化参数，执行多个静态方法的目录。
    """

    def __init__(self, param):
        # 用来决定那个静态方法会被执行的字典，但是也被用来存储可能param的的值
        self._static_method_choices = {
            "param_value_1": self._static_method_1,
            "param_value_2": self._static_method_2,
        }

        # 简单测试使得param的值有效
        if param in self._static_method_choices.keys():
            self.param = param  # 描述器
        else:
            raise ValueError("invalid value for Param: {0}".format(param))

    @staticmethod
    def _static_method_1():
        print("excuted method 1!")

    @staticmethod
    def _static_method_2():
        print("excuted method 2!")

    def main_method(self):
        """根据self.param的值，将会执行_static_method_1 和 _static_method_2 两者之一。"""
        self._static_method_choices[self.param]()


# 对于不同的方法等级的可选的实现
class CatalogInstance:
    """根据初始化参数的执行多个方法的目录"""

    def __init__(self, param):
        self.x1 = "x1"
        self.x2 = "x2"

        # 简单测试使得param值有效
        if param in self._instance_method_choices:
            self.param = param
        else:
            raise ValueError("Invalid Value for Param: {0}".format(param))

    def _instance_method_1(self):
        print("Value {}".format(self.x1))

    def _instance_method_2(self):
        print("Value {}".format(self.x2))

    _instance_method_choices = {
        "param_value_1": _instance_method_1,
        "param_value_2": _instance_method_2,
    }

    def main_method(self):
        """根据self.param的值，将会执行_instance_method_1 和 _instance_method_2两个
        方法中的一个。
        """
        # 访问实例属性
        self._instance_method_choices[self.param].__get__(self)()


class CatalogClass:
    """根据初始化参数，将执行多个类方法的目录。
    """

    x1 = "x1"
    x2 = "x2"

    def __init__(self, param):
        # 简单测试使得param值有效
        if param in self._class_method_choices:
            self.param = param
        else:
            raise ValueError("Invalid Value for Param: {0}".format(param))

    @classmethod
    def _class_method_1(cls):
        print("Value {}".format(cls.x1))

    @classmethod
    def _class_method_2(cls):
        print("Value {}".format(cls.x2))

    _class_method_choices = {
        "param_value_1": _class_method_1,
        "param_value_2": _class_method_2,
    }

    def main_method(self):
        """根据self.param的值，将会执行_class_method_1 和 _class_method_2两个方法中
        的一个。
        """
        self._class_method_choices[self.param].__get__(None, self.__class__)()


class CatalogStatic:
    """根据初始化参数执行多个静态方法的目录。
    """

    def __init__(self, param):
        # 简单测试使得param的值有效
        if param in self._static_method_choices:
            self.param = param
        else:
            raise ValueError("Invalid Value for Param: {0}".format(param))

    @staticmethod
    def _static_method_1():
        print("excuted method 1!")

    @staticmethod
    def _static_method_2():
        print("excuted method 2!")

    _static_method_choices = {
        "param_value_1": _static_method_1,
        "param_value_2": _static_method_2,
    }

    def main_method(self):
        """根据self.param的值将会执行_static_method_1和_static_method_2两者之一。"""
        # https://docs.python.org/3/reference/datamodel.html#object.__get__
        # https://docs.python.org/3/reference/datamodel.html#invoking-descriptors
        # 静态方法可以通过类名来调用或者通过该类的实例来调用。
        # 访问类属性
        # self._static_method_choices[self.param].__get__(None, self.__class__)()
        # 访问类属性
        self._static_method_choices[self.__dict__["param"]].__get__(
            None, self.__class__
        )()


def main():
    """
    >>> test = Catalog('param_value_2')
    >>> test.main_method()
    excuted method 2!

    >>> test = CatalogInstance('param_value_1')
    >>> test.main_method()
    Value x1

    >>> test = CatalogClass('param_value_2')
    >>> test.main_method()
    Value x2

    >>> test = CatalogStatic('param_value_1')
    >>> test.main_method()
    excuted method 1!
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

