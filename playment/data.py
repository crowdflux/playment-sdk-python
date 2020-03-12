from playment.datatype_handler import SensorFusionData, ImageData


class Data:
    def to_dict(data: SensorFusionData or ImageData):
        if type(data) == ImageData:
            return data.__dict__
        data = data.__dict__
        iterator = 0
        while iterator < len(data['frames']):
            data['frames'][iterator] = data['frames'][iterator].__dict__
            iterator_2 = 0
            while len(data['frames'][iterator]['sensors']) > iterator_2:
                data['frames'][iterator]['sensors'][iterator_2] = data['frames'][iterator]['sensors'][iterator_2].__dict__
                if iterator == 0:
                    data['sensor_meta'][iterator_2] = data['sensor_meta'][iterator_2].__dict__
                iterator_2 += 1
            iterator += 1
        return {"sensor_data": data}
