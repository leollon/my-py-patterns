"""使用一个类作为其他的应用程序接口

例子来自 https://en.wikipedia.org/wiki/Facade_pattern#Python


这个设计模式是关于什么的？
这个外观模式是提供一个更简单统一的接口给更复杂的系统。它通过提供单一入口点来更简单地访问底层
系统功能。这种类型的抽象在现实生活不乏少见。例如，通过按下一个按钮即可打开计算机，但是事实上，
当产生这个事情时，这其中完成了许多的过程和操作（例如，从磁盘加载程序到内存上）。在这个例子中，
这个按钮充当了所有打开一台计算机底层过程的接口。

这个设计模式的实际用处？
在使用isdir这个函数的时候，这个设计模式在Python标准库中可以看到。尽管用户仅仅是通过这个函数而
得知一个路径是否是指向的是一个目录，但是系统还是做了一下操作并调用了其他模块（例如，os.stat）
来给出结果。


参考
https://sourcemaking.com/design_patterns/facade
https://fkromer.github.io/python-pattern-references/design/#facade
http://python-3-patterns-idioms-test.readthedocs.io/en/latest/ChangeInterface.html#facade


总而言之，外观模式描述的是给复杂的系统提供更为简单统一的接口。
"""


class CPU:
    """简单的cpu特征
    """

    def freeze(self):
        print("Freezing processor.")

    def jump(self, position):
        print("Jumping to:", position)

    def execute(self):
        print("Excuting.")


class Memory:
    """简易的内存特征
    """

    def load(self, position, data):
        print("Loading from {0} data: '{1}'.".format(position, data))


class SolidStateDrive:
    """简易的固态硬盘特征
    """

    def read(self, lba, size):
        return "Some data from sector{0} with size {1}".format(lba, size)


class ComputerFacade:
    """表示不同计算机部件的外观"""

    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.ssd = SolidStateDrive()

    def start(self):
        self.cpu.freeze()
        self.memory.load("0x00", self.ssd.read("100", "1024"))
        self.cpu.jump("0x00")
        self.cpu.execute()


def main():
    """
    >>> computer_facade = ComputerFacade()
    >>> computer_facade.start()
    Freezing processor.
    Loading from 0x00 data: 'Some data from sector100 with size 1024'.
    Jumping to: 0x00
    Excuting.
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)
