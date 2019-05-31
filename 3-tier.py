#!/usr/bin/env python3
"""
总而言之，将表现形式，应用处理，和数据管理功能分隔开来。
MVC似有3-tier的意思，但其实则不然。

Reference:
  https://stackoverflow.com/questions/10739914/what-is-the-difference-between-3-tier-architecture-and-a-mvc

3-tier 是像这样子的过程, c -> b -> a and a -> b -> c，它从不直接与数据管理直接沟通，而是
要通过一次中转处理的过程，才能到达数据管理层，然而， MVC 是下面这样子的过程：
          M
         ↗ ↘
        ↗   ↘
       ↗     ↘
      C ⬅ ⬅ ⬅ V，
视图将更新发送给控制器，控制更新数据管理模型，数据管理模型将更新返回给视图层。
"""


class Data:
    """数据存储类"""

    products = {
        "milk": {"price": 1.50, "quantity": 10},
        "eggs": {"price": 0.20, "quantity": 100},
        "cheese": {"price": 2.00, "quantity": 10},
    }

    def __get__(self, obj, klass):
        print("(Fetching from Data Store)")
        return {"products": self.products}


class BusinessLogic:
    """应用处理
        业务逻辑有所有的数据存储实例
    """

    data = Data()

    def product_list(self):
        return self.data["products"].keys()

    def product_information(self, product):
        return self.data["products"].get(product, None)


class Ui:
    """表现形式
        UI 交互类
    """

    def __init__(self):
        self.business_logic = BusinessLogic()

    def get_product_list(self):
        print("PRODUCT LIST:")
        for product in self.business_logic.product_list():
            print(product)
        print("")

    def get_product_information(self, product):
        product_info = self.business_logic.product_information(product)
        if product_info:
            print("PRODUCT INFORMATION:")
            print(
                "Name: {0}, Price: {1:.2f}, Quantity: {2:}".format(
                    product.title(),
                    product_info.get("price", 0),
                    product_info.get("quantity", 0),
                )
            )


def main():
    ui = Ui()
    ui.get_product_list()
    ui.get_product_information("cheese")
    ui.get_product_information("eggs")
    ui.get_product_information("milk")
    ui.get_product_information("arepass")


if __name__ == "__main__":
    main()


#####Output#####
# PRODUCT LIST:
# (Fetching from Data Store)
# milk
# eggs
# cheese

# (Fetching from Data Store)
# PRODUCT INFORMATION:
# Name: Cheese, Price: 2.00, Quantity: 10
# (Fetching from Data Store)
# PRODUCT INFORMATION:
# Name: Eggs, Price: 0.20, Quantity: 100
# (Fetching from Data Store)
# PRODUCT INFORMATION:
# Name: Milk, Price: 1.50, Quantity: 10
# (Fetching from Data Store)
