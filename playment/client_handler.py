from playment.job import Job
from playment.config import apis
from playment.requests import Requests
from playment.batch_handler import Batch
from playment.requests import Head
import json


class Client:
    def __init__(self, client_key: str):
        assert client_key is not None
        self.client_key = client_key
        self.requester = Requests(client_key)
        # Head.Value.client_key = self.client_key

    def create_batch(self, batch: Batch, project_id: str):
        assert batch.name is not None
        assert batch.label is not None
        assert batch.description is not None
        assert project_id is not None
        url = apis['batch_creation'].format(project_id)
        response = Requests.post(url, data=batch)

        batch.batch_id = response[1]['batch_id']
        return batch

    def create_job(self, job: Job, project_id: str):
        assert project_id is not None
        url = apis['job_creation'].format(project_id)
        # ToDo: job.data.valid()
        data = job.as_dict(job=job)
        print(url)

        print(json.dumps(data))
        response = self.requester.post(
            url=url,
            data=data
        )
        # response = Requests.post(
        #     url,
            # headers={
            #             'x-client-key': self.client_key
            #         },
            # data=data
            #                     )

        return response

    def get_project_summary(self, project_id: str):
        assert project_id is not None
        url = apis['project_summary'].format(project_id)
        response = Requests.get(
            url=url,
            headers={
                "x-playment-key": self.client_key
            }
        )
        return response

    def get_project_batches_summary(self, project_id: str):
        assert project_id is not None
        url = apis['project_batch_details'].format(project_id)
        response = Requests.get(
            url=url,
            headers={
                "x-playment-key": self.client_key
            }
        )
        return response

    def get_batch_summary(self, batch: Batch, project_id: str):
        assert batch.batch_id is not None
        assert project_id is not None
        url = apis['batch_summary'].format(project_id, batch.batch_id)
        response = Requests.get(
            url=url,
            headers={
                "x-playment-key": self.client_key
            }
        )
        return response

    def get_job_data(self, project_id: str, job_id: str):
        assert project_id is not None
        assert job_id is not None
        url = apis['job_result'].format(project_id, job_id)
        response = Requests.get(
            url=url,
            headers={
                "x-playment-key": self.client_key
            }
        )
        return response
