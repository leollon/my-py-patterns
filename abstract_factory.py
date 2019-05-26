"""factory pattern

这个模式是关于什么？

在Java和其他编程语言中，抽象工厂模式提供一个创建有关联的或者相互依赖对象的接口，而不需要要指定
具体的类。

根据业务逻辑，平台选择等等抽象出对象创建的的思想。

在Python中，使用的接口是仅仅是一个在Python内置的可调用对象，并且在通常情况下，仅仅使用类本身
即可作为那个可调用对象，因为在Python中类是一级对象。

这个例子是干什么的？
这里的实现的是抽象一只宠物的创建并且依赖于选择的工厂(狗或者猫，或随便一种动物)
这个能够有效是因为狗，猫随机一种动物遵循相同的接口(创建和`speak()`的可调用对象)。
现在这个我的应用可以抽象地创建宠物并且以后基于我的标准，决定是狗还是猫。

在实际中，这个设计模式用在哪里？


引用:
https://sourcemaking.com/design_patterns/abstract_factory
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/

TL;DR

总的来说就是，提供一种封装一组独立工厂的方式。
"""


import random


class PetShop:
    """宠物商店
    """

    def __init__(self, animal_factory=None):
        """
            pet_factory是我们的抽象工厂。我们可以随意设置这个工厂。
        """

        self.pet_factory = animal_factory

    def show_pet(self):
        """
            使用抽象工厂创建并显示一只宠物。
        """

        pet = self.pet_factory()
        print(f"We have a lovely {pet}")
        print(f"It says {pet.speak()}")


class Dog:
    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"


class Cat:
    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"


# 随意创建一直动物实例
def random_animal():
    """随机地动态创建动物实例！"""
    return random.choice([Dog, Cat])()


# 使用不同的工厂显示宠物
if __name__ == "__main__":

    # 只卖猫的商店
    cat_shop = PetShop(Cat)
    cat_shop.show_pet()
    print("")

    # 什么动物都卖的商店
    shop = PetShop(random_animal)
    for _ in range(3):
        shop.show_pet()
        print("=" * 20)


# 输出
# We have a lovely Cat
# It says meow

# We have a lovely Cat
# It says meow
# ====================
# We have a lovely Dog
# It says woof
# ====================
# We have a lovely Cat
# It says meow
# ====================
