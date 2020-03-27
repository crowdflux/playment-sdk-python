import playment

client = playment.Client("HRGudEwp0b50Vk2Ao87elc5n6mRnLNe+LXW2PWks6Rg")

"""
Prepare Image Data
"""
image_url = "http://dfnq1fss3rnqc.cloudfront.net/play/original/b28565f1-5c9a-431a-94de-14d6f2c2f04e"
image_data = playment.ImageData(image_url=image_url)

"""
Image Data job creation
"""
try:
    job = client.create_job(reference_id="55", tag='image',
                            data=image_data, project_id="1894ef62-19b4-4c57-a3d0-a32162581723")
except playment.PlaymentException as e:
    print(e.code, e.message, e.data)


class JobData:
    sensor_data = sensor_data or None
    image_url = image_url or None
    metadata = extra