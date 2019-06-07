"""用来软化接改变的一个客户端供给中间人

参考
http://en.wikibooks.org/wiki/Computer_Science_Design_Patterns/Bridge_Pattern#Python

总而言之，其目的是用于从它的实现中解偶出抽象概念

"""
#!/usr/bin/python3


# 具体实现器 1/2
class DrawingAPI1:
    def draw_circle(self, x, y, radius):
        print("API1.circle at {}:{} radius {}".format(x, y, radius))


# 具体实现器 2/2
class DrawingAPI2:
    def draw_circle(self, x, y, radius):
        print("API2.circle at {}:{} radius {}".format(x, y, radius))


# 提炼抽象概念
class CircleShape:
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    # 实现细节
    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    # 抽象细节
    def scale(self, pct):
        self._radius *= pct


def main():
    shapes = (
        CircleShape(1, 2, 3, DrawingAPI1()),
        CircleShape(5, 7, 11, DrawingAPI2()),
    )

    for shape in shapes:
        shape.scale(2.5)
        shape.draw()


if __name__ == "__main__":
    main()

########## OUTPUT ##########
# API1.circle at 1:2 radius 7.5
# API2.circle at 5:7 radius 27.5

