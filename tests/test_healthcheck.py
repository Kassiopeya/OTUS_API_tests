import requests

auth_headers = {'Authorization': 'Bearer 2JMbU9I0MQpcxDyxPh87xj_gOee-Hu5o'}
base_url = "https://api.gectaro.com"
project_id = "87984"

def test_resource_requests_healthcheck():
    response = requests.get(f"{base_url}/v1/projects/{project_id}/resource-requests",
                 headers=auth_headers)
    print(response.text)
    assert response.status_code == 200

def test_task_healthcheck():
    response = requests.get(f"{base_url}/v1/projects/{project_id}/tasks",
                            headers=auth_headers)
    print(response.text)
    assert response.status_code == 200

def test_unauth_request():
    response = requests.get(f"{base_url}/v1/projects/{project_id}/tasks")
    print(response.text)
    assert response.status_code == 401



# def test_add_new_GektRequest():
#     request_params = {project_id: project_id,
#                       project_tasks_resource_id: 'value2'}
#     requests.post(f"{base_url}/v1/projects/{project_id}/resource-requests", [id = project_id ])
