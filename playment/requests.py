import requests
from playment.response import response_to_dict, json2obj, PlaymentResponse
from playment.exception import PlaymentException
import time
import json


# class Head:
#     class Key:
#         playment_key = "x-client-key"
#
#     class Value:
#         playment_key = None


def retry(url: str, headers: dict, data=None, method: str = "POST", limit: int = 3, count: int = 1):
    print("retrying for {} time".format(str(count)))

    if method == "POST":
        response = requests.post(url, headers=headers, json=data)
        if (response.status_code >= 500 or response.status_code in [408, 429, 443, 444]) and count <= limit:
            count += 1
            time.sleep(0.5*count)
            response = retry(url=url, headers=headers, data=data, method=method, limit=limit, count=count)
        return response

    else:
        response = requests.get(url, headers=headers)
        if (response.status_code >= 500 or response.status_code in [408, 429, 443, 444]) and count <= limit:
            count += 1
            response = retry(url, headers=headers, method=response.request.method, limit=limit)
        return response


class Requests:
    def __init__(self, value: str):
        self.headers = dict(zip(["x-client-key"], [value]))

    def post(self, url: str, data=None, limit: int = 3, headers: dict = None):
        if headers is None:
            headers = self.headers
        else:
            headers.update(self.headers)
        res = requests.post(url, headers=headers, json=data)
        if res.status_code >= 500 or res.status_code in [408, 429, 443, 444]:
            res = retry(url=url, headers=headers, data=data, method=res.request.method, limit=limit)
        response = PlaymentResponse(res)
        if response.success is False:
            return PlaymentException(response)
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
