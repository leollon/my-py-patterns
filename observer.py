"""提供回调功能给事件通知或改变数据时的通知
http://code.activestate.com/recipes/131499-observer-pattern/

总而言之，维护一个依赖列表并且它们的状态发生改变时发出通知。

在Python生态系统中的例子：
Django Signals: https://docs.djangoproject.com/en/2.2/topics/signals/
Flask Signals: http://flask.pocoo.org/docs/1.0/signals/
"""


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class Data(Subject):
    __slots__ = ["_data", "name"]

    def __init__(self, name=""):
        super(Data, self).__init__()
        self.name = name
        self._data = 0

    @property
    def data(self):
        # 描述器协议
        return self._data

    @data.setter
    def data(self, value):
        # 描述器协议
        self._data = value
        self.notify()


class HexViewer:
    def update(self, subject):
        print(
            "HexViewer: Subject %s has data 0x%x" % (subject.name, subject.data)
        )


class DecimalViewer:
    def update(self, subject):
        print(
            "DecimalViewer: Subject %s has data %d"
            % (subject.name, subject.data)
        )


def main():
    """
    >>> data1 = Data("Data 1")
    >>> data2 = Data("Data 2")
    >>> view1 = DecimalViewer()  # 观察者1
    >>> view2 = HexViewer()  # 观察者2

    >>> data1.attach(view1)
    >>> data1.attach(view2)
    >>> data2.attach(view2)
    >>> data2.attach(view1)

    >>> data1.data = 10
    DecimalViewer: Subject Data 1 has data 10
    HexViewer: Subject Data 1 has data 0xa

    >>> data2.data = 15
    HexViewer: Subject Data 2 has data 0xf
    DecimalViewer: Subject Data 2 has data 15

    >>> data1.data = 3
    DecimalViewer: Subject Data 1 has data 3
    HexViewer: Subject Data 1 has data 0x3

    >>> data2.data = 5
    HexViewer: Subject Data 2 has data 0x5
    DecimalViewer: Subject Data 2 has data 5

    # Detach HexViewer from data1 and data2
    >>> data1.detach(view2)
    >>> data2.detach(view2)

    >>> data1.data = 10
    DecimalViewer: Subject Data 1 has data 10

    >>> data2.data = 15
    DecimalViewer: Subject Data 2 has data 15
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
