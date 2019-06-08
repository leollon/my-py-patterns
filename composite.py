"""然客户端统一对象独立的对象和组合

这个模式是关于什么的？
这个组合模式描述的是像使用相同的方式对待相同对象类型的单一实例一样对待一组对象。
组合的目的是为了将对象“组合”成为树结构来表示部分-整体的层次关系。实现这个组合模式让客户端
统一对待独立对象和组合对象。

这个例子干什么？
这个例子实现一个图形类，可以是椭圆或是几个图形的组合。每个图形都可以打印出来。

这个模式的实际用处？
在图形编辑器中，一个形状可简单可复杂。一条直线就是一个简单的图行，矩形有四条直线组成的一个复杂
的图形。 由于形状都有许多相同的操作，比如将形状渲染到屏幕上，并且形状遵循部分-整体的层次关系，
组合模式可以用来让程序统一处理所有的形状。

参考：

https://en.wikipedia.org/wiki/Composite_pattern
https://infinitescript.com/2014/10/the-23-gang-of-three-design-patterns/

总而言之，组合模式描述的是一组对象可以像单个实例一样来对待。
"""


class Graphic:
    def render(self):
        raise NotImplementedError("You should implement this.")


class CompositeGraphic(Graphic):
    def __init__(self):
        self.graphics = []

    def render(self):
        for graphic in self.graphics:
            graphic.render()

    def add(self, graphic):
        self.graphics.append(graphic)

    def remove(self, graphic):
        self.graphics.remove(graphic)


class Ellipse(Graphic):
    def __init__(self, name):
        self.name = name

    def render(self):
        print("Ellipse: {}".format(self.name))


if __name__ == "__main__":
    ellipse1 = Ellipse("1")  # 独立对象
    ellipse2 = Ellipse("2")  # 独立对象
    ellipse3 = Ellipse("3")  # 独立对象
    ellipse4 = Ellipse("4")  # 独立对象

    graphic1 = CompositeGraphic()
    graphic2 = CompositeGraphic()

    graphic1.add(ellipse1)  # 将独立对象组合起来
    graphic1.add(ellipse2)  # 将独立对象组合起来
    graphic1.add(ellipse3)  # 将独立对象组合起来
    graphic2.add(ellipse4)  # 将独立对象组合起来

    graphic = CompositeGraphic()

    graphic.add(graphic1)  # 再次将独立对象组合起来
    graphic.add(graphic2)  # 再次将独立对象组合起来

    graphic.render()  # 渲染组合对象


########## OUTPUT #########
# Ellipse: 1
# Ellipse: 2
# Ellipse: 3
# Ellipse: 4
