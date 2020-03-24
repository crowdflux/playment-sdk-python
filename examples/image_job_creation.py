import playment

client = playment.Client("HRGudEwp0b50Vk2Ao87elc5n6mRnLNe+LXW2PWks6Rg")

image_data = playment.ImageData(image_url="http://dfnq1fss3rnqc.cloudfront.net/play/original/b28565f1-5c9a-431a-94de-14d6f2c2f04e")

"""
Image Data job creation
"""
try:
    job = client.create_job(reference_id="55", tag='asad',
                            data=image_data, project_id="1894ef62-19b4-4c57-a3d0-a32162581723")

except playment.PlaymentException as e:
    print(e.code, e.message, e.data)
