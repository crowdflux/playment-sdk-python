import json
from collections import namedtuple
from playment.projects import ProjectSummary
import abc


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


class Decodable(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasscheck__(cls, subclass):
        return (
                hasattr(subclass, '_json_object_hook') and
                callable(subclass._json_object_hook)
        )

    @abc.abstractmethod
    def json_object_hook(self, d):
        raise NotImplementedError


class JSON2Obj:
    def __init__(self, obj: Decodable, data):
        self.obj = obj
        self.data = data

    def json2obj(self):
        return json.loads(self.data, object_hook=self.obj.json_object_hook)


def to_dict(obj):
    return json.loads(
        json.dumps(obj, default=lambda o: getattr(o, '__dict__', str(o)))
    )
