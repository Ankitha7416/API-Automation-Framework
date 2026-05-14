import requests
from Utils import urls, header
import pytest

@pytest.mark.employee
def test_get_employee_list():
    print("\n----- Running Get Employee List API Test -----")
    headers = header.get_headers()
    response = requests.get(urls.get_employee_url, headers=headers)

    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

    assert response.status_code == 200, "Employee list API failed"
    assert isinstance(response.json(), list), "Response is not a list"
    assert "name" in response.json()[0], "Employee name key missing in response"

    print("✅ Employee list fetched successfully.")
