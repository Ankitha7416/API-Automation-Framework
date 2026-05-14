import requests
from Utils import urls, payload, variable
import pytest
import os

@pytest.mark.login
def test_post_login():
    print("\n----- Running Login API Test -----")
    response = requests.post(urls.login_url, json=payload.login_payload())
    print("Status Code:", response.status_code)

    aa = response.json()
    ResponseJSON = aa.get("access_token")
    print("Access Token:", ResponseJSON)


    assert response.status_code == 200, "Login API failed"
    variable.access_token = ResponseJSON
    file_path = os.path.join(os.path.dirname(__file__), "../Utils/variable.py")
    with open(file_path, "w") as f:
        f.write(f'access_token = "{ResponseJSON}"\n')
        f.write(f'mentor_id    = {variable.mentor_id}\n')
        f.write(f'mentor_name = "{variable.mentor_name}"\n')
    assert variable.access_token is not None, "Access token not received"
    print("✅ Login successful, token saved.")
