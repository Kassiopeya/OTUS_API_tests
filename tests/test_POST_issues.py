import requests

auth_headers = {'Authorization': 'Bearer 2JMbU9I0MQpcxDyxPh87xj_gOee-Hu5o'}
base_url = "https://api.gectaro.com"
project_id = "87984"
company_id = "7323"
user_id = "23385"

def test_post_issues_positive():
    data = {'executor_id': '23385', 'name': 'test', 'creator_id': '23385', 'company_id': '7323'}
    response = requests.post(f"{base_url}/v1/companies/{company_id}/issues", data=data,
                             headers=auth_headers)
    assert response.status_code == 201

def test_post_issues_unauth():
    data = {'executor_id': '23385', 'name': 'test', 'creator_id': '23385', 'company_id': '7323'}
    response = requests.post(f"{base_url}/v1/companies/{company_id}/issues", data=data)
    assert response.status_code == 401
