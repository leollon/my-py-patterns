"""零个以上的注册监听人的源联合事件或数据
参考
http://www.slideshare.net/ishraqabd/publish-subscribe-model-overview-13368808
作者： https://github.com/HanWenfang
"""


class Provider:
    def __init__(self):
        self._msg_queue = []
        self._subscribers = {}

    def notify(self, msg):
        self._msg_queue.append(msg)

    def subscribe(self, msg, subscriber):
        # try:
        #     self._subscribers[msg].append(subscriber)
        # except KeyError:
        #     self._subscribers[msg] = []
        # self._subscribers[msg].append(subscriber)
        # 与下面的语句，处理字典中键不存在的情况，使用下方的更为高效
        self._subscribers.setdefault(msg, []).append(subscriber)

    def unsubscribe(self, msg, subscriber):
        self._subscribers[msg].remove(subscriber)

    def update(self):
        for msg in self._msg_queue:
            for sub in self._subscribers.get(msg, []):
                sub.run(msg)
        self._msg_queue = []


class Publisher:
    def __init__(self, msg_center):
        self._provider = msg_center

    def publish(self, msg):
        self._provider.notify(msg)


class Subscriber:
    def __init__(self, name, msg_center):
        self.name = name
        self._provider = msg_center

    def subscribe(self, msg):
        self._provider.subscribe(msg, self)

    def unsubscribe(self, msg):
        self._provider.unsubscribe(msg, self)

    def run(self, msg):
        print("{} got {}".format(self.name, msg))


def main():
    """
    >>> message_center = Provider()  # 消息中心，给订阅人发送消息

    >>> fftv = Publisher(message_center)  # 内容发布人

    # 订阅人
    >>> jim = Subscriber("Jim", message_center)
    >>> jack = Subscriber("Jack", message_center)
    >>> gee = Subscriber("Gee", message_center)
    >>> vani = Subscriber("Vani", message_center)

    # 订阅内容
    >>> jim.subscribe("cartoon")
    >>> vani.subscribe("movie")
    >>> jack.subscribe("music")
    >>> gee.subscribe("move")

    # 取消订阅
    >>> vani.unsubscribe("movie")
    
    # 内容发布人往消息中心发布内容
    >>> fftv.publish("cartoon")
    >>> fftv.publish("music")
    >>> fftv.publish("ads")
    >>> fftv.publish("movie")
    >>> fftv.publish("cartoon")
    >>> fftv.publish("cartoon")
    >>> fftv.publish("movie")
    >>> fftv.publish("blank")

    >>> message_center.update()
    Jim got cartoon
    Jack got music
    Jim got cartoon
    Jim got cartoon
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

