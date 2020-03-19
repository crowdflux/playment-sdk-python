from playment.project_handler import Project
from playment.job import Job
from playment.config import apis
from playment.requests import Requests
from playment.batch_handler import Batch


class Client:
    def __init__(self, client_key: str):
        self.client_key = client_key

    #todo: remove Project -> just project_id
    def create_batch(self, batch: Batch, project: Project):
        assert batch.name is not None
        assert batch.label is not None
        assert batch.description is not None
        assert project.project_id is not None
        url = apis['batch_creation'].format(project.project_id)
        response = Requests.post(url,
                                 headers={
                                            'x-playment-key': self.client_key
                                         },
                                 data=batch.__dict__
                                 )

        batch.batch_id = response[1]['batch_id']
        return batch

    # todo: remove Project -> just project_id
    def create_job(self, job: Job, project: Project):
        assert project.project_id is not None
        url = apis['job_creation'].format(project.project_id)
        job.data.valid()
        response = Requests.post(
            url,
            headers={
                        'x-playment-key': self.client_key
                    },
            data=job.__dict__
                                )
        return response

    def get_project_summary(self, project: Project):
        assert project.project_id is not None
        url = apis['project_summary'].format(project.project_id)
        response = Requests.get(
            url=url,
            headers={
                "x-playment-key": self.client_key
            }
        )
        return response

    def get_project_batches_summary(self, project: Project):
        assert project.project_id is not None
        url = apis['project_batch_details'].format(project.project_id)
        response = Requests.get(
            url=url,
            headers={
                "x-playment-key": self.client_key
            }
        )
        return response

    def get_batch_summary(self, batch: Batch, project: Project):
        assert batch.batch_id is not None
        assert project.project_id is not None
        url = apis['batch_summary'].format(project.project_id, batch.batch_id)
        response = Requests.get(
            url=url,
            headers={
                "x-playment-key": self.client_key
            }
        )
        return response

    def get_job_data(self, project: Project, job_id: str):
        assert project.project_id is not None
        url = apis['job_result'].format(project.project_id, job_id)
        response = Requests.get(
            url=url,
            headers={
                "x-playment-key": self.client_key
            }
        )
        return response
