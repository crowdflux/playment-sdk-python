import requests
from playment.response import PlaymentResponse, response_to_dict
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
    headers = dict(zip([Head.Key.client_key], [Head.Value.client_key]))
    def post(url: str, headers: dict = headers, data=None, limit: int = 3):

        # globalHeader.append(headers)
        #
        # globalconverter.convertojson()
        response = requests.post(url, headers=headers, json=data)
        if response.status_code >= 500 or response.status_code in [408, 429, 443, 444]:
            response = retry(url, headers, data, response.request.method, limit)
        elif 400 <= response.status_code < 500:
            raise PlaymentException(response)
        elif response.status_code == 200 and response.json()['success'] is False:
            raise PlaymentException(response)
        response = PlaymentResponse(response_to_dict(res=response))
        return response

    def get(url: str, headers: dict = headers, limit: int = 3):
        response = requests.get(url, headers=headers)
        if response.status_code >= 500 or response.status_code in [408, 429, 443, 444]:
            response = retry(url, headers=headers, method=response.request.method, limit=limit)
        elif 400 <= response.status_code < 500:
            raise PlaymentException(response)
        elif response.status_code == 200 and response.json()['success'] is False:
            raise PlaymentException(response)
        return Responses.response(response)
