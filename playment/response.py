import json


class ToJson:
    def object_to_json(obj):
        return json.loads(
            json.dumps(obj, default=lambda o: getattr(o, '__dict__', str(o)))
        )

    def response(res: dict):
        success = res['success']
        data = res['data']
        error = res['error']
        return success, data, error

    def response_to_dict(res):
        return ToJson.response(res.json())


class PlaymentResponses:
    def __init__(self, res: dict):
        self.success = res['success']
        self.error = res['error'] if 'error' in res else None
        self.data = res['data'] if 'data' in res else None

    # def response(res: requests.models.Response):
    #     return res.json()['success'] if "success" in res.json() else None,\
    #            res.json()['data'] if "data" in res.json() else None,\
    #            res.json()['error']['code'] if "error" in res.json() else None
