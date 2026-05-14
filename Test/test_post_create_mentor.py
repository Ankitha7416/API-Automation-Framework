import requests
import pytest
import os
from Utils import urls, payload, header, variable

@pytest.mark.create
def test_create_mentor():
    print("\n----- Running Create Mentor API Test -----")
    headers = header.get_headers()
    response = requests.post(urls.create_mentor_url, json=payload.create_mentor_payload(), headers=headers)

    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

    assert response.status_code == 200, "Create Mentor API passed with unexpected status code"
    assert response.json().get("name") == payload.create_mentor_payload().get("name"), "Mentor name mismatch"

    # # Save mentor ID for PUT & DELETE operations
    variable.mentor_id = response.json().get("id")
    file_path = os.path.join(os.path.dirname(__file__), "../Utils/variable.py")
    with open(file_path, "w") as f:
        f.write(f'access_token = "{variable.access_token}"\n')
        f.write(f'mentor_id    = {variable.mentor_id}\n')
        f.write(f'mentor_name = "{variable.mentor_name}"\n')
    # assert variable.mentor_id is not None, "Mentor ID not returned from API"

    # print(f"✅ Mentor created successfully. Stored mentor_id = {variable.mentor_id}")