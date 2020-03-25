import playment

client = playment.Client("HRGudEwp0b50Vk2Ao87elc5n6mRnLNe+LXW2PWks6Rg")

"""
Get project summary
"""
try:
    project_summary = client.get_project_summary(project_id="1894ef62-19b4-4c57-a3d0-a32162581723")
except playment.PlaymentException as e:
    print(e.code, e.message, e.data)

"""
Get batch summary
"""
try:
    batch_summary = client.get_batch_summary(project_id="1894ef62-19b4-4c57-a3d0-a32162581723",
                                             batch_id="17492663-e795-418d-970d-1f293693a5f0")
except playment.PlaymentException as e:
    print(e.code, e.message, e.data)

"""
Get project's batches summary
"""
try:
    project_batch_summary = client.get_project_batches_summary(project_id="1894ef62-19b4-4c57-a3d0-a32162581723")
except playment.PlaymentException as e:
    print(e.code, e.message, e.data)
