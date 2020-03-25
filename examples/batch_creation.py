import playment

client = playment.Client("HRGudEwp0b50Vk2Ao87elc5n6mRnLNe+LXW2PWks6Rg")

try:
    batch = client.create_batch(name="test_99", label="test_99", description="label",
                                project_id="1894ef62-19b4-4c57-a3d0-a32162581723")
except playment.PlaymentException as e:
    print(e.code, e.message, e.data)
