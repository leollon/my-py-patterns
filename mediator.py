"""懂得如何连接其他对象并且充当一个代理的一个对象
https://www.djangospin.com/design-patterns-python/mediator/

系统中的对象通过中介对象而不是直接彼此之间进行通信。
减少了通信对象之间的依赖，因此减少了耦合。

总而言之，封装了一系列对象的交互方式。
"""


class ChatRoom:
    """中介类"""

    def display_message(self, user, message):
        print("[{} says]: {}".format(user, message))


class User:
    """彼此之间要进行交互的类的实例"""

    def __init__(self, name):
        self.name = name
        self.chat_room = ChatRoom()

    def say(self, message):
        self.chat_room.display_message(self, message)

    def __str__(self):
        return self.name


def main():
    """
    >>> molly = User("Molly")
    >>> mark =  User("Mark")
    >>> ethan =  User("Ethan")
        
    >>> molly.say("Hi Team! Meeting at 3 PM today.")
    [Molly says]: Hi Team! Meeting at 3 PM today.

    >>> mark.say("Roger that!")
    [Mark says]: Roger that!

    >>> ethan.say("Alright.")
    [Ethan says]: Alright.
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
