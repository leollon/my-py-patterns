"""将命令和参数捆绑一起来供后续调用
总而言之，封装被用来执行一个动作或是触发一个事件的所有信息。

在Python生态系统中的例子：
Django HttpRequest (无 `execute` 方法):
https://docs.djangoproject.com/en/2.2/ref/request-response/#httprequest-objects
"""
import pathlib


class MoveFileCommand:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def execute(self):
        self.rename(self.src, self.dest)

    def undo(self):
        self.rename(self.dest, self.src)

    def rename(self, src, dest):
        print("renaming %s to %s" % (src, dest))
        pathlib.Path(src).rename(dest)


def main():
    """
    >>> import pathlib
    
    >>> command_stacks = [
    ...     MoveFileCommand("foo.txt", "bar.txt"),
    ...     MoveFileCommand("bar.txt", "baz.txt"),
    ... ]

    # 验证不存在所有的文件
    >>> assert not pathlib.Path('foo.txt').exists()
    >>> assert not pathlib.Path('bar.txt').exists()
    >>> assert not pathlib.Path('baz.txt').exists()

    # 创建空的文件
    >>> open("foo.txt", "w").close()

    # 后续可以执行的命令
    >>> for cmd in command_stacks:
    ...     cmd.execute()
    renaming foo.txt to bar.txt
    renaming bar.txt to baz.txt

    # 也可以随意撤销
    >>> for cmd in reversed(command_stacks):
    ...      cmd.undo()
    renaming baz.txt to bar.txt
    renaming bar.txt to foo.txt

    >>> pathlib.Path("foo.txt").unlink()
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
