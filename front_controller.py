"""单一处理程序请求进入应用程序
@author: Gordeev Andrey <gordeev.and.and@gmail.com>


提供一个中心化的控制和管理请求处理的入口点。
"""


class MobileView:
    def show_index_page(self):
        print("Display mobile index page")


class TabletView:
    def show_index_page(self):
        print("Displaying tablet index page")


class Dispatcher:
    def __init__(self):
        self.mobile_view = MobileView()
        self.tablet_view = TabletView()

    def dispatch(self, request):
        if request.type == Request.mobile_type:
            self.mobile_view.show_index_page()
        elif request.type == Request.tablet_type:
            self.tablet_view.show_index_page()
        else:
            print("Can't disatch the request")


class RequestController:
    """前置控制器"""

    def __init__(self):
        self.dispatcher = Dispatcher()

    def dispatch_request(self, request):
        if isinstance(request, Request):
            self.dispatcher.dispatch(request)
        else:
            print("request must be a Request object")


class Request:
    """请求"""

    mobile_type = "mobile"
    tablet_type = "tablet"

    def __init__(self, request):
        self.type = None
        request = request.lower()
        if request == self.mobile_type:
            self.type = self.mobile_type
        elif request == self.tablet_type:
            self.type = self.tablet_type


if __name__ == "__main__":
    front_controller = RequestController()
    front_controller.dispatch_request(Request("mobile"))
    front_controller.dispatch_request(Request("tablet"))

    front_controller.dispatch_request(Request("Desktop"))
    front_controller.dispatch_request("mobile")


##### OUTPUT #####
# Display mobile index page
# Displaying tablet index page
# Can't disatch the request
# request must be a Request object
