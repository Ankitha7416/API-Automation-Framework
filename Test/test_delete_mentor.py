import requests
import pytest
from Utils import urls, payload, header, variable

@pytest.mark.delete
def test_delete_mentor():
    print("\n----- Running Delete Mentor API Test -----")

    # Check if we have mentor ID created earlier
    assert variable.mentor_name is not None, "Mentor ID not found. Run create mentor test first."

    headers = header.get_headers()
    delete_url = urls.delete_mentor_url(variable.mentor_name)

    response = requests.delete(delete_url, headers=headers)

    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

    # Assertions
    assert response.status_code == 200, "Deleted Mentor API Passed with unexpected status code"

    print("✅ Mentor Deleted successfully.")

