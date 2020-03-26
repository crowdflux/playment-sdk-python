import playment

client = playment.Client("HRGudEwp0b50Vk2Ao87elc5n6mRnLNe+LXW2PWks6Rg")

"""
Get Job Result Data
"""
try:
    job_result = client.get_job_result(project_id="21b76a0d-1fb5-474f-a17e-6d7506c00f97",
                                       job_id="95e64fcf-2f4c-4130-8103-18c6f615e90e")
except playment.exception.PlaymentException as e:
    print(e.code, e.message, e.data)
