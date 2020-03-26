from playment.base.data import Data


class Job:
    def __init__(self, reference_id: str, tag: str, data: Data, id: str = None,
                 priority_weight: int = 5, batch_id: str = None):
        assert type(reference_id) is str
        assert type(tag) is str
        assert type(data) is Data
        assert type(id) is str or id is None
        assert type(priority_weight) is int and 0 < priority_weight < 11
        assert type(batch_id) is str
        self.id = id
        self.reference_id = reference_id
        self.tag = tag
        self.data = data
        self.batch_id = batch_id
        self.priority_weight = priority_weight
