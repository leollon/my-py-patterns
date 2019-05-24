"""Singleton
单例模式

保证一个类仅有一个实例，并提供一个访问它的全局访问点
    
    - 确保任何情况下只有一个实例存在

单例模式
    用处：
        1. 计数器

    不足之处:
        1. 多线程，要考虑加锁
        2. web时，往往是多进程起
        3. web时，扩容时还往往是多机器实例

"""
from functools import wraps


class SingletonOne:
    """
    使用__new__方法，自定义类对象的创建过程
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            # 描述器协议
            cls._instance = super(SingletonOne, cls).__new__(
                cls, *args, **kwargs
            )
        return cls._instance


class MethodOne(SingletonOne):
    pass


class SingletonTwo(type):
    """自定义一个元类的
    """

    def __call__(cls, *args, **kwargs):
        """
        调用类进行类对象的创建
        """
        if not hasattr(cls, "_instance"):
            cls._instance = super(SingletonTwo, cls).__call__(*args, **kwargs)
        return cls._instance


class MethodTwo(metaclass=SingletonTwo):
    pass


def singleton_three(cls):
    instance = {}

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return get_instance


@singleton_three
class MethodThree:
    pass


if __name__ == "__main__":

    # first method
    instance_a1 = MethodOne()
    instance_b1 = MethodOne()
    print(id(instance_a1), id(instance_b1))  # Same with each other
    print(instance_a1 == instance_b1)  # True
    print(instance_a1 is instance_b1, "\n")  # True

    # second method

    instance_a2 = MethodTwo()
    instance_b2 = MethodTwo()

    print(id(instance_a2), id(instance_b2))
    print(instance_a2 == instance_b2)
    print(instance_a2 is instance_b2, "\n")  # True

    # third method

    instance_a3 = MethodThree()
    instance_b3 = MethodThree()

    print(id(instance_a3), id(instance_b3))
    print(instance_a3 == instance_b3)
    print(instance_a3 is instance_b3, "\n")  # True
