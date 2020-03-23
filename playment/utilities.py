import json
from collections import namedtuple
from playment.projects import ProjectSummary


class ObjDict(dict):
    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError("No such attribute: " + name)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("No such attribute: " + name)


class JSON2Obj:
    def __init__(self, obj, data):
        self.obj = obj
        self.data = data

    def _json_object_hook(self, d):
        if self.obj == "ProjectSummary":
            return ProjectSummary(
                name=d['name'],
            )
        return namedtuple(self.obj, d.keys())(*d.values())

    def json2obj(self):
        return json.loads(self.data, object_hook=self._json_object_hook)


def to_dict(obj):
    return json.loads(
        json.dumps(obj, default=lambda o: getattr(o, '__dict__', str(o)))
    )