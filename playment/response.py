import requests.models


class Responses:
    def response(res: requests.models.Response):
        return res.json()['success'] if "success" in res.json() else None,\
               res.json()['data'] if "data" in res.json() else None,\
               res.json()['error']['code'] if "error" in res.json() else None
