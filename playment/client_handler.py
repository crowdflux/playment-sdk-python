from playment.job import Job
from playment.config import types
from playment.requests import Requests
from playment.batch_handler import Batch


class Client:
    def __init__(self, client_key: str):
        assert client_key is not None
        self.client_key = client_key
        self.requester = Requests(client_key)

    def create_batch(self, batch: Batch, project_id: str):
        assert batch.name is not None
        assert batch.label is not None
        assert batch.description is not None
        assert project_id is not None
        url = types.batch_creation.format(project_id)
        response = self.requester.post(url=url, data=batch)
        return response

    def create_job(self, job: Job, project_id: str):
        assert project_id is not None
        url = types.job_creation.format(project_id)
        data = job.as_dict(job=job)
        response = self.requester.post(
            url=url,
            data=data
        )

        return response

    def get_project_summary(self, project_id: str):
        assert project_id is not None
        url = types.project_summary.format(project_id)
        response = self.requester.get(
            url=url
        )
        return response

    def get_project_batches_summary(self, project_id: str):
        assert project_id is not None
        url = types.project_batch_details.format(project_id)
        response = self.requester.get(
            url=url
        )
        return response

    def get_batch_summary(self, batch: Batch, project_id: str):
        assert batch.batch_id is not None
        assert project_id is not None
        url = types.batch_summary.format(project_id, batch.batch_id)
        response = self.requester.get(
            url=url
        )
        return response

    def get_job_data(self, project_id: str, job_id: str):
        assert project_id is not None
        assert job_id is not None
        url = types.job_result.format(project_id, job_id)
        response = self.requester.get(
            url=url
        )
        return response
