import requests

auth_headers = {'Authorization': 'Bearer 2JMbU9I0MQpcxDyxPh87xj_gOee-Hu5o'}
base_url = "https://api.gectaro.com"
project_id = "87984"
company_id = "7323"
group_id = "97407"

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

def test_contractor_type_list():
    response = requests.get(f"{base_url}/v1/contractor-types",
                            headers=auth_headers)
    print(response.text)
    assert response.status_code == 200

def test_companies_list():
    response = requests.get(f"{base_url}/v1/companies",
                            headers=auth_headers)
    print(response.text)
    assert response.status_code == 200

def test_stocks_list():
    response = requests.get(f"{base_url}/v1/companies/{company_id}/stocks",
                            headers = auth_headers)
    print(response.text)
    assert response.status_code == 200

def test_stock_operations():
    response = requests.get(f"{base_url}/v1/companies/{company_id}/stock-operations",
                            headers = auth_headers)
    print(response.text)
    assert response.status_code == 200

def test_stocks():
    response = requests.get(f"{base_url}/v2/companies/{company_id}/stocks/stock-operations/stocks",
                            headers = auth_headers)
    print(response.text)
    assert response.status_code == 200

def test_stock_orders():
    response = requests.get(f"{base_url}/v2/companies/{company_id}/stocks/stock-operations/resource-orders",
                            headers = auth_headers)
    print(response.text)
    assert response.status_code == 200

def test_statistics_stocks():
    response = requests.get(f"{base_url}/v1/companies/{company_id}/statistics/stocks",
                            headers = auth_headers)
    print(response.text)
    assert response.status_code == 200

def test_stock_balances():
    response = requests.get(f"{base_url}/v1/companies/{company_id}/stock-balances",
                            headers = auth_headers)
    print(response.text)
    assert response.status_code == 200