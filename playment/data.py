# from playment.datatype_handler import SensorFusionData
# from playment.datatype_handler import ImageData
import abc


class Data(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls,subclass):
        return (hasattr(subclass, 'valid') and
                callable(subclass.load_data_source))
