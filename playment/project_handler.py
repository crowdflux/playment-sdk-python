from playment.batch_handler import Batch


class Project:
    def __init__(self, project_id: str):
        self.project_id = project_id
        self.initialize_project_details()

    def initialize_project_details(self):
        # ToDo: An API call to fetch further details
        self.name = "project_name"
        self.label = "project_label"
        self.created_at = "created_at"
        self.updated_at = "updated_at"

    def fetch_batch(self, batch_id: str):
        return Batch(batch_id)

    def get_summary(self):
        # ToDo: An API call to fetch further details

        summary = "api_response"
        return summary

    def get_batch_summary(self):
        # ToDo: An API call to fetch further details
        summary = "api_response"
        return summary
