import pytest

@pytest.fixture(scope="session", autouse=True) #reusable setup code for all tests
def setup_session():
    print("\n===== Starting API Automation Tests =====")
    yield
    print("\n===== All Tests Completed =====")


# Setup & teardown
# Common reusable methods
# Test initialization
