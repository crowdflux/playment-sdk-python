class Batch:
    def __init__(self, id: str = None, name: str = None, label: str = None, description: str = None):
        assert type(id) is str or id is None
        assert type(name) is str
        assert type(label) is str
        assert type(description) is str
        self.id = id
        self.name = name
        self.label = label
        self.description = description
