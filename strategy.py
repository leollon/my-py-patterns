"""对于相同数据的可选择操作

这个模式关于什么？
定义一族算法，对每一个进行封装，并且使它们可互相交换。
策略使得算法独立于使用它的客户端。

总而言之，在运行时能够选择一个算法。
"""


class Order:
    def __init__(self, price, discount_strategy=None):
        self._price = price
        self._discount_strategy = discount_strategy

    def price_after_discount(self):
        discount = 0
        if self._discount_strategy:
            discount = self._discount_strategy(self)
        return self._price - discount

    def __repr__(self):
        fmt = "<Price: {}, price after discount: {}>"
        return fmt.format(self._price, self.price_after_discount())


def ten_percent_discount(order):
    return order._price * 0.10


def on_sale_discount(order):
    return order._price * 0.25 + 20


def main():
    """
    >>> Order(100)
    <Price: 100, price after discount: 100>
    
    >>> Order(100, discount_strategy=ten_percent_discount)
    <Price: 100, price after discount: 90.0>

    >>> Order(1000, discount_strategy=on_sale_discount)
    <Price: 1000, price after discount: 730.0>

    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
