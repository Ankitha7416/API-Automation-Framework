import requests
import pytest
from Utils import urls, payload, header, variable

@pytest.mark.update
def test_update_mentor():
    print("\n----- Running Update Mentor API Test -----")

    # Check if we have mentor ID created earlier
    assert variable.mentor_id is not None, "Mentor ID not found. Run create mentor test first."

    headers = header.get_headers()
    update_url = urls.update_mentor_url(variable.mentor_id)

    response = requests.put(update_url, json=payload.update_mentor_payload(), headers=headers)

    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

    # Assertions
    assert response.status_code == 200, "Update Mentor API Passed with unexpected status code"
    assert response.json().get("name") == payload.update_mentor_payload().get("name"), \
        "Mentor name not updated correctly"

    print("✅ Mentor updated successfully.")

