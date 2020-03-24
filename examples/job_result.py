import playment

client = playment.Client("HRGudEwp0b50Vk2Ao87elc5n6mRnLNe+LXW2PWks6Rg")

"""
Get Job Data
"""
try:
    job_result = client.get_job_data(project_id="00d13bf0-b1c5-41a1-9a86-36677cb9f8d0",
                                     job_id="48284fcd-c6f9-4361-8f7d-feac38b60b4b")
except playment.exception.PlaymentException as e:
    print(e.code, e.message, e.data)
