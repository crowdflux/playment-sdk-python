from collections import namedtuple


def _json_object_hook(d):
    return namedtuple('batch_details', d.keys())(*d.values())


class ProjectBatchSummary:
    def __init__(self, name: str = None, base: str = None, batches: list = None):
        self.name = name
        self.base = base
        self.batches = batches

    def _json_object_hook(self, d):
        if 'batches' in d:
            jobs = []
            for j in d['batches']:
                j = dict(j._asdict())
                jobs.append(_json_object_hook(j))
            d['batches'] = jobs
        obj = namedtuple('ProjectBatchSummary', d.keys())(*d.values())
        return obj
