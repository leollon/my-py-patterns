#!/usr/bin/env python3
"""
简单工厂模式

增加操作：
    1. 增加对应子类
    2. 修改工厂类
"""


class Operation:
    """
       背后的原理是使用Python的描述器
    """

    @property
    def number_a(self):
        return self.__number_a

    @number_a.setter
    def number_a(self, value):
        self.__number_a = value

    @property
    def number_b(self):
        return self.__number_b

    @number_b.setter
    def number_b(self, value):
        self.__number_b = value


class OperationAdd(Operation):
    def get_result(self):
        return self.number_a + self.number_b


class OperationSub(Operation):
    def get_result(self):
        return self.number_a - self.number_b


class OperationFactory:
    """
        根据操作的不同使用不同的类创建该类的类对象。
    """

    @staticmethod
    def create_operation(operator):
        if operator == "+":
            return OperationAdd()
        elif operator == "-":
            return OperationSub()


if __name__ == "__main__":
    op_plus = OperationFactory.create_operation("+")
    op_plus.number_a = 10
    op_plus.number_b = 5

    print(op_plus.get_result())

    op_minus = OperationFactory.create_operation("-")
    op_minus.number_a = 2
    op_minus.number_b = 10

    print(op_minus.get_result())

