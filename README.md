# API Automation Framework

API automation framework built using Python, pytest, and requests library.

## Tech Stack
- Language: Python
- Framework: pytest
- Library: requests
- Reporting: pytest-html

## Project Structure
- `Test/` - All API test scripts
- `Utils/` - Reusable helpers (URLs, headers, payloads, variables)
- `conftest.py` - Session-level setup and teardown
- `pytest.ini` - Pytest configuration and markers
- `reports/` - HTML test reports

## APIs Tested
- POST Login API
- GET All Employees API
- POST Create Mentor API
- PUT Update Mentor API
- DELETE Delete Mentor API
