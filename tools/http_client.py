import requests

class GectaroHttpClient:

    def __init__(self, base_url, token="2JMbU9I0MQpcxDyxPh87xj_gOee-Hu5o", project_id="87984"):
        self.session = requests.Session()
        self.session.headers["Authorization"] = f"Bearer {token}"
        self.base_url = base_url
        self.project_id = project_id

    def get_projects_resource_requests(self):
        response = self.session.get(
            f"{self.base_url}/v1/projects/" f"{self.project_id}/resource-requests"
        )
        print(response.text)
        return response

    def get_response_status_code(self):
        response = self.session.get(
            f"{self.base_url}/v1/projects/" f"{self.project_id}/resource-requests"
        )
        print(response.text)
        return response.status_code