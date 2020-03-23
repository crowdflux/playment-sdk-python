import abc


class Data(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'valid') and
                callable(subclass.load_data_source))