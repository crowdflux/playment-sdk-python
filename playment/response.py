import json
from collections import namedtuple


def _json_object_hook(d):
    return namedtuple('PlaymentResponse', d.keys())(*d.values())


def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)


def object_to_json(obj):
    return json.loads(
        json.dumps(obj, default=lambda o: getattr(o, '__dict__', str(o)))
    )


def response(res: dict):
    success = res['success']
    data = res['data'] if 'error' in res else None
    error = res['error'] if 'data' in res else None
    return success, data, error


def response_to_dict(res):
    return response(res.json())


# class PlaymentResponse:
#     def __init__(self, res: dict):
#         self.success = res['success']
#         self.error = res['error']
#         self.data = res['data']

    # def response(res: requests.models.Response):
    #     return res.json()['success'] if "success" in res.json() else None,\
    #            res.json()['data'] if "data" in res.json() else None,\
    #            res.json()['error']['code'] if "error" in res.json() else None
