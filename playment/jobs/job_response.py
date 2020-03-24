from collections import namedtuple


class JobResponse:
    def __init__(self, job_id: str = None, reference_id: str = None, tag: str = None):
        self.job_id = job_id
        self.reference_id = reference_id
        self.tag = tag

    def _json_object_hook(self, d):
        return namedtuple('JobResponse', d.keys())(*d.values())
