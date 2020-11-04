from typing import Type

import flask

from mat_server.app.mat_server.routes_ext import views


class RoutesExt:
    """設定 MatServer 的路由"""

    def __init__(self,
                 get_config_view_class: Type[views.GetConfigView],
                 proxy_view_class: Type[views.ProxyView]):
        self._get_config_view_class = get_config_view_class
        self._proxy_view_class = proxy_view_class

    def init_app(self, app: flask.Flask):
        with app.app_context():
            app.add_url_rule('/_mat', view_func=self._get_config_view_class.as_view('get_config'))
            app.add_url_rule('/<path:path>', view_func=self._proxy_view_class.as_view('proxy'))
