import playment

client = playment.Client("HRGudEwp0b50Vk2Ao87elc5n6mRnLNe+LXW2PWks6Rg")

frames = [
    "https://example.com/image_url_1",
    "https://example.com/image_url_2",
    "https://example.com/image_url_3"
]


"""
Create sensor_fusion_data variable
"""
sensor_fusion_data = playment.SensorFusionData()


"""
Defining Sensor Meta: Contain details of sensor
:param _id: This is the sensor's id.
:param name: Name of the sensor.
:param primary_view: Only one of the sensor can have primary_view as true.
:param state(optional): If you want this sensor not to be annotated, provide state as non_editable. Default is editable.
"""
sensor_meta = playment.Sensor(_id="right", name="right", primary_view=True)


"""
Preparing Frame Data
"""
for i in range(len(frames)):
    # Preparing a sensor with with sensor frame url and sensor_id
    sensor = playment.SensorFrameObject(frames[i], sensor_meta.id)
    # Preparing a frame with every sensor
    frame = playment.Frame(str(i), [sensor])
    # Adding the frame in sensor data
    sensor_fusion_data.add_frame(frame)


"""
Adding Sensor Meta
"""
sensor_fusion_data.add_sensor_meta(sensor_meta)

sensor_data = playment.SensorData(sensor_fusion_data)

"""
Creating a job with sensor data
:param reference_id: This will be unique for every job in a given project.
:param tag: This will be provided by Playment and will only take one type of data. For e.g. ImageData or SensorData.
:param data: This is the data you are sending to Playment.
:param batch_id: This is an optional argument which will associate the job to the given batch if its left as none,
              the job will be associated with the default batch. It is recommended to create a batch for a set of flus.
:param priority_weight(optional): Range of priority weight is [1,10] and integers only. 10 is the highest priority.
                                  Default is 5.
"""
try:
    job = client.create_job(reference_id="54", tag='sensor_fusion',
                            data=sensor_data, project_id="21b76a0d-1fb5-474f-a17e-6d7506c00f97")

except playment.PlaymentException as e:
    print(e.code, e.message, e.data)
