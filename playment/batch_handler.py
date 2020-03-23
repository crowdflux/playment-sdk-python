class Batch:
    def __init__(self, batch_id: str = None, name: str = None, label: str = None, description: str = None):
        self._id = batch_id
        self.name = name
        self.label = label
        self.description = description

    def get_batch_details(self):
        # ToDo: An API to fetch further details
        self.name = "batch_name"
        self.label = "batch_label"
        self.description = "batch_description"
        self.created_at = "created_at"
        self.updated_at = "updated_at"

    def get_job_summary(self):
        # ToDo: An API to fetch further details
        summary = "api_response"
        return summary
