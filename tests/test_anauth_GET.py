import requests

base_url = "https://api.gectaro.com"
project_id = "87984"
company_id = "7323"

def test_tasks_unauth():
    response = requests.get(f"{base_url}/v1/projects/{project_id}/tasks")
    assert response.status_code == 401

def test_contractor_type_list_unauth():
    response = requests.get(f"{base_url}/v1/contractor-types")
    assert response.status_code == 401

def test_companies_list_unauth():
    response = requests.get(f"{base_url}/v1/companies")
    assert response.status_code == 401

def test_stocks_list_unauth():
    response = requests.get(f"{base_url}/v1/companies/{company_id}/stocks")
    print(response.text)
    assert response.status_code == 401

def test_stock_operations():
    response = requests.get(f"{base_url}/v1/companies/{company_id}/stock-operations")
    print(response.text)
    assert response.status_code == 401

def test_stocks():
    response = requests.get(f"{base_url}/v2/companies/{company_id}/stocks/stock-operations/stocks")
    print(response.text)
    assert response.status_code == 401

def test_stock_orders():
    response = requests.get(f"{base_url}/v2/companies/{company_id}/stocks/stock-operations/resource-orders")
    print(response.text)
    assert response.status_code == 401

def test_statistics_stocks():
    response = requests.get(f"{base_url}/v1/companies/{company_id}/statistics/stocks")
    print(response.text)
    assert response.status_code == 401

def test_stock_balances():
    response = requests.get(f"{base_url}/v1/companies/{company_id}/stock-balances")
    print(response.text)
    assert response.status_code == 401