## Installation
You don't need this source code unless you want to modify the package. If you just want to use the package, just run:

```
pip install --upgrade playment
```

Install from source with:

```
python setup.py install
```

Requirements:

```
Python 3.5+
```

## Documentation
Please visit the [Docs](https://docs.playment.io) to know more about Playment APIs.

## Usage
```
import playment
client = playment.Client(client_key="your x-client-key")
```
It is a secret key required to call Playment APIs. The secret x-client-key ensures that only you are able to access your projects.
The x-client-key can be accessed from the settings page of your dashboard.



#### [Summary](https://github.com/crowdflux/playment-sdk-python/blob/master/examples/summary.py)
* Project Overview
* Batch Summary
* Project's batches Summary


#### Creating a [Batch](https://github.com/crowdflux/playment-sdk-python/blob/master/examples/batch_creation.py)


#### Creating a Single-Image Based [Job](https://github.com/crowdflux/playment-sdk-python/blob/master/examples/image_job_creation.py).


#### Creating a Sensor Based Job with Multiple Images with only camera sensor or multiple image based [Job](https://github.com/crowdflux/playment-sdk-python/blob/master/examples/video_job_creation.py).


#### Creating a Sensor Based Job with Multiple Images/PCDs or Sensor Fusion [Job](https://github.com/crowdflux/playment-sdk-python/blob/master/examples/sensor_job_creation.py).
This can also be used for only LiDAR based jobs.

#### Creating a [Job with metadata](https://github.com/crowdflux/playment-sdk-python/blob/master/examples/job_creation_with_metadata.py).
metadata: You can send any type of data in metadata which can be useful in the task or record of any other data related to that job. metadata should be a type `dict`.


#### Get [Job Result](https://github.com/crowdflux/playment-sdk-python/blob/master/examples/job_result.py).


#### Create Jobs with High Priority and associating them with a batch.
```
image_url = "https://example.com/image_url"
image_data = playment.ImageData(image_url=image_url)

try:
    job = client.create_job(reference_id="55", tag='image',
                            data=image_data, project_id="project_id",
                            priority_weight=10, batch_id="batch_id")
except playment.PlaymentException as e:
    print(e.code, e.message, e.data)
```
