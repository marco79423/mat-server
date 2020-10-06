from typing import Callable

import flask


class MatServer:

    def __init__(self,
                 flask_app: flask.Flask,
                 wsgi_application_prod_serve_func: Callable):
        self._flask_app = flask_app
        self._wsgi_application_prod_serve_func = wsgi_application_prod_serve_func

    def get_app(self):
        return self._flask_app

    def serve(self, host: str, port: int):
        self._wsgi_application_prod_serve_func(self._flask_app, host=host, port=port)
