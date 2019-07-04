"""跟踪一个类的所有子类
"""


class RegistryHolder(type):
    REGISTRY = {}

    def __new__(cls, name, bases, attrs):
        new_cls = type.__new__(cls, name, bases, attrs)
        """
            使用类名作为键，但是它可以是任何类参数。
        """
        cls.REGISTRY[new_cls.__name__] = new_cls
        return new_cls

    @classmethod
    def get_registry(cls):
        return dict(cls.REGISTRY)


class BaseRegisteredClass(metaclass=RegistryHolder):
    """
    任何继承BaseRegisteredClass将会包含在字典 `RegistryHolder.REGISTRY`，字典中的键是
    类型的名字和相关的值，类自己。
    """


def main():
    """
    # 在子类化之前
    >>> sorted(RegistryHolder.REGISTRY)
    ['BaseRegisteredClass']

    >>> class ClassRegisteredTree(BaseRegisteredClass):
    ...     def __init__(self, *args, **kwargs):
    ...          pass

    # 在子类化之后
    >>> sorted(RegistryHolder.REGISTRY)
    ['BaseRegisteredClass', 'ClassRegisteredTree']
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
