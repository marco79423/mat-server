import flask.views

from mat_server.domain import use_cases


class GetConfigView(flask.views.MethodView):

    def __init__(self,
                 get_config_use_case: use_cases.GetConfigUseCase,):
        self._get_config_use_case = get_config_use_case

    def get(self):
        mat_config = self._get_config_use_case.execute()
        return mat_config.serialize()
