from flask.views import MethodView


class BaseView(MethodView):
    def get(self):
        return "Hello World!"
