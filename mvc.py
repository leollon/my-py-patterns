"""model<->view<->controller (非约束关系)

将在GUIs的数据从表现形式和接受的方式中分离开来
"""


class Model:
    def __iter__(self):
        raise NotImplementedError

    def get(self, item):
        """返回一个带有能够迭代它的信息的键值对的.items()方法的对象。
        """
        raise NotImplementedError

    @property
    def item_type(self):
        raise NotImplementedError


class ProductModel(Model):
    class Price(float):
        """一种传递一个具有__str__功能的浮点数的多态的方式"""

        def __str__(self):
            return "{:.2f}".format(self)

    products = {
        "milk": {"price": Price(1.50), "quantity": 10},
        "eggs": {"price": Price(0.20), "quantity": 100},
        "cheese": {"price": Price(2.00), "quantity": 10},
    }

    item_type = "product"

    def __iter__(self):
        for item in self.products:
            yield item

    def get(self, product):
        try:
            return self.products[product]
        except KeyError as e:
            raise KeyError((str(e) + "not in the model's item list."))


class View:
    def show_item_list(self, item_type, item_list):
        raise NotImplementedError

    def show_item_information(self, item_type, item_name, item_info):
        """通过迭代由item_info.items()生成的键值对来查找商品的信息
        """
        raise NotImplementedError

    def item_not_found(self, item_type, item_name):
        raise NotImplementedError


class ConsoleView(View):
    def show_item_list(self, item_type, item_list):
        print(item_type.upper() + " List:")
        for item in item_list:
            print(item)
        print("")

    @staticmethod
    def capitalizer(string):
        return string[0].upper() + string[1:].lower()

    def show_item_information(self, item_type, item_name, item_info):
        print(item_type.upper() + " INFORMATION:")
        printout = ["Name: %s" % item_name]
        for key, value in item_info.items():
            printout.append(
                ", " + self.capitalizer(str(key)) + ": " + str(value)
            )
        printout.append("\n")
        print("".join(printout))

    def item_not_found(self, item_type, item_name):
        print(
            'That %s "%s" does not exist in the records'
            % (item_type, item_name)
        )


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_items(self):
        items = list(self.model)
        item_type = self.model.item_type
        self.view.show_item_list(item_type, items)

    def show_item_information(self, item_name):
        try:
            item_info = self.model.get(item_name)
        except Exception:
            item_type = self.model.item_type
            self.view.item_not_found(item_type, item_name)
        else:
            item_type = self.model.item_type
            self.view.show_item_information(item_type, item_name, item_info)


if __name__ == "__main__":

    model = ProductModel()
    view = ConsoleView()
    controller = Controller(model, view)
    controller.show_items()
    controller.show_item_information("cheese")
    controller.show_item_information("eggs")
    controller.show_item_information("milk")
    controller.show_item_information("agrepas")


##### OUTPUT #####
# PRODUCT List:
# milk
# eggs
# cheese

# PRODUCT INFORMATION:
# Name: cheese, Price: 2.00, Quantity: 10

# PRODUCT INFORMATION:
# Name: eggs, Price: 0.20, Quantity: 100

# PRODUCT INFORMATION:
# Name: milk, Price: 1.50, Quantity: 10

# That product "agrepas" does not exist in the records
