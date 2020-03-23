import requests
from playment.response import response_to_dict, json2obj
from playment.exception import PlaymentException
import json


class Head:
    class Key:
        playment_key = "x-client-key"

    class Value:
        playment_key = None


def retry(url: str, headers: dict, data=None, method: str = "POST", limit: int = 3, count: int = 1):
    print("retrying for {} time".format(str(count)))

    if method == "POST":
        response = requests.post(url, headers=headers, json=data)
        if (response.status_code >= 500 or response.status_code in [408, 429, 443, 444]) and count <= limit:
            count += 1
            response = retry(url=url, headers=headers, data=data, method=method, limit=limit, count=count)
        elif 400 <= response.status_code < 500:
            raise PlaymentException(response)
        elif response.status_code == 200 and response.json()['success'] is False:
            raise PlaymentException(response)
        return response

    else:
        response = requests.get(url, headers=headers)
        if (response.status_code >= 500 or response.status_code in [408, 429, 443, 444]) and count <= limit:
            count += 1
            response = retry(url, headers=headers, method=response.request.method, limit=limit)
        elif 400 <= response.status_code < 500:
            raise PlaymentException(response)
        elif response.status_code == 200 and response.json()['success'] is False:
            raise PlaymentException(response)
        return response


class Requests:
    def __init__(self, headers: str):
        Head.Value.playment_key = headers
        self.headers = dict(zip([Head.Key.playment_key], [Head.Value.playment_key]))

    def post(self, url: str, data=None, limit: int = 3):
        response = requests.post(url, headers=self.headers, json=data)
        resp = json2obj(json.dumps(response.json()))
        print(type(resp))
        print(resp)
        print(resp.error.code)
        if response.status_code >= 500 or response.status_code in [408, 429, 443, 444]:
            response = retry(url, self.headers, data, response.request.method, limit)
        elif 400 <= response.status_code < 500:
            raise PlaymentException(response)
        elif response.status_code == 200 and response.json()['success'] is False:
            raise PlaymentException(response)
        # response = PlaymentResponse(response_to_dict(res=response))
        return response

    def get(self, url: str, limit: int = 3):
        response = requests.get(url, headers=self.headers)
        if response.status_code >= 500 or response.status_code in [408, 429, 443, 444]:
            response = retry(url, headers=self.headers, method=response.request.method, limit=limit)
        elif 400 <= response.status_code < 500:
            raise PlaymentException(response)
        elif response.status_code == 200 and response.json()['success'] is False:
            raise PlaymentException(response)
        return PlaymentResponse(response_to_dict(res=response))
