from playment.job import Job
from playment.config import types
from playment.requests import Requests
from playment.batch_handler import Batch
from playment.data import Data
from playment.utilities import to_dict
from playment.utilities import JSON2Obj
from playment.projects import ProjectSummary, ProjectBatchSummary
from playment.batches import BatchSummary
from playment.jobs import JobResult
import json


class Client:
    def __init__(self, client_key: str):
        assert client_key is not None
        self.client_key = client_key
        self.requester = Requests(client_key)

    def create_batch(self, name, label, description, project_id: str) -> Batch:
        assert name is not None
        assert label is not None
        assert description is not None
        assert project_id is not None
        url = types.batch_creation.format(project_id)
        batch = Batch(name=name, label=label, description=description)
        data = to_dict(obj=batch)
        response = self.requester.post(url=url, data=data)
        batch.id = response.data.batch_id
        return batch

    def create_job(self, reference_id: str, tag: str, data: Data, project_id: str,
                   priority_weight: int = 5, batch_id: str = None) -> Job:
        assert project_id is not None
        url = types.job_creation.format(project_id)
        job = Job(reference_id=reference_id, tag=tag, data=data, priority_weight=priority_weight, batch_id=batch_id)
        data = to_dict(obj=job)
        response = self.requester.post(
            url=url,
            data=data
        )
        job.id = response.data.job_id
        return job

    def get_project_summary(self, project_id: str) -> ProjectSummary:
        assert project_id is not None
        url = types.project_summary.format(project_id)
        response = self.requester.get(
            url=url
        )
        response = JSON2Obj(ProjectSummary(), json.dumps(response.data)).json2obj()
        return response

    def get_project_batches_summary(self, project_id: str):
        assert project_id is not None
        url = types.project_batch_details.format(project_id)
        response = self.requester.get(
            url=url
        )
        response = JSON2Obj(ProjectBatchSummary(), json.dumps(response.data)).json2obj()
        return response

    def get_batch_summary(self, batch_id: str, project_id: str):
        assert batch_id is not None
        assert project_id is not None
        url = types.batch_summary.format(project_id, batch_id)
        response = self.requester.get(
            url=url
        )
        response = JSON2Obj(BatchSummary(), json.dumps(response.data)).json2obj()
        return response

    def get_job_data(self, project_id: str, job_id: str) -> JobResult:
        assert project_id is not None
        assert job_id is not None
        url = types.job_result.format(project_id, job_id)
        response = self.requester.get(
            url=url
        )
        response = JSON2Obj(JobResult(), json.dumps(response.data)).json2obj()
        return response
