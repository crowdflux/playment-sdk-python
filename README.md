## Installation
You don't need this source code unless you want to modify the package. If you just want to use the package, just run:

```pip install --upgrade playment-connect```

Install from source with:

```python setup.py install```

Requirements:

``Python 3.5+``

## Documentation
Go at Docs.

## Usage
```
import playment-connect as playment
client = playment.Client(client_key="your x-client-key")
```

```
"""
Preparing a project object
:param project_id: Should be a string of uuid which you can get from the Playment's Customer Dashboard.
"""
PROJECT_ID = "project_id"
project = playment.Project(project_id=PROJECT_ID)
```


####Get Project Summary
```
"""
Get Project Summary
"""
try:
    print(client.get_project_summary(project=project))
except playment.PlaymentException as e:
    print(e.status_code, e.message)
```


####Get Project's Batches Summary
```
"""
Get Project's Batches Summary: This will provide all the batches and their summary
"""
try:
    print(client.get_project_batches_summary(project=project))
except playment.PlaymentException as e:
    print(e.status_code, e.message)
```


####Get Batch Summary
```
"""
Get Batch Summary: This will provide you summary of batch with its jobs and viewer links.
:param batch_id: Should be a string of uuid which you can get from the Playment's Customer Dashboard.
"""
batch = playment.Batch(batch_id="batch_id")
try:
    print(client.get_batch_summary(batch=batch, project=project))
except playment.PlaymentException as e:
    print(e.status_code, e.message)
```


####Creating a Batch
```
"""
Creating new batch: This will return a batch object with batch_id
:param name: Name for the batch. E.g. John
:param label: Label for the batch. E.g. Doe
:param description: Description for the batch. E.g. Alias for unknown.
"""
try:
    batch = playment.Batch(name="test_1", label="test_1", description="testing")
    batch = client.create_batch(batch=batch, project=project)
except playment.PlaymentException as e:
    print(e.message, e.status_code)
```


####Creating a Single-Image Based Job 
```
"""
Define a batch
:param batch_id: Should be a string of uuid which you can get from the Playment's customer dashboard
"""
batch = playment.Batch(batch_id="batch_id")


"""
Creating Image data:
:param image_url: Provide a valid image_url
"""
image_url = "https://example.com/image_url_1"
image_data = playment.ImageData(image_url=image_url)


"""
Defining a job with image data
:param reference_id: This will be unique for every job in a given project.
:param tag: This will be provided by Playment and will only take one type of data. For e.g. ImageData or SensorData.
:param data: This is the data you are sending to Playment.
:param batch: This is an optional argument which will associate the job to the given batch if its left as none,
              the job will be associated with the default batch. It is recommended to create a batch for a set of flus.
:param priority_weight: Range of priority weight is [1,10] and integers only. 10 is the highest priority.
"""
job = playment.Job(reference_id="33", tag='image', data=playment.Data.to_dict(image_data), batch=batch)


"""
Creating the job
"""
try:
    res = client.create_job(job, project=project)
    print(res)
except playment.PlaymentException as e:
    print(e.status_code, e.message)
```


####Creating a Sensor Based Job with Multiple Images/PCDs
```
"""
Define a batch
:param batch_id: Should be a string of uuid which you can get from the Playment's customer dashboard
"""
batch = playment.Batch(batch_id="batch_id")


frames = [
    "https://example.com/image_url_1",
    "https://example.com/image_url_2",
    "https://example.com/image_url_3"
]


"""
Create sensor_data variable
"""
sensor_data = playment.SensorFusionData()


"""
Defining Sensor
:param _id: This is the sensor's id.
:param name: Name of the sensor.
:param primary_view: Only one of the sensor can have primary_view as true.
:param state(optional): If you want this sensor not to be annotated, provide state as non_editable. Default is editable.
"""
sensor_meta = playment.SensorMeta(_id="right", name="right", primary_view=True)


"""
Preparing Frame Data
"""
for i in range(len(frames)):
    # Preparing a sensor with with sensor frame url and sensor_id
    sensor = playment.Sensor(frames[i], sensor_meta.id)
    # Preparing a frame with every sensor
    frame = playment.Frame(str(i), [sensor])
    # Adding the frame in sensor data
    sensor_data.add_frame(frame)


"""
Adding Sensor Meta
"""
sensor_data.add_sensor_meta(sensor_meta)


"""
Defining a job with sensor data
:param reference_id: This will be unique for every job in a given project.
:param tag: This will be provided by Playment and will only take one type of data. For e.g. ImageData or SensorData.
:param data: This is the data you are sending to Playment.
:param batch: This is an optional argument which will associate the job to the given batch if its left as none,
              the job will be associated with the default batch. It is recommended to create a batch for a set of flus.
:param priority_weight(optional): Range of priority weight is [1,10] and integers only. 10 is the highest priority.
                                  Default is 5.
"""
job = playment.Job(reference_id="34", tag='sensor_fusion', data=playment.Data.to_dict(sensor_data), batch=batch)


"""
Creating the job
"""
try:
    res = client.create_job(job, project=project)
    print(res)
except playment.PlaymentException as e:
    print(e.status_code, e.message)

```
