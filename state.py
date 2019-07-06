"""将逻辑组织成不连续数量的潜在状态并且下一个状态能够被过渡到

实现状态模式

http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/

实现状态作为一个状态模式接口的派生类。
通过调用来自模式超类的方法实现状态的过渡。
"""


class State:
    """基状态。为了共享功能"""

    def scan(self):
        """扫描通信的下一站"""
        self._pos += 1
        if self._pos == len(self._stations):
            self._pos = 0
        print(
            "Scanning ... stations is %s %s"
            % (self._stations[self._pos], self._name)
        )


class AmState(State):
    def __init__(self, radio):
        self._radio = radio
        self._stations = ["1250", "1380", "1510"]
        self._pos = 0
        self._name = "AM"

    def toggle_amfm(self):
        print("Switching to FM")
        self._radio.state = self._radio._fmstate


class FmState(State):
    def __init__(self, radio):
        self._radio = radio
        self._stations = ["81.3", "89.1", "103.9"]
        self._pos = 0
        self._name = "FM"

    def toggle_amfm(self):
        print("Switching to AM")
        self._radio.state = self._radio.amstate


class Radio:
    """电台。   它有扫描的按钮，并且能够切换FM/AM。"""

    def __init__(self):
        """有AM状态和FM状态"""
        self._amstate = AmState(self)
        self._fmstate = FmState(self)
        self._state = self._amstate

    def toggle_amfm(self):
        self._state.toggle_amfm()

    def scan(self):
        self._state.scan()


def main():
    """
    >>> radio = Radio()
    >>> actions = [radio.scan] * 2 + [radio.toggle_amfm] + [radio.scan] * 2
    >>> actions *= 2

    >>> for action in actions:
    ...     action()
    Scanning ... stations is 1380 AM
    Scanning ... stations is 1510 AM
    Switching to FM
    Scanning ... stations is 1250 AM
    Scanning ... stations is 1380 AM
    Scanning ... stations is 1510 AM
    Scanning ... stations is 1250 AM
    Switching to FM
    Scanning ... stations is 1380 AM
    Scanning ... stations is 1510 AM
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

